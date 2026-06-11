import os
from dotenv import load_dotenv
from anthropic import Anthropic
load_dotenv()  # Load environment variables from .env file

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)

messages = []

def add_user_message(messages, content):
    messages.append({
        "role": "user",
        "content": content,
    })

def add_assistant_message(messages, content):
    messages.append({
        "role": "assistant",
        "content": content,
    }) 

def chat(messages):
    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            print("Exiting the chatbot. Goodbye!")
            break
        add_user_message(messages, user_input)
        response = client.messages.create(
            max_tokens=1024,
            messages=messages,
            model="claude-sonnet-4-5",
        )
        assistant_response = response.content[0].text
        print(f"Assistant: {assistant_response}")
        add_assistant_message(messages, assistant_response) 

if __name__ == "__main__":
    print("Welcome to the simple chatbot! Type 'exit' to quit.")
    chat(messages)
