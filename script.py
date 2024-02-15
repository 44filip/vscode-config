import os
from openai import OpenAI


client = OpenAI(
    # This is the default and can be omitted
    api_key= open("OPENAI_API_KEY", "r").read()
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Please show me a cyber security related daily quote.",
        }
    ],
    model="gpt-3.5-turbo",
)