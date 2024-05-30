import scrapy

class BbcNewsItem(scrapy.Item):
    menu = scrapy.Field()
    submenu = scrapy.Field()
    topic = scrapy.Field()
    title = scrapy.Field()
    subtitle = scrapy.Field()
    text = scrapy.Field()
    date = scrapy.Field()
    images = scrapy.Field()
    authors = scrapy.Field()
    video = scrapy.Field()
