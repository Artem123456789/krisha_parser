import scrapy

class FlatsSpider(scrapy.Spider):
    name = "flats"
    start_urls = [
        "https://krisha.kz/prodazha/kvartiry/karaganda/"
    ]