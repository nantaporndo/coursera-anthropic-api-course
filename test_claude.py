import os
from dotenv import load_dotenv
from anthropic import Anthropic
load_dotenv()  # Load environment variables from .env file

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)

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
    response = client.messages.create(
        max_tokens=1024,
        messages=messages,
        model="claude-sonnet-4-5",
    )
    return response.content[0].text

messages = []

add_user_message(messages, "Define the term 'artificial intelligence'. for 40 words or less.")

answer = chat(messages)
print(answer)

add_assistant_message(messages, "Write another message.")

answer = chat(messages)
print(answer)
