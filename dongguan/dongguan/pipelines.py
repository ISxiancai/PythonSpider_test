# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs

class DongguanPipeline(object):
    def __init__(self):
        self.filename = codecs.open('dongguan.json','wb',encoding='utf-8')
    def process_item(self, item, spider):
        text = json.dumps(dict(item),ensure_ascii=False)+',\n'
        self.filename.write(text)
        return item
