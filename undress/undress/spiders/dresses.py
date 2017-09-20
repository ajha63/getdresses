# -*- coding: utf-8 -*-
import scrapy
from undress.items import UndressItem

class QuotesSpider(scrapy.Spider):
	name = "dresses"

	allowed_domains = ['simons.ca']
	start_urls = ['https://www.simons.ca/en/women-clothing/dresses--6680']

	def parse(self, response):

		for item in response.xpath('//*[@class=$val]/div', val='product_card loaded'):
			