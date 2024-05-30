from pymongo import MongoClient
from neo4j import GraphDatabase

class MongoDBPipeline:
    def open_spider(self, spider):
        self.client = MongoClient('mongo', 27017)
        self.db = self.client[spider.settings.get('MONGO_DATABASE')]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db.articles.insert_one(dict(item))
        return item

class Neo4jPipeline:
    def open_spider(self, spider):
        uri = spider.settings.get('NEO4J_URI')
        user = spider.settings.get('NEO4J_USER')
        password = spider.settings.get('NEO4J_PASSWORD')
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close_spider(self, spider):
        self.driver.close()

    def process_item(self, item, spider):
        with self.driver.session() as session:
            session.run(
                "CREATE (a:Article {title: $title, subtitle: $subtitle, date: $date, text: $text, images: $images, authors: $authors, video: $video})",
                title=item['title'],
                subtitle=item.get('subtitle', ''),
                date=item['date'],
                text=item['text'],
                images=item['images'],
                authors=item.get('authors', ''),
                video=item.get('video', '')
            )
        return item
    
