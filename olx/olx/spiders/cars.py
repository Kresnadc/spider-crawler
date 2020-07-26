import scrapy

# Created by Kresna Dwi
# Class that inherit scrapy Spider
class CarsSpider(scrapy.Spider):
    name = "cars"

    # urls to be crawl
    def start_requests(self):
        urls = [
            'https://www.olx.co.id/mobil-bekas_c198?page=1',
        ]

        # loop each urls to be parsed
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # parse response into structured result
    def parse(self, response):
        # this item refer to item list in olx product page
        for item in response.xpath('//li[@data-aut-id="itemBox"]'):
            # collect field every product item
            yield{
                'product_name': item.xpath('.//span[@data-aut-id="itemTitle"]/text()').extract_first(),
                'year': item.xpath('.//span[@data-aut-id="itemDetails"]/text()').extract_first(),
                'price': item.xpath('.//span[@data-aut-id="itemPrice"]/text()').extract_first(),
                'location': item.xpath('.//span[@data-aut-id="item-location"]/text()').extract_first(),
            }        
