import os

# Scrapy settings for myspider project
SPIDER_MODULES = ['myspider.spiders']
NEWSPIDER_MODULE = 'myspider.spiders'

ITEM_PIPELINES = {
    'myspider.pipelines.MongoDBPipeline': 300,
    'myspider.pipelines.Neo4jPipeline': 400,
}

MONGO_URI = 'mongodb://mongo:27017'
MONGO_DATABASE = 'bbc_news'

NEO4J_URI = 'bolt://neo4j:7687'
NEO4J_USERNAME = 'neo4j'
NEO4J_PASSWORD = 'password'