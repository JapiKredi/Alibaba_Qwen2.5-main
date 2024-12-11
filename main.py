import os

from openai import OpenAI

# Input a long text file
with open("example.txt", "r", encoding="utf-8") as f:
    text = f.read()
user_input = text + "\n\nSummarize the above text."

client = OpenAI(
    api_key=os.getenv("YOUR_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

completion = client.chat.completions.create(
    model="qwen-turbo-latest",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_input},
    ],
)

print(completion.choices[0].message)
