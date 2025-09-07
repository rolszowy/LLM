import requests
import json
import os
from dotenv import load_dotenv
from openai import OpenAI
from IPython.display import Markdown, display, update_display

MODEL_GPT = "gpt-4o-mini"
MODEL_LLAMA = "llama3.2"

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

question = """
Please explain what this code does and why:
yield from {book.get("author") for book in books if book.get("author")}
"""

system_prompt = "Respond in Markdown format."

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": question}
]

client = OpenAI()
response = client.chat.completions.create(
    model=MODEL_GPT,messages=messages,
    stream=True,
    )
# print(response.choices[0].message.content)

display_handle = display(Markdown(""), display_id=True)

for chunk in response:
    delta = chunk.choices[0].delta.content or ''
    delta = delta.replace("```", "").replace("markdown", "")
    print(delta, end="", flush=True)

