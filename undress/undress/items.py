# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UndressItem(scrapy.Item):
    # define the fields for your item here like:
    url_img_product = scrapy.Field()
    id_item = scrapy.Field()
    product_url = scrapy.Field()
    product_name = scrapy.Field()
    short_description = scrapy.Field()
    description = scrapy.Field()
    tags = scrapy.Field()
    price_regular = scrapy.Field()
    reduction_type = scrapy.Field()
    reduction = scrapy.Field()
    sale_price = scrapy.Field()
    meta_title = scrapy.Field()
    meta_keyword = scrapy.Field()
    meta_description = scrapy.Field()
    caegory_id = scrapy.Field()
    sub_cat = scrapy.Field()
    brand_name = scrapy.Field()
    cover_image_url = scrapy.Field()
    cover_image_caption = scrapy.Field()
    supplier_name = scrapy.Field()
    combi_name1 = scrapy.Field()
    combi_value1 = scrapy.Field()
    combi_name2 = scrapy.Field()
    combi_value2 = scrapy.Field()
    combi_image_url = scrapy.Field()
    combi_price = scrapy.Field()