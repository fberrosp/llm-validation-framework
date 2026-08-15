from openai import OpenAI

client = OpenAI()

# Get the response from the LLM for a given prompt.


def get_llm_response(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
