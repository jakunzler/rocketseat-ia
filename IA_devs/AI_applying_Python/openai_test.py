"""
Teste de Open AI API
"""

from openai import OpenAI

from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

response = client.responses.create(
  model="gpt-3.5-turbo",
  input="Tell me a three sentence bedtime story about a unicorn."
)

print(response)
