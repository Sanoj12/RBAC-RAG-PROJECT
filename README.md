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


Title:Role Based Access Control System(RBAC) RAG Chatbot

##A secure Role-Baesd Access Control(RBAC) Chatbot built using  Retrieval-Augmented Generation (RAG).The system autenticates users enforces role-based permissions,retreive authorized documents,and generate context-aware response using LLMs.


Features

-JWT Autentication
-Bcrypt Password Hashing
-SQLAlchemy ORM
-RBAC
-RAG
-Vector Search with Pinecone
-Docling for PDF and text parsing
-langchain
-REST APIs using FastAPI
-Dockerized Deployment
-CI/CD with GitHub Actions



## tech stack

1.Backend:
-Python
-FastAPI

2.AI/ML:
-Langchain
-Document Parsing-> Docling
-VectorDB -> Pinecone
-Embeddings -> Sentence Transformer
-LLM -> Ollama(llama)

3.Database
-Sqlite
-SQLAlchemy



4.DevOps

-Docker
-CI/CD Tool -> Github Actions


## User Authenication flow


User Login  ->   Verify Password using Bcrypt ->  Generate JWT Token ->   Return Token to user -> User sends JWT in api requestss -> server verifies jwt  -> Access granted/Access denied




### RBAC WORKFLOW



                    User Login
                         │
                         ▼
                JWT Authentication
                         │
                         ▼
                Extract User based on department
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
              Filter Documents by department
                         │
                         ▼
              Send Context to LLM(Ollama)
                         │
                         ▼
                 Generate Response



## key

- Implemented secure JWT-based authentication and authorization.
- Designed department-level document access using RBAC.
- Built a Retrieval-Augmented Generation (RAG) pipeline using LangChain and Pinecone.
- Integrated Docling for PDF document parsing and ingestion.
- Developed RESTful APIs using FastAPI and SQLAlchemy.
- Containerized the application using Docker.
- Automated build and deployment pipelines using GitHub Actions.




## run application


uvicorn application.main:app --reload 



streamlit run app.py
