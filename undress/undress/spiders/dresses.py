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
			request = scrapy.Request(url_prod, callback = self.parse_dress)
			request.meta['urlimgprod'] = '{:s}'.format(url_img_prod)
			yield request

		strpath = '//*[@id="footer_filter"]/div/div[2]/span[3]/a/@href'
		next_page = response.xpath(strpath).extract_first()
		if next_page:
			yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

	def parse_dress(self, response):
		idItem = response.xpath('//*[@id="product_right"]/div[2]/div[1]/span/span/text()').extract_first()
		prodName = response.xpath('//*[@id="product_right"]/div[1]/div[2]/span/text()').extract_first()
		prodDescription = response.xpath('normalize-space(//*[@id="product_right"]/div[2]/div[1]/div/span)').extract()
		metaTitle = response.xpath('//title/text()').extract_first()
		metaDescription = response.xpath('normalize-space(/html/head/meta[1]/@content)').extract_first()
		brandName = response.xpath('//*[@id="product_right"]/div[1]/div[1]/div/span/text()').extract_first()
		try:
			priceRegular = response.xpath('//*[@id="product_right"]/div[1]/span/span[1]/text()').extract()[0].strip()
		except:
			priceRegular = ""

		try:
			salePrice = response.xpath('//*[@id="product_right"]/div[1]/span/span/text()').extract()[1].strip()
		except:
			salePrice = ""

		yield UndressItem(
			id_item = '{:s}'.format(idItem),
			product_url = '{:s}'.format(response.url),
			product_name = '{:s}'.format(prodName),
			short_description = '{:s}'.format(prodName),
			description = '{0}'.format(prodDescription),
			price_regular = '{:s}'.format(priceRegular),
			reduction_type = '{:s}'.format('amount'),
			sale_price = '{:s}'.format(salePrice),
			meta_title = '{:s}'.format(metaTitle),
			meta_keyword = '{:s}'.format('Not keywords'),
			meta_description = '{:s}'.format(metaDescription),
			category_id = '{:d}'.format(3),
			sub_cat = '{:s}'.format('8,10'),
			brand_name = '{:s}'.format(brandName),
			cover_image_url = response.meta['urlimgprod']
		)

