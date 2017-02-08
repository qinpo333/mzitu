import scrapy, time, urllib, re, uuid
from scrapy.selector import Selector
from scrapy.contrib.loader import ItemLoader,Identity
from mzitu.items import MzituItem

class MzituSpider(scrapy.Spider):
    name = "mzitu"
    allowed_domains = ["mzitu.com"]
    start_urls = (
        "http://www.mzitu.com/page/8",
    )

    def parse(self, response):
        sel = Selector(response)

        page_urls = sel.xpath("//ul[@id='pins']/li/a/@href").extract()
        for page_url in page_urls:
            yield scrapy.Request(page_url, callback=self.parse)
            # yield request

        pages = sel.xpath("//div[@class='pagenavi']/a/span/text()").extract()
        # print(pages)
        if len(pages) > 2 :
            page_link = pages[-2]
            # page_link = page_link.replace('/a', '')
            # print page_link

            for i in range(1, int(page_link) + 1):
                print(response.url + '/%s' % i)
                yield scrapy.Request(response.url + '/%s' % i, callback=self.parse_item)
                # yield request

    def parse_item(self, response):

        # sel = Selector(response)
        #
        # name = sel.xpath("//div[@class='main-image']/p/a/img/@alt").extract()[0]
        # print(name)

        l = ItemLoader(item=MzituItem(), response=response)
        l.add_xpath('image_urls', "//div[@class='main-image']/p/a/img/@src", Identity())
        l.add_xpath('name', "//div[@class='main-image']/p/a/img/@alt", Identity())
        # l.add_value('name', name)

        return l.load_item()
