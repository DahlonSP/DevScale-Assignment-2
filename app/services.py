import os

from openai import OpenAI

from app.settings import settings

from app.schema import MessageInput, CompletionResponse

def generate_response(MessageInput) -> str:
    client = OpenAI(base_url=settings.sumopod_base_url, api_key=settings.sumopod_api_key)
    completion = client.chat.completions.create(
        model="nvidia/nemotron-3-nano-30b",
        messages=[{"role":"user", "content":MessageInput}],
    )

    response = completion.choices[0].message.content
    return response or "No response from LLM"
