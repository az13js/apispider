# -*- coding: UTF-8 -*-
import json
import random
import scrapy

class ApispiderSpider(scrapy.Spider):
    name = 'apispider'

    def start_requests(self):
        # 股票代码列表
        codes = ['000788', '000008']
        url = 'http://www.szse.cn/api/market/ssjjhq/getTimeData?marketId=1'
        for code in codes:
            self.log('Request:' + code)
            yield scrapy.Request(url = url + '&random=' + str(random.randint(1,50)) + '&code=' + code, callback = self.parse)

    def parse(self, response):
        data = json.loads(response.body)
        if '0' == data['code']:
            yield {
                'datetime': data['datetime'],
                'code': data['data']['code'],
                'name': data['data']['name'],
                'price': data['data']['now']
            }
