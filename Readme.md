# ````markdown
# SnippetAI

SnippetAI is a fine-tuned Qwen-based language model designed for generating and explaining programming snippets. This repository contains the training, inference, and deployment code for the project.

> **Note:** The trained model (`Qwen_Merged`) and the generated `.gguf` file are **not included** in this repository because of their size.

---

## Project Structure

```text
DRDO_Project/
│
├── inference/
│   ├── inference.py
│   ├── app.py
│   └── requirements.txt
│
├── frontend/
│
├── Modelfile
├── README.md
├── .gitignore
└── Qwen_Merged/          <-- Place the merged Hugging Face model here
```

---

## Prerequisites

- Python 3.10+
- Git
- Ollama
- llama.cpp
- CUDA-enabled GPU (recommended)

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

---

# Step 1 - Clone the Repository

```bash
git clone <repository-url>
cd DRDO_Project
```

---

# Step 2 - Place the Merged Model

Copy your merged Hugging Face model into:

```text
DRDO_Project/
└── Qwen_Merged/
```

The directory should contain files such as:

```text
config.json
generation_config.json
model.safetensors
tokenizer.json
tokenizer_config.json
special_tokens_map.json
```

---

# Step 3 - Clone llama.cpp

```bash
git clone https://github.com/ggml-org/llama.cpp
cd llama.cpp
```

Build llama.cpp according to your operating system.

---

# Step 4 - Convert the Hugging Face Model to GGUF

Run the conversion script:

```bash
python convert_hf_to_gguf.py ../Qwen_Merged --outfile snippetai.gguf
```

After conversion you should have:

```text
snippetai.gguf
```

Move or copy the file into your project directory if desired.

---

# Step 5 - Install Ollama

Verify the installation:

```bash
ollama --version
```

---

# Step 6 - Create the Modelfile

Create a file named `Modelfile`.

Example:

```text
FROM ./snippetai.gguf

PARAMETER temperature 0.7
PARAMETER top_p 0.9

SYSTEM """
You are SnippetAI, an AI assistant specialized in programming and code generation.
Provide clear, accurate, and concise answers.
"""
```

---

# Step 7 - Create the Ollama Model

Run:

```bash
ollama create snippetai -f Modelfile
```

If successful, the model will be registered with Ollama.

Verify:

```bash
ollama list
```

---

# Step 8 - Run the Model

```bash
ollama run snippetai
```

Example:

```text
>>> Explain binary search using Python.
```

---

# Step 9 - Run the Python Inference Script

```bash
cd inference

python inference.py
```

or

```bash
python app.py
```

depending on your project structure.

---

# Example Prompt

```text
Write a Python function to reverse a linked list.
```

---

# Troubleshooting

## Model not found

```bash
ollama list
```

If the model is missing:

```bash
ollama create snippetai -f Modelfile
```

---

## GGUF file missing

Ensure:

```text
snippetai.gguf
```

exists in the same directory as the `Modelfile`.

---

## CUDA not detected

Verify PyTorch:

```python
import torch
print(torch.cuda.is_available())
```

---

## Project Features

- Fine-tuned Qwen model
- GGUF conversion
- Ollama integration
- Python inference
- LangChain compatibility
- Local offline execution

---

## Notes

This repository intentionally excludes:

- `Qwen_Merged/`
- `.gguf` files
- checkpoints
- datasets

These artifacts should be stored separately because of their size.

---

## License

This project is intended for educational and research purposes.
````
