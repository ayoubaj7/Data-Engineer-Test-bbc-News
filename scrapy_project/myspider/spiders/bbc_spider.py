import scrapy
from scrapy.loader import ItemLoader
from myspider.items import BbcNewsItem  

class BBCSpider(scrapy.Spider):
    name = 'bbc'
    allowed_domains = ['bbc.com']
    start_urls = ['https://www.bbc.com/news/business']

    def parse(self, response):
        # Extract main menus
        main_menus = response.css('').getall()
        for menu in main_menus:
            yield response.follow(menu, self.parse_article)

    def parse_article(self, response):
        loader = ItemLoader(item=BbcNewsItem(), response=response)
        
        loader.add_css('menu', '')
        loader.add_css('submenu', '')
        loader.add_css('topic', '')
        loader.add_css('title', '')
        loader.add_css('subtitle', '')
        loader.add_css('text', '')
        loader.add_css('date', '')
        loader.add_css('images', '')
        loader.add_css('authors', '')
        loader.add_css('video', '')
        
        yield loader.load_item()
