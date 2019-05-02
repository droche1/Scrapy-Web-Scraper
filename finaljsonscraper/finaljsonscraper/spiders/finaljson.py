# -*- coding: utf-8 -*-
import scrapy
import json

class FinaljsonSpider(scrapy.Spider):
    name = 'finaljson'
    allowed_domains = ['https://petition.parliament.uk/petitions/241584.json']
    start_urls = ['http://https://petition.parliament.uk/petitions/241584.json/']

    allowed_domains = ['petition.parliament.uk']
    start_urls = ['https://petition.parliament.uk/petitions/241584.json']

    def parse(self, response):
        details = {}
        results = json.loads(response.body)
        details["signatures_by_constituency"] = results["data"]["attributes"]["signatures_by_constituency"]
         
        return details