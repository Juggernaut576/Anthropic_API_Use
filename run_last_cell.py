from dotenv import load_dotenv
import os
from anthropic import Anthropic

load_dotenv()

client = Anthropic()
model = "claude-opus-4-1"

def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)

def chat(messages, system=None, temperature=None):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
    }

    if system:
        params["system"] = system

    if temperature is not None:
        params["temperature"] = temperature

    message = client.messages.create(**params)
    return message.content[0].text

# Run last cell
print("=" * 60)
print("Running Last Cell: Movie Idea Generation")
print("=" * 60)
messages4 = []
add_user_message(messages4, "Generate a one sentence movie idea")
answer = chat(messages4, temperature=2.0)
print(answer)
print()

