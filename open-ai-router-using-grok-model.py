import chromadb
from openai import OpenAI

CHROMA_PATH = r"chroma-db"

chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)
collection = chroma_client.get_or_create_collection(name="pdf-files")

user_query = "who is NICOLE LURIE?"

results = collection.query(
query_texts=[user_query],
n_results= 4 )

print("\nRetrieved documents:\n")
for i, doc in enumerate(results['documents'][0]):
    print(f"{i+1}. {doc}\n{'-'*50}\n")


system_prompt = ""f"""
helpful assistant Only answer based on the knowledge provided below If you don't know the answer, just say: Idon't know.
{results['documents'][0]}
"""""


client = OpenAI(base_url="https://openrouter.ai/api/v1",
    api_key="your openrouter.ai api key")



response = client.chat.completions.create(

    model="x-ai/grok-3-mini", 

    messages=[

        {

            "role": "system", 

            "content": system_prompt

        },

        {

            "role": "user", 

            "content": user_query

        }

    ]

)

print("\nLLM Answer:\n")
print(response.choices[0].message.content)


