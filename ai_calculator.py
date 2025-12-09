from openai import OpenAI

client = OpenAI(api_key="PUT YOUR API KEY HERE")

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
