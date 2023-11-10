# Ref: https://cookbook.openai.com/examples/how_to_format_inputs_to_chatgpt_models
# https://github.com/openai/openai-python/tree/main#installation
# https://pypi.org/project/python-dotenv/
# https://platform.openai.com/docs/api-reference/chat/object
# https://platform.openai.com/tokenizer

from dotenv import load_dotenv
from openai import OpenAI
from rich.console import Console
import os

console = Console()

load_dotenv(dotenv_path="./.env")
API = os.getenv(key="OPENAI_API_KEY")

client = OpenAI(api_key=API)
MODEL = "gpt-3.5-turbo-1106"

def response(content):
    completions = client.chat.completions.create(
        model=MODEL,
        max_tokens=100,
        messages=[
            {
                "role": "user",
                "content": content,
            }
        ],
    )
    result = completions.choices[0].message.content
    console.print(f"chat-GPT : {result}", style="#16a180")


console.line()
console.rule(title="ถาม chat-GPT", style="#16a180")

while True:
    prompt = console.input("user : ")
    if prompt == "":
        console.rule(title="จบการทำงาน", style="#16a180")
        break
    response(prompt)
