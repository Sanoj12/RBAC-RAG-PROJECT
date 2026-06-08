from application.rag.pinecone_store import index
from application.rag.embedding import create_embeddings

from application.rag.llm import generate_answer



def retrieve_answer(query,department):

    query_embedding =create_embeddings(query)

    results = index.query(
        vector=query_embedding,
        top_k=5,
        include_metadata=True,
        filter={
            "department": department
        }
    )
    print("Pinecone Results:", results)
    response = [r["metadata"]["text"] for r in results["matches"]]
    


    prompt= f"""
    
    You are a secure RBAC(role-based access control) assistant.

    Rules:
    -Answer only from Content document
    -do not hallucinate
    -if answer is missing say:'information is not available'
        
        
    context:
    {response}

    Question :{query}
    
    
    
    
    """


    final_answer = generate_answer(prompt)

    return final_answer