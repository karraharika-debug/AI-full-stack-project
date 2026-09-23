import ollama
response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "system",
            "content": "you are teaching a 5 year old child give me answer in 2 lines only"
        },
        {
            "role": "user",
            "content": "say 1 poem of nurssary class"
        }
    ]
)
print(response["message"]["content"])