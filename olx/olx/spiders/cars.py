import scrapy

class CarsSpider(scrapy.Spider):
    name = 'cars'
    allowed_domains = ['www.olx.co.id']
    start_urls = ['http://www.olx.co.id/mobil-bekas_c198/']

    rules = (Rule
    (LinkExtractor(allow=('mobil-bekas_c198/'), restrict_css=('.pageNextPrev',)),
    callback="parse_item",
    follow=True),
    )
            
    def parse_item(self, response):
        print('Processing..' + response.url)
