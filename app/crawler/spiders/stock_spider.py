import scrapy
from scraper.items import StockItem


class StockSpider(scrapy.Spider):
    name = "stock"
    allowed_domains = ['finance.yahoo.com']

    def start_requests(self):
        urls = [
            'https://finance.yahoo.com/quote/GOOG/summary?p=GOOG',
            'https://finance.yahoo.com/quote/AAPL/summary?p=AAPL',
            'https://finance.yahoo.com/quote/FB/summary?p=FB',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for title in response.xpath('//h1/text()').extract():
            yield StockItem(title=title)
        for price in response.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/span/text()').extract():
            yield StockItem(price=price)
