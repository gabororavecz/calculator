import ollama

print("AI Calculator (Ollama)")
print("Ask me any math question. Type 'quit' to exit.")

while True:
    user_input = input("\nYour question: ")

    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    response = ollama.chat(
        model="llama3",
        messages=[
            {"role": "system", "content": "You are a calculator. Only give numeric results with a short explanation."},
            {"role": "user", "content": user_input}
        ]
    )

    answer = response['message']['content']
    print("Result:", answer)
