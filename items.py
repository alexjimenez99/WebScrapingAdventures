# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TemplateSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    low_temp     = scrapy.Field()
    high_temp    = scrapy.Field()
    day_of_month = scrapy.Field()
    # item_3 = scrapy.Field()
    # item_4 = scrapy.Field()
    
    
