import scrapy


class PbcCastSpider(scrapy.Spider):
    name = 'pbc_cast'

    # allowed_domains = ['www.pbc.gov.cn']
    # start_urls = ['http://www.pbc.gov.cn/']

    # def start_requests(self):
    #     urls = ["http://www.pbc.gov.cn/goutongjiaoliu/113456/113469/11040/index1.html","http://www.pbc.gov.cn/goutongjiaoliu/113456/113469/11040/index6.html"]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)
    #
    # # 对返回页面进行解析等步骤
    # def parse(self, response):
    #     fname = response.url.split("/")[-1]
    #     with open(fname, "wb") as f:
    #         f.write(response.body)
    #         self.log("Saved file %s." % fname)
    def start_requests(self):
        urls = ["http://www.pbc.gov.cn/goutongjiaoliu/113456/113469/11040/index2.html",
                "http://www.pbc.gov.cn/goutongjiaoliu/113456/113469/11040/index7.html"]
        for url in urls:
            yield scrapy.Request(url=url, method='POST', callback=self.nparse)

    # 对返回页面进行解析等步骤
    def nparse(self, response):
        fname = response.url.split("/")[-1]
        with open(fname, "wb") as f:
            f.write(response.body)
            self.log("Saved file %s." % fname)

if __name__ == '__main__':
    from scrapy import cmdline
    cmdline.execute(f'scrapy crawl {PbcCastSpider.name}'.split())
