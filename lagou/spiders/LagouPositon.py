# -*- coding: utf-8 -*-
import scrapy
import json
from lagou.items import LagouItem
#from scrapy_redis.spiders import RedisSpider

class LagoupositonSpider(scrapy.Spider):
    name = "LagouPositon"
    #allowed_domains = ["lagou.com/zhaopin/"]
    # start_urls = (
    #     'http://www.lagou.com/jobs/positionAjax.json?gj=%E5%BA%94%E5%B1%8A%E6%AF%95%E4%B8%9A%E7%94%9F&xl=%E5%A4%A7%E4%B8%93&jd=%E6%88%90%E9%95%BF%E5%9E%8B&hy=%E7%A7%BB%E5%8A%A8%E4%BA%92%E8%81%94%E7%BD%91&px=new&city=%E4%B8%8A%E6%B5%B7',
    # )
    totalPageCount = 0
    curpage = 1
    myurl = 'http://www.lagou.com/jobs/positionAjax.json?px=new'
    city = u'北京'
    kd = u'大数据'
    def start_requests(self):
        return [scrapy.http.FormRequest(self.myurl,
                                        formdata={'pn':str(self.curpage),'kd':self.kd},callback=self.parse)]

    def parse(self, response):
        # fp = open('1.html','w')
        # fp.write(response.body)
        item = LagouItem()
        jdict = json.loads(response.body)
        jcontent = jdict["content"]
        jposresult = jcontent["positionResult"]
        jresult = jposresult["result"]
        self.totalPageCount = jposresult['totalCount'] /15 + 1;
        # if self.totalPageCount > 30:
        #     self.totalPageCount = 30;
        for each in jresult:
            item['city']=each['city']
            item['companyName'] = each['companyName']
            item['companySize'] = each['companySize']
            item['positionName'] = each['positionName']
            item['positionType'] = each['positionType']
            sal = each['salary']
            sal = sal.split('-')
            print sal
            if len(sal) == 1:
                item['salaryMax'] = int(sal[0][:sal[0].find('k')])
            else:
                item['salaryMax'] = int(sal[1][:sal[1].find('k')])
            item['salaryMin'] = int(sal[0][:sal[0].find('k')])
            item['positionAdvantage'] = each['positionAdvantage']
            item['companyLabelList'] = each['companyLabelList']
            yield item
        if self.curpage <= self.totalPageCount:
            self.curpage += 1
            yield scrapy.http.FormRequest(self.myurl,
                                        formdata={'pn':str(self.curpage),'kd':self.kd},callback=self.parse)
