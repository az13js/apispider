# -*- coding: UTF-8 -*-
import json
import random
import scrapy

class ApispiderSpider(scrapy.Spider):
    name = 'apispider'

    def start_requests(self):
        # 测试，先写死，请求2次看看
        url = 'http://www.szse.cn/api/market/ssjjhq/getTimeData?marketId=1&code=000008'
        for i in range(2):
            yield scrapy.Request(url = url + '&random=' + str(random.randint(1,50)), callback = self.parse)

    def parse(self, response):
        data = json.loads(response.body)
        if '0' == data['code']:
            self.log('price:' + data['data']['now'])
            yield {
                'datetime': data['datetime'],
                'code': data['data']['code'],
                'name': data['data']['name'],
                'price': data['data']['now']
            }
