"""_summary_
DeepSeek API request example
"""

import os
import requests
import json

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Set up the API key and endpoint
api_key = os.getenv("DEEPSEEK_API_KEY")
api_url = "https://api.deepseek.com/v1/chat/completions"

headers = {
    "Authorization": api_key,
    "Content-Type": "application/json"
}

data = {
    "model": "deepseek-r1",
    "messages": [{"role": "user", "content": "Como criar um programa em Python?"}]
}

response = requests.post(
  api_url,
  headers=headers,
  json=json.dumps(data),
  )
print(response)