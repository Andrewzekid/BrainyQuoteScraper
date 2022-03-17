import scrapy


class BrainyquoteSpider(scrapy.Spider):
    name = 'BrainyQuote'
    allowed_domains = ['www.brainyquote.com/topics/valentines-day-quotes']
    start_urls = ['https://www.brainyquote.com/topics/valentines-day-quotes/']

    def parse(self, response):

        #select the element that has the class: "grid-item qb clearfix bqQt" and store it in a variable named "quoteblocks"
        quoteblocks = response.css(".grid-item.qb.clearfix.bqQt")
        for quoteblock in quoteblocks:
            item = {}
            #scrape the quote text
            quote = quoteblock.xpath(".//a/div/text()").get()
                  
            #scrape the author name
            author = quoteblock.xpath(".//a[@title='view author']/text()").get()

            item["quote"] = quote
            item["author"] = author

            yield item

