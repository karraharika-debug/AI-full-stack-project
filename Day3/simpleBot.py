import ollama
while True:
    question=input("Ask the question")
    if question.lower() == "exit":
        break
    response = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {
            "role": "system",
            "content": "Give the answer in 2-3 lines only."
            },
            {
            "role": "user",
            "content": question 
            }
        ]
    )
    print(response["message"]["content"])