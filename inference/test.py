from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

llm = ChatOllama(model="snippetai")

prompt = ChatPromptTemplate.from_template(
    "You are SnippetAI.\nQuestion: {question}"
)

chain = prompt | llm

response = chain.invoke({"question": "Explain binary search using python."})
print(response.content)