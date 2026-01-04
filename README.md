# PDF RAG Assistant (CLI)

This project is a command-line PDF assistant that enables conversational querying over PDF documents using a **Retrieval-Augmented Generation (RAG)** approach.

The system dynamically ingests PDF URLs, stores document embeddings in a vector database, and retrieves relevant content at query time to generate responses grounded in the source documents.

---

## What it does

- Accepts one or multiple PDF URLs at runtime  
- Parses and chunks PDF content for processing  
- Converts text chunks into vector embeddings  
- Stores embeddings in PostgreSQL with pgvector  
- Retrieves relevant document sections using semantic similarity  
- Generates responses grounded in the uploaded PDFs  
- Persists chat history and session state  

---

## High-level architecture

### 1. Ingestion
- PDF URLs are collected dynamically at runtime  
- PDFs are downloaded, parsed, and split into chunks  

### 2. Storage
- Each chunk is converted into a vector embedding  
- Embeddings and metadata are stored in PostgreSQL using pgvector  

### 3. Retrieval
- User queries are embedded at runtime  
- Semantic similarity search retrieves the most relevant chunks  

### 4. Generation
- Retrieved chunks are passed to the language model as context  
- Responses are generated based strictly on document content  

---

## Notes

- Designed as a learning project to understand practical RAG implementations  
- Supports clean re-indexing when PDFs or embedding models change  
- Fully local execution, with external API usage limited to embeddings and LLM inference  

---

## Setup

Detailed setup instructions and environment configuration are available **on request**.
