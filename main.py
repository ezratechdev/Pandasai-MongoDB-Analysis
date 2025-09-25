import os
from dotenv import load_dotenv
import pandas as pd
from pymongo import MongoClient

# Load environment varibles from .env
load_dotenv()

# Connection is made from the uri connection string
uri = os.getenv('mongo_string')
database_name = os.getenv('database')
collection_name = os.getenv('collection')
llm_base = os.getenv("api_base")
llm_token = os.getenv("api_token")
llm_model = os.getenv("model")

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
