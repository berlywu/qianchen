# -*- coding: utf-8 -*-
import scrapy


class QcSpiderSpider(scrapy.Spider):
    name = 'qc_spider'
    allowed_domains = ['51job.com']
    start_urls = ['http://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?']

    def parse(self, response):
        div_list = response.xpath("//div[@class='dw_table']/div[@class='el']")
        for div in div_list:
            item = {}
            # 职位
            item['postion'] = div.xpath("./p/span/a/@title")[0]
            item['company_name'] = div.xpath("./span[@class='t2']/a/@title")[0]
            item['work_addr'] = div.xpath("./span[@class='t3']/text()")[0]
            print(item)



