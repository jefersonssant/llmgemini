import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("A chave GEMINI_API_KEY não foi encontrada no arquivo .env")

client = genai.Client(api_key=api_key)

config = types.GenerateContentConfig(
    temperature=0.2,
    max_output_tokens=300,
    system_instruction="Você é um assistente técnico direto e objetivo. Responda com informações essenciais."
)

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="Explique resumidamente o que é um token em modelos de linguagem",
    config=config
)

print("Resposta do Modelo:\n", response.text)