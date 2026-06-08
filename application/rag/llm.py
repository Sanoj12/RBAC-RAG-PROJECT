

import ollama

def generate_answer(prompt):
    
    response = ollama.chat(
        model = "llama3",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
        
    )
    print(response)
    return response["message"]["content"]
    