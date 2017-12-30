# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class QcPipeline(object):
    def process_item(self, item, spider):

        return item


class QianchenPipeline(object):
    def __init__(self):
        self.file = 'qianchen.txt'

    def process_item(self, item, spider):
        with open(self.file, "a")as f:
            f.write(json.dumps(item, ensure_ascii=False, indent=4))
            f.write("\n")
        return item

    def spider_closed(self, spider):
        self.file.close()
