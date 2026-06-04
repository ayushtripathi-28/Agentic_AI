# Semantic Search Engine using FAISS

## Objective

Build a mini semantic search engine using:

- Sentence Transformers
- FAISS Vector Database
- Cosine Similarity Search

This project demonstrates the core concept behind Retrieval-Augmented Generation (RAG) systems.

---

## Features

- Generate sentence embeddings using all-MiniLM-L6-v2
- Store embeddings in FAISS
- Perform semantic similarity search
- Retrieve Top-K matching results
- Interactive command-line interface

---

## Installation

### Clone Project

```bash
git clone <repository_url>
cd semantic-search-faiss
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
python semantic_search_faiss.py
```

---

## Knowledge Base

The project contains 10 customer-support related documents covering:

- Password Reset
- Billing
- Login Issues
- Account Management
- Refunds
- Security
- Subscription Plans

---

## Embedding Model

Model Used:

```python
all-MiniLM-L6-v2
```

Output Embedding Size:

```python
384 dimensions
```

Expected Shape:

```python
(10, 384)
```

---

## FAISS Index

Index Type:

```python
faiss.IndexFlatL2(384)
```

Normalization:

```python
faiss.normalize_L2()
```

Normalization allows L2 distance to behave similarly to cosine similarity.

---

## Example Queries

### Query 1

```text
How do I change my password?
```

Expected Match:

```text
To reset your password, click on the Forgot Password link on the login page.
```

---

### Query 2

```text
Where can I see my invoice?
```

Expected Match:

```text
Billing invoices can be downloaded from the billing section of your account.
```

---

### Query 3

```text
I am unable to access my account
```

Expected Match:

```text
If your account is locked, contact customer support for assistance.
```

---

## Output Format

```text
Rank | Score | Matched Sentence
```

Example:

```text
Rank  Score      Matched Sentence
---------------------------------------------------------
1     0.4213     To reset your password...
2     0.5876     If you cannot log in...
3     0.6921     Two-factor authentication...
```

---

## Project Structure

```text
semantic-search-faiss/
│
├── semantic_search_faiss.py
├── requirements.txt
└── README.md
```

---

## Concepts Covered

- Embeddings
- Vector Databases
- FAISS
- Cosine Similarity
- Semantic Search
- Retrieval-Augmented Generation (RAG)

---

## Author

Ayush Tripathi