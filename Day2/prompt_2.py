import ollama
response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content": "act as a btech student and answer give the defination of AI in 2 lines and say the 3 main types of ai in simple terms in points"
        }
    ]
)
print(response["message"]["content"])