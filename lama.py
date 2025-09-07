import requests
import json
import os
from ollama import chat
from ollama import ChatResponse

MODEL_GPT = "gpt-4o-mini"
MODEL_LLAMA = "llama3.2"

question = """
Please explain what this code does and why:
yield from {book.get("author") for book in books if book.get("author")}
"""

system_prompt = "Respond in Markdown format."

# response: ChatResponse = chat(model=MODEL_LLAMA, messages=[
#     {"role": "system", "content": system_prompt},
#     {"role": "user", "content": question}
# ])
# print(response['message']['content'])

stream: ChatResponse = chat(model=MODEL_LLAMA, messages=[
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": question}],
    stream=True,
    )

for chunk in stream:
    print(chunk['message']['content'], end="", flush=True)
