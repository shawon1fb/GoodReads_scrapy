import scrapy


class GoodReads(scrapy.Spider):
    name = "goodreads"

    def start_requests(self):
        urls = [
            'https://www.goodreads.com/quotes',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.xpath("//div[@class='quote']"):
            yield {
                'Text': quote.xpath(".//div[@class='quoteText']/text()[1]").extract_first(),
                'Author': quote.xpath(".//div[@class='quoteText']/child::span/text()").extract_first(),
                'Tag': quote.xpath(".//div[@class='greyText smallText left']/a/text()").extract(),
            }
