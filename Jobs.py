import os
from ollama import Client

client = Client(host="http://127.0.0.1:11434")

model_name = "llama3.2"

def chat(prompt: str) -> None:
    stream = client.chat(
        stream=True,
        model=model_name,
        options={'temperature': 0.6},
        messages=[
            {
                "role": "system",
                "content": """If user wrote a job List the related jobs 
                you must write only jobs names with number bullet""",
            },
            {
                "role" : "user",
                "content": prompt
            }
        ],
    )

    for chunk in stream:
        content = chunk["message"]["content"]
        print(content, end="", flush=True)

    input("\nPress Enter to continue ...")

while True:
    os.system(command="cls")
    prompt = input("Enter Your Job : ")

    if prompt.lower() in ["quit", "exit"]:
        break

    chat(prompt=prompt)