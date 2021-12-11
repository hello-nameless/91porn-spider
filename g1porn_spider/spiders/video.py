import scrapy


class VideoSpider(scrapy.Spider):
    name = 'video'
    allowed_domains = ['91porn.com']
    start_urls = ['https://91porn.com/index.php/']

    def parse(self, response):
        pass
