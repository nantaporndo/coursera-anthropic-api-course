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

def chat(messages,system=None):

    parameters = {
        "max_tokens": 1024,
        "messages": messages,
        "model": "claude-sonnet-4-5",
    }

    if system:
        parameters["system"] = system

    response = client.messages.create(**parameters) 

    return response.content[0].text

messages = []

    system = """You are a patient math tutor.
    Do not directly answer the question. Instead, ask the student questions to guide them to the answer.
    If the student is stuck, give them a hint."""

add_user_message(messages, "What is 2 + 2?")

answer = chat(messages)
print(answer)

# add_assistant_message(messages, "Write another message.")

# answer = chat(messages, system=system)
# print(answer)
