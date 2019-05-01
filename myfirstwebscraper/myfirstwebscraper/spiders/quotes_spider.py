import scrapy

class QuotesScraper(scrapy.Spider):
    name = "quotes"
    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/'
            ]
        for url in urls:
            print(url)
            yield scrapy.Request(url=url,callback = self.parse)
    
    def parse(self, responce):
        page = responce.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(responce.body)
        self.log("saved file %s" % filename)