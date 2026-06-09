Installation
1. Install uv
curl -Ls https://astral.sh/uv/install.sh | sh

or

pip install uv
2. Clone the repository
git clone https://github.com/your-username/project-name.git
cd project-name
3. Create virtual environment
uv venv

Activate it:

Linux / Mac

source .venv/bin/activate

Windows

.venv\Scripts\activate
4. Install dependencies

Using requirements file:

uv pip install -r requirements.txt



# ** Role-Based Access Control (RBAC) RAG Chatbot**

A secure **Role-Based Access Control (RBAC)** chatbot built using **Retrieval-Augmented Generation (RAG)**. The system authenticates users, enforces role-based permissions, retrieves authorized documents, and generates context-aware responses using Large Language Models (LLMs).

## Features

* JWT Authentication
* Bcrypt Password Hashing
* SQLAlchemy ORM
* Role-Based Access Control (RBAC)
* Retrieval-Augmented Generation (RAG)
* Vector Search with Pinecone
* Docling for PDF and Text Parsing
* LangChain Integration
* REST APIs using FastAPI
* Dockerized Deployment
* CI/CD with GitHub Actions

## 🛠️ Tech Stack

### Backend

* Python
* FastAPI

### AI/ML

* LangChain
* Document Parsing → Docling
* Vector Database → Pinecone
* Embeddings → Sentence Transformers
* LLM → Ollama (Llama)

### Database

* SQLite
* SQLAlchemy

### DevOps

* Docker
* GitHub Actions (CI/CD)

## 🔐 User Authentication Flow

```text
User Login
    │
    ▼
Verify Password (Bcrypt)
    │
    ▼
Generate JWT Token
    │
    ▼
Return Token to User
    │
    ▼
User Sends JWT in API Requests
    │
    ▼
Server Verifies JWT
    │
    ▼
Access Granted / Access Denied
```

## 🏢 RBAC Workflow

```text
                    User Login
                         │
                         ▼
                JWT Authentication
                         │
                         ▼
          Extract User Department
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
    Finance          Engineering         HR
        │                │                │
        ▼                ▼                ▼
Financial Docs    Technical Docs    Employee Docs

                         │
                         ▼
                     Marketing
                         │
                         ▼
                 Marketing Docs

                         │
                         ▼
              Query Pinecone Vector DB
                         │
                         ▼
           Filter Documents by Department
                         │
                         ▼
             Send Context to LLM (Ollama)
                         │
                         ▼
                 Generate Response
```

## Key 

-Implemented secure JWT-based authentication and authorization.
- Designed department-level document access using RBAC.
- Built a Retrieval-Augmented Generation (RAG) pipeline using LangChain and Pinecone.
- Integrated Docling for PDF document parsing and ingestion.
- Developed RESTful APIs using FastAPI and SQLAlchemy.
- Containerized the application using Docker.
- Automated build and deployment pipelines using GitHub Actions.

##  Run Application

- Start FastAPI Server

```bash
uvicorn application.main:app --reload
```

-Start Streamlit UI
streamlit run app.py
```bash
streamlit run app.py
```
