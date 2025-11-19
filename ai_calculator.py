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
