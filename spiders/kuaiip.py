# -*- coding: utf-8 -*-
import scrapy
from kuaidaili.items import KuaidailiItem

class KuaiipSpider(scrapy.Spider):
    name = 'kuaiip'
    allowed_domains = ['kuaidaili.com']
    start_urls = ['http://www.kuaidaili.com/free/']
    for i in range(1,3):
    	start_urls.append('http://www.kuaidaili.com/free/inha/%d/' % i)

    def parse(self, response):
        results = response.xpath('//div[@class="con-body"]//tbody//tr')
        #print(results)
        for td in results:
        	data = td.xpath('./td/text()').extract()
        	#print(data)
        	item = KuaidailiItem()
        	item['ip'] = data[0]
        	item['port'] = data[1]
        	item['area'] = data[4]
        	item['types'] = data[2].strip('名')
        	yield item
