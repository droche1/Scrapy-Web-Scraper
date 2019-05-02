# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Join, MapCompose, SelectJmes
from testjsonscraper.items import TestjsonscraperItem

class TestjsonSpider(scrapy.Spider):
    name = 'testjson'
    allowed_domains = ['jsonplaceholder.typicode.com/users']
    start_urls = ['http://jsonplaceholder.typicode.com/users/']
# dictionary to map Item fields to Jmes query paths
    jmes_paths = {
        'user_id': 'id',
        'name': 'name',
        'email': 'email',
        'address': 'address.["zipcode", "city", "street", "suite"]',
        'phone': 'phone',
        'company': 'company.name',
    }
    def parse(self, response):
        """Main parse method."""
        jsonresponse = json.loads(response.body_as_unicode())
 
        for user in jsonresponse:
 
            loader = ItemLoader(item=TestjsonscraperItem())  # create an ItemLoader to populate a UserItem
            loader.default_input_processor = MapCompose(str)  # apply str conversion on each value
            loader.default_output_processor = Join(' ')
 
            for (field, path) in self.jmes_paths.items():
                loader.add_value(field, SelectJmes(path)(user))
 
            yield loader.load_item()
