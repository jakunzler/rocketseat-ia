"""
File expore DeepSeek API
"""

import os

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Set up the API key and endpoint
api_key = os.getenv("DEEPSEEK_API_KEY")

from openai import OpenAI

client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False
)

print(response.choices[0].message.content)