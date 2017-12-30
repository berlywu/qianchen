# -*- coding: utf-8 -*-
import scrapy


class JobSpider(scrapy.Spider):
    name = 'job'
    allowed_domains = ['51job.com']
    start_urls = ['http://search.51job.com/list/020000,000000,0000,00,9,99,Python 爬虫,2,1.html?lang=c']

    # 获取所有关于爬虫的招聘信息
    def parse(self, response):
        # print(response.body.decode('gbk'))
        div_list = response.xpath('//div[@class="dw_table"]/div[@class="el"]')
        print(len(div_list))
        for div in div_list:
            item = {}
            # 职位
            item['postion'] = div.xpath("./p/span/a/text()").extract_first().strip()
            # 详请链接
            item['detail_link'] = div.xpath("./p/span/a/@href").extract_first().strip()
            # 公司名字
            item['company'] = div.xpath("./span[@class='t2']/a/@title").extract_first().strip()
            # 公司详请链接
            item['company_link'] = div.xpath("./span[@class='t2']/a/@href").extract_first().strip()
            # 位置
            item['addr'] = div.xpath("./span[@class='t3']/text()").extract_first().strip()
            # 工资
            item['wages'] = div.xpath("./span[@class='t4']/text()").extract_first()
            # 发布时间
            item['publish_time'] = div.xpath("./span[@class='t5']/text()").extract_first().strip()
            print(item)

            yield scrapy.Request(
                item['detail_link'],
                callback=self.parse_detail,
                meta={"item":item}
            )


        # 翻页
        print('*'* 100)
        next_url = response.xpath("//div[@class='p_in']/ul/li[last()]/a/@href").extract_first()
        print(next_url)
        print('*'*100)
        if next_url is not None:
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )




    def parse_detail(self, response):
        item = response.meta['item']
        # 公司详请
        item['company_detail'] = response.xpath("//div/p[@class='msg ltype']/text()").extract_first().strip()
        # 职位要求
        item['postion_request'] = response.xpath("//div[@class='t1']/span/text()").extract()
        # 公司福利
        item['company_weal'] = response.xpath("//p[@class='t2']/span/text()").extract()
        # 职位信息及要求
        item['postion_info'] = response.xpath("//div[@class='bmsg job_msg inbox']/text()").extract()
        # 公司详细地址
        item['detail_addr'] = response.xpath("//div[@class='bmsg inbox']/p[1]/text()").extract_first()
        # 公司信息
        item['company_info'] = response.xpath("//div[@class='tmsg inbox']/text()").extract()
        yield item