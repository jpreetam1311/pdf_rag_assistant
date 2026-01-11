# 📄 Retrieval-Augmented PDF Assistant (RAG + Vector Database)

> **Applied AI Project (Prototype)**  
> **Purpose:** Exploration of retrieval-augmented generation for organizational knowledge access and decision support  
> **Context:** CLI-based prototype of a scalable RAG system designed for enterprise and internal data workflows

---

## 📌 Project Overview

This project implements a **Retrieval-Augmented Generation (RAG) assistant** that enables conversational querying over PDF documents. It dynamically ingests document sources, converts content into vector embeddings, and retrieves the most relevant sections at query time to generate **grounded, source-aware responses**.

While implemented as a command-line prototype, this system represents a **core AI capability** commonly used in production knowledge platforms: combining **vector search** with **LLM reasoning** to enable reliable access to unstructured organizational data.

The design intentionally mirrors patterns used in internal tools, automation platforms, and enterprise AI systems.

---

## System Scope

This project implements the core retrieval and generation logic of a real-time RAG system in a simplified, CLI-based form.

The emphasis is on architectural correctness and extensibility rather than production hardening. The same design can be extended to support real-time ingestion, UI-based access, and enterprise deployment.

---

## 🎯 Problem Framing (Generalized)

Organizations accumulate large volumes of unstructured documents (policies, reports, manuals, contracts), but accessing this knowledge is often:
- Fragmented across files and systems
- Dependent on keyword search
- Time-consuming for analysts and operators

This project explores the question:

> **How can AI enable accurate, explainable, and scalable access to organizational knowledge while minimizing hallucination and maintaining source traceability?**

The emphasis is on **decision support**, not open-ended text generation.

---

## 🧠 System Architecture

The system follows a modular **RAG pipeline**, designed for clarity, extensibility, and data governance.

### 1. Ingestion
- PDF URLs are provided dynamically at runtime
- Documents are downloaded, parsed, and chunked into manageable text segments

### 2. Vectorization & Storage
- Each chunk is converted into a vector embedding
- Embeddings and metadata are stored in **PostgreSQL using pgvector**
- Enables semantic similarity search while retaining relational structure

### 3. Retrieval
- User queries are embedded at runtime
- Semantic similarity search retrieves the most relevant document chunks

### 4. Generation
- Retrieved chunks are passed as bounded context to the language model
- Responses are generated strictly from retrieved content, preserving grounding

This architecture reflects a **production-grade pattern** for RAG systems.

---

## 🧩 Product-Oriented Use Cases

Although demonstrated on PDFs, the underlying capability generalizes to:

- Internal knowledge bases and policy assistants
- Analyst and research workflows
- Compliance and audit support
- Technical documentation search
- Customer support enablement
- AI copilots for enterprise tools

The assistant acts as a **trusted interface to knowledge**, rather than a creative text generator.

---

## 🔍 Decision-Making Impact

From a product and analytics perspective, this system:
- Reduces time spent searching across documents
- Improves answer reliability through retrieval grounding
- Enables explainable responses tied to source material
- Supports faster, higher-confidence decisions
- Scales across teams without duplicating knowledge

This aligns with how RAG is used in real-world AI platforms: **augmenting humans, not replacing them**.

---

## ⚙️ Key Design Constraints & Trade-offs

- Uses vector search to prioritize semantic relevance over keyword matching
- Stores embeddings in a relational database to balance flexibility and governance
- Designed for clean re-indexing when documents or models change
- Emphasizes grounding and traceability over open-ended creativity
- Operates locally, with external APIs limited to embeddings and inference

These choices reflect practical trade-offs in enterprise AI systems.

---

## 🛠️ Implementation Notes

- Supports one or multiple PDF sources per session
- Persists chat history and session state
- Clean re-ingestion supported when document sets evolve
- CLI interface chosen for simplicity and experimentation

---

## 🔮 Future Extensions

Planned or potential enhancements include:
- Migration to a dedicated vector database at scale
- Hybrid retrieval (semantic + keyword)
- Role-based access control and permissions
- Document versioning and lineage tracking
- UI integration for non-technical users
- Expansion beyond PDFs to other data types

---

## 🧑‍💻 Author & Context

- **Author:** Preetam Jena  
- **Context:** Applied AI and product experimentation  
- **Focus:** Retrieval-augmented generation, vector databases, and AI-driven knowledge systems
