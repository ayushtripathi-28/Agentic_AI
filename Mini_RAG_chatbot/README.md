
```markdown
# Mini RAG Chatbot

## Project Overview

This project implements a simple Retrieval-Augmented Generation (RAG) chatbot capable of answering questions from a PDF document.

The chatbot extracts text from a PDF, splits the content into chunks, generates embeddings, stores them in a FAISS vector database, retrieves relevant chunks based on user queries, and generates answers using Google Gemini.

---

## Features

- PDF text extraction
- Text chunking
- Embedding generation using Sentence Transformers
- Vector similarity search using FAISS
- Semantic retrieval
- LLM-powered question answering
- Prompt engineering

---

## Tech Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Notebook Environment | Jupyter Notebook |
| PDF Extraction | PyPDF |
| Chunking | LangChain |
| Embeddings | Sentence Transformers |
| Vector Database | FAISS |
| LLM | Google Gemini API |

---

## Project Structure

```text
mini-rag-chatbot/
│
├── Mini_RAG_Chatbot.ipynb
├── README.md
├── requirements.txt
├── .gitignore
├── sample_data/
│   └── sample_rag_dataset.pdf
├── screenshots/
│   ├── Chunking.png
│   |── Context.png
│   |── Embeddings.png
│   └── LLM_Response.png
```

---

## Installation

### 1. Clone Repository

```bash
git clone <your-github-repository-link>
cd mini-rag-chatbot
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Setup Gemini API

1. Visit Google AI Studio:

https://aistudio.google.com/

2. Create an API key.

3. Replace the API key inside the notebook:

```python
genai.configure(api_key="YOUR_API_KEY")
```

---

## How the RAG Pipeline Works

1. Read PDF document
2. Extract text
3. Split text into chunks
4. Generate embeddings
5. Store embeddings in FAISS
6. Convert user query into embedding
7. Retrieve relevant chunks
8. Send retrieved context to Gemini
9. Generate final answer

---

## Sample Workflow

```text
PDF → Chunking → Embeddings → FAISS → Retrieval → Gemini → Final Answer
```

---

## Libraries Used

- pypdf
- langchain
- sentence-transformers
- faiss-cpu
- google-generativeai
- numpy

---

## Future Improvements

- Add Streamlit UI
- Add support for multiple PDFs
- Improve retrieval accuracy
- Add conversation memory
- Deploy as a web application

---

## Learnings

Through this project, I learned:

- Fundamentals of Retrieval-Augmented Generation (RAG)
- PDF text extraction
- Semantic search
- Embeddings and vector databases
- Prompt engineering
- LLM integration using Gemini API

---

## Conclusion

This project demonstrates a complete beginner-friendly implementation of a RAG chatbot using modern AI tools and frameworks.
```
