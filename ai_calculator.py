from openai import OpenAI

client = OpenAI(api_key="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")

print("AI Calculator")
print("Ask me any math question. Type 'quit' to exit.")

while True:
    user_input = input("\nYour question: ")

    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    # Send request to OpenAI model
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a calculator. Only give numeric results with a short explanation."},
            {"role": "user", "content": user_input}
        ]
    )

    answer = response.choices[0].message.content
    print("Result:", answer)
