# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json, codecs
import pymongo

class QierPipeline(object):
    def __init__(self):
        self.file = codecs.open('qieranchor.csv', 'wb+', encoding='utf-8')  # 创建以utf-8编码的csv文件
        client = pymongo.MongoClient('localhost', 27017)  # 创建mongodb连接
        db = client['spiderData']  # 创建mongodb数据库
        self.collection = db['qieranchor']  # 创建数据库中collection

    def process_item(self, item, spider):
        item = dict(item)  # 将抓到的item转为dict格式
        line = json.dumps(item) + '\n'  # 定义line字段将抓到的item转为jump格式，加上空格换行
        self.file.write(line)  # 将line写进csv中输出 修改了decode（）
        self.collection.insert(item)  # 将item写进mongodb中
