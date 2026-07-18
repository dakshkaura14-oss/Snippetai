import requests

url=(
     "https://datasets-server.huggingface.co/rows"
     "?dataset=TinyPixel%2Ftiny-codes"
     "&config=default"
     "&split=train"
     "&offset=0"
     "&length=100")

response=requests.get(url)

data=response.json()

rows=[item['row'] for item in data["rows"]]

print(repr(type(rows[0]["text"])))

import re
data_set=[]
for row in rows:
    text=row["text"]
    instruction = re.search(
        r"<\|im_start\|>USER:\s*(.*?)\s*<\|im_end\|>",
        text,
        re.DOTALL
    ).group(1)

    response = re.search(
        r"<\|im_start\|>ASSISTANT:\s*(.*?)\s*<\|im_end\|>",
        text,
        re.DOTALL
    ).group(1)

    sample = {"user": instruction,
            "content": response}
    data_set.append(sample)

import json

with open("dataset.json", "w", encoding="utf-8") as f:
    json.dump(data_set, f, indent=4, ensure_ascii=False)


    