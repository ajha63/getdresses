# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UndressItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # brand_name = scrapy.Field()
    # product_name = scrapy.Field()
    # short_description = scrapy.Field()
    # price_regular = scrapy.Field()
    # combi_value1  = scrapy.Field()
    url_img_product = scrapy.Field()
    url_product = scrapy.Field()
