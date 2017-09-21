# -*- coding: utf-8 -*-
import scrapy
from undress.items import UndressItem

class QuotesSpider(scrapy.Spider):
	name = "dresses"
	start_urls = [
		'https://www.simons.ca/en/women-clothing/dresses--6680',
	]
	def parse(self, response):
		for item in response.css('div.product_card'):
			url_prod = item.css('a').xpath('@href').extract_first()
			url_img_prod = item.css('a').xpath('@href').extract_first()
			yield scrapy.Request(path, callback = self.parse_dress)
			#yield UndressItem(
			#	url_img_product = item.css('img').xpath('@src').extract(),
			#	url_product = item.css('a').xpath('@href').extract_first()
			#)

		strpath = '//*[@id="footer_filter"]/div/div[2]/span[3]/a/@href'
		next_page = response.xpath(strpath).extract_first()
		if next_page:
			yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

	def parse_dress(self, response):
		idItem = 

