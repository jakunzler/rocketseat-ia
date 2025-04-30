import google.generativeai as genai
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente
load_dotenv()

# Define a chave da API da Google (obtenha no console do Google AI Studio)
GOOGLE_API_KEY = os.getenv("GOOGLE_AI_STUDIO_API_KEY")

# Configura a autenticação
genai.configure(api_key=GOOGLE_API_KEY)

# for m in genai.list_models():
#     print(m.name)

# Cria o modelo (equivalente ao gpt-3.5-turbo da OpenAI)
model = genai.GenerativeModel(model_name='models/gemini-1.5-pro')

# Faz a chamada ao modelo
response = model.generate_content("Which are the 5 top artists in the world?")

# Imprime a resposta
print(response.text)
