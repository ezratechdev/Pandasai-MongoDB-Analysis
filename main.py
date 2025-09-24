import os
from dotenv import load_dotenv
import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm import LLM
from pymongo import MongoClient
import requests

# Load environment varibles from .env
load_dotenv()

# Connection is made from the uri connection string
uri = os.getenv('mongo_string')
database_name = os.getenv('database')
collection_name = os.getenv('collection')
llm_base = os.getenv("api_base")
llm_token = os.getenv("api_token")
llm_model = os.getenv("model")


# Used AI for this code here - Connector for pandas AI with deepseel
class DeepSeekLLM(LLM):
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.deepseek.com/v1"  # Check DeepSeek's actual API endpoint
        self._temperature = 0.1
        self._max_tokens = 1000

    def call(self, prompt: str) -> str:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        
        payload = {
            "model": "deepseek-chat",  # Use the appropriate DeepSeek model
            "messages": [{"role": "user", "content": prompt}],
            "temperature": self._temperature,
            "max_tokens": self._max_tokens
        }
        
        response = requests.post(f"{self.base_url}/chat/completions", 
                               headers=headers, 
                               json=payload)
        response.raise_for_status()
        
        return response.json()["choices"][0]["message"]["content"]

    @property
    def type(self) -> str:
        return "deepseek"
deepseek_llm = DeepSeekLLM(llm_token)
# End of AI code

#Making the connection
client = MongoClient(uri)
if not client:
    raise ValueError('Could not connect to the database')

database = client[database_name]

if not database:
    raise ValueError(f"Database {database_name} not found")


collection = database[collection_name]

if not collection:
    raise ValueError(F"Collection {collection_name} not found")


collection_data = list(collection.find({}))

if len(collection_data) == 0:
    raise ValueError(f"No data found in {database_name}/{collection_data}")

df = pd.DataFrame(collection_data)


#  Dropping the _id property

if '_id' in df.columns:
    df = df.drop(columns=['_id'])


smart_df = SmartDataframe(df, config={
    "llm": deepseek_llm
})

response = smart_df.chat("What is the avarage value of amount")

print(response)