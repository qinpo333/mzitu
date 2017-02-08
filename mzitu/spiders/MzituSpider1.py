import scrapy, time, urllib, re, uuid
from scrapy.selector import Selector

class MzituSpider(scrapy.Spider):
    name = "mzitu1"
    allowed_domains = ["mzitu.com"]
    start_urls = (
        "http://www.mzitu.com/65682",
    )

    def parse(self, response):
        sel = Selector(response)

        pages = sel.xpath("//div[@class='pagenavi']/a/span/text()").extract()
        print(pages)
        if len(pages) > 2 :
            page_link = pages[-2]
            # page_link = page_link.replace('/a', '')
            print page_link

            for i in range(1, int(page_link) + 1):
                print i
                request = scrapy.Request('http://www.mzitu.com/65682/%s' % i, callback=self.parse_item)
                yield request

    def parse_item(self, response):
        sel = Selector(response)

        url = sel.xpath("//div[@class='main-image']/p/a/img/@src").extract()[0]
        print(url)
        name = url.split('/')[5]
        # print(url.split('/'))
        print name
        urllib.urlretrieve(url, "/Users/cmcc/Pictures/sugar/" + name)