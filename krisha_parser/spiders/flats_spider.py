import scrapy

class FlatsSpider(scrapy.Spider):
    name = "flats"
    start_urls = [
        "https://krisha.kz/prodazha/kvartiry/karaganda/"
    ]

    def parse(self, response):
        for flat in response.css("div.a-card__header"):
            yield {
                "header": flat.css("a.a-card__title::text").get(),
                "price": flat.css("div.a-card__price::text").get(),
                "subtitle": flat.css("div.a-card__subtitle::text").get()
            }