import chromadb
from dotenv import load_dotenv
import requests, json

CHROMA_PATH = r"chroma-db"

chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)
collection = chroma_client.get_or_create_collection(name="pdf-files")

user_query = input("prompt\n\n")

results = collection.query(
query_texts=[user_query],
n_results= 4 )

print("\nRetrieved documents:\n")
for i, doc in enumerate(results['documents'][0]):
    print(f"{i+1}. {doc}\n{'-'*50}\n")


    system_prompt = f"""
23.You are a helpful assistant. You answer questions. Only answer based on the knowledge provided
below. Don't make things up. If you don't know the answer, just say: I
don't know.
--------------------
Data:
{results['documents'][0]}
"""

prompt = f"{system_prompt}\n\nQuestion: {user_query}"

url = "http://localhost:11434/api/generate"
data = {"model": "hf.co/Qwen/Qwen2.5-7B-Instruct-GGUF:latest", "prompt": prompt, "stream": True}
response = requests.post(url, json=data, stream=True)

full_text = ""
for line in response.iter_lines():
    if line:
        decoded = json.loads(line)
        if "response" in decoded:
            full_text += decoded["response"]

print("\nLLM Answer:\n")
print(full_text)