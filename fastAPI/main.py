# project-root/fastapi/main.py
from fastapi import FastAPI
from pymongo import MongoClient
from neo4j import GraphDatabase
import os

app = FastAPI()

# MongoDB connection
mongo_client = MongoClient(os.getenv('MONGO_URL', 'mongodb://mongo_container:27017'))
mongo_db = mongo_client["scrapy_db"]

# Neo4j connection
neo4j_driver = GraphDatabase.driver(
    os.getenv('NEO4J_URL', 'bolt://neo4j_container:7687'),
    auth=("neo4j", "password")
)

@app.get("/mongo_data")
def get_mongo_data():
    data = mongo_db["scrapy_collection"].find()
    return list(data)

@app.get("/neo4j_data")
def get_neo4j_data():
    with neo4j_driver.session() as session:
        result = session.run()
        return [record for record in result]
