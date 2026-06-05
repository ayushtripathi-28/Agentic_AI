# Agentic AI Meeting Preparation Assistant

## Overview

The Agentic AI Meeting Preparation Assistant helps users prepare for upcoming client meetings by automatically gathering information from multiple sources, retrieving historical context, identifying open action items, and generating a concise meeting brief.

This project demonstrates key Agentic AI concepts including:

* Retrieval-Augmented Generation (RAG)
* FAISS Vector Database
* Agentic Planning and Tool Execution
* Short-Term Memory
* Long-Term Memory
* Multi-Tool Architecture
* Groq LLM Integration

---

## Architecture

```text
User Query
    │
    ▼
Planner Agent
    │
    ▼
Tool Selection
    │
    ├── Company Search Tool
    ├── Meeting Notes Tool
    ├── Action Items Tool
    ├── Contacts Tool
    └── Memory Tool
            │
            ▼
      FAISS Retrieval
            │
            ▼
      Context Aggregation
            │
            ▼
       Groq LLM
            │
            ▼
      Meeting Brief
```

---

## Features

### Retrieval-Augmented Generation (RAG)

* Converts company records into LangChain Documents
* Generates embeddings using Sentence Transformers
* Stores vectors in FAISS
* Retrieves relevant company information using semantic search

### Short-Term Memory

Maintains conversation context using:

```python
InMemoryChatMessageHistory
```

### Long-Term Memory

Stores information across sessions using:

```text
memory.json
```

Examples:

* Important clients
* Meeting history
* User preferences

### Agentic Workflow

The assistant does not directly answer questions.

Instead it:

1. Understands the user request
2. Creates a plan
3. Selects tools
4. Retrieves information
5. Generates a meeting brief

---

## Project Structure

```text
project_root/

├── Meeting_preparation_assistant.ipynb
├── README.md
├── requirements.txt
├── .env
├── memory.json
├── screenshots/
│   ├── Embedding_response.png
│   ├── Final_response.png
│   └── Index.png
```

---

## Setup Instructions

### Clone Repository

```bash
git clone <repository-url>
cd project_root
```

### Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```text
GROQ_API_KEY=your_groq_api_key
```

---

## Running the Project

Open Jupyter Notebook:

```bash
jupyter notebook
```

Run:

```text
Meeting_preparation_assistant.ipynb
```

Execute all cells.

---

## Sample Query

```text
Prepare me for my meeting with Acme Corp
```

---

## Sample Workflow

### Step 1

User enters:

```text
Prepare me for my meeting with Acme Corp
```

### Step 2

Planner creates tool execution plan:

```json
{
  "tools": [
    {
      "tool_name": "company_search",
      "company_name": "Acme Corp"
    },
    {
      "tool_name": "meeting_notes",
      "company_name": "Acme Corp"
    }
  ]
}
```

### Step 3

Tools retrieve information.

### Step 4

Groq generates a meeting brief.

---

## Sample Output

### Company Overview

Acme Corp is a manufacturing company focused on AI-powered logistics optimization.

### Previous Meetings

* Discussed AI logistics implementation
* Requested pricing proposal

### Open Action Items

* Send Proposal
* Schedule Workshop

### Stakeholders

* Sarah Johnson (Procurement Director)
* Michael Chen (CTO)

### Talking Points

* AI Logistics Roadmap
* Proposal Review
* Workshop Planning

### Next Steps

* Finalize proposal
* Schedule implementation workshop

---

## Technologies Used

* Python
* Pandas
* NumPy
* LangChain
* FAISS
* Sentence Transformers
* Groq
* Python Dotenv

---

## Future Improvements

* ChromaDB Integration
* Real Function Calling
* CRM Integration
* Email Retrieval
* Calendar Integration
* Multi-Agent Architecture
* Web Search Tool
* Persistent Database Storage

---

## Author

Agentic AI Meeting Preparation Assistant Assignment Project
