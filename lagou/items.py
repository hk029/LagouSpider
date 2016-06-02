# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    city = scrapy.Field()
    companyName = scrapy.Field()
    companySize = scrapy.Field()
    positionName = scrapy.Field()
    salaryMax = scrapy.Field()
    salaryMin = scrapy.Field()
    salaryAvg = scrapy.Field()
    positionType = scrapy.Field()
    positionAdvantage = scrapy.Field()
    companyLabelList = scrapy.Field()
    keyword = scrapy.Field()

