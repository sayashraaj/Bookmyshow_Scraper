import scrapy
from ..items import BookmyshowItem

class spider(scrapy.Spider):
    name='bms'
#Reading urls.txt for obtaining URLs
    f = open("urls.txt")
    start_urls = [url.strip() for url in f.readlines()]
    f.close()

    def parse(self,response):
        a = response.css('div.wrapper li.list')
        items = BookmyshowItem()
#Crawling and storing output for each time the item is found
        for b in a:
            namecin = b.css('::attr(data-name)').extract()
            timin = b.css('a::attr(data-display-showtime)').extract()
            percentage = b.css('a::attr(data-seats-percent)').extract()
            date = b.css('a::attr(data-cut-off-date-time)').extract()
            sr = b.css('::attr(data-sub-region-name)').extract()
#Storing the data using items.py
            items['cinema'] = namecin
            items['subregion'] = sr
            items['timings'] = timin
            items['percentage'] = percentage
            items['date'] = int((int(date[0])/10000))

            yield items