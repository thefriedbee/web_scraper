import os
from dotenv import load_dotenv

from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
# print("api_key:", api_key)

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set")


client = OpenAI(api_key=api_key)
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a joke."}
    ]
)

print(response.choices[0].message.content)
