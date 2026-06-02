# Conversational RAG Assistant with Tool Calling

## Project Overview

This project implements a Conversational Retrieval-Augmented Generation (RAG) Assistant capable of:

* Answering questions from a PDF document using semantic search.
* Maintaining conversation history and context.
* Rewriting follow-up questions into standalone questions.
* Using external tools when required.
* Routing between RAG-based answers and tool-based answers.

The project demonstrates the complete workflow of a conversational AI assistant using embeddings, vector search, retrieval, memory, and tool calling.

---

## Memory Implementation

The assistant maintains chat history using a Python list of messages.

Example:

```python
chat_history = [
    {"role": "user", "content": "What is RAG?"},
    {"role": "assistant", "content": "RAG stands for Retrieval-Augmented Generation."}
]
```

Memory is used for:

1. Tracking previous user interactions.
2. Understanding follow-up questions.
3. Providing context-aware responses.

Before retrieval, follow-up questions are rewritten into standalone questions using the LLM.

Example:

User: What is RAG?
User: Explain it more.

Rewritten Question:

Explain Retrieval-Augmented Generation in more detail.

---

## Tool Explanation

The project includes external tools defined using JSON schemas.

### 1. get_current_time()

Returns the current system date and time.

### 2. calculate(expression)

Evaluates mathematical expressions.

Example:

```python
calculate("25 * 40")
```

Output:

```text
1000
```

Tool Calling Flow:

1. User asks a question.
2. LLM decides whether a tool is required.
3. Tool request is returned as JSON.
4. Python executes the tool.
5. Result is sent back to the LLM.
6. Final natural-language response is generated.

---

## Steps to Run the Project

### 1. Clone Repository

```bash
git clone <repository-url>
cd conversational-rag-assistant
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

Linux/Mac:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create .env File

```env
GROQ_API_KEY=your_api_key_here
```

### 5. Launch Jupyter Notebook

```bash
jupyter notebook
```

Open:

```text
Conversational_RAG_Assistant.ipynb
```

### 6. Run All Cells

Execute the notebook from top to bottom.

### 7. Start Chatting

Example:

```text
User: What is RAG?
User: Explain it more.
User: What is 25 * 40?
User: What time is it?
```

---

## Project Structure

```text
conversational-rag-assistant/
│
├── Conversational_RAG_Assistant.ipynb
├── tools.py
├── README.md
├── requirements.txt
└── screenshots/
```
