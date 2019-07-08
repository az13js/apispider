# -*- coding: UTF-8 -*-
import json
import random
import scrapy
import csv

class ApispiderSpider(scrapy.Spider):
    name = 'apispider'

    def start_requests(self):
        url = 'http://www.szse.cn/api/market/ssjjhq/getTimeData?marketId=1'
        with open('codes.csv') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                yield scrapy.Request(url = url + '&random=' + str(random.randint(1,50)) + '&code=' + row[0], callback = self.parse)

    def parse(self, response):
        data = json.loads(response.body)
        if '0' == data['code']:
            yield {
                'datetime': data['datetime'],
                'code': data['data']['code'],
                'name': data['data']['name'],
                'price': data['data']['now']
            }
