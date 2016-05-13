# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.conf import settings
import pymongo

class LagouPipeline(object):
    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbname = settings['MONGODB_NAME']
        clint = pymongo.MongoClient()  #本地可以不加东西也行
        tdb = clint[dbname]  #通过这种方式选择数据库名
        self.post = tdb[settings['MONGODB_TABLE']]


    def process_item(self, item, spider):
        bookinfo = dict(item)
        self.post.insert(bookinfo)
        return item
