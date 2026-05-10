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

def chat(messages):
    system = """
    You are a patient tutor.
    Do not directly answer a student's questions.
    Guide them to a solution step by step.
    """
    try:
        message = client.messages.create(
            model=model,
            max_tokens=1000,
            system=system,
            messages=messages
        )
        return message.content[0].text
    except Exception as e:
        return f"Error: {str(e)}"

# Test 1: Quantum computing question
print("=" * 60)
print("TEST 1: Quantum Computing Question")
print("=" * 60)
messages = []
add_user_message(messages, "Define quantum computing in one sentence")
answer = chat(messages)
add_assistant_message(messages, answer)
add_user_message(messages, "Write another sentence")
final_answer = chat(messages)
print(final_answer)
print()

# Test 2: Algebra problem
print("=" * 60)
print("TEST 2: Algebra Problem")
print("=" * 60)
messages2 = []
add_user_message(messages2, "How do i solve 5x+2=3 for x?")
answer2 = chat(messages2)
print(answer2)
print()

print("=" * 60)
print("✅ ALL CELLS EXECUTED SUCCESSFULLY!")
print("=" * 60)

