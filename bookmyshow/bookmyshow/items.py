# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookmyshowItem(scrapy.Item):
    cinema = scrapy.Field()
    subregion = scrapy.Field()
    timings = scrapy.Field()
    percentage = scrapy.Field()
    date = scrapy.Field()