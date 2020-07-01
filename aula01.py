import scrapy

class MainSpider(scrapy.Spider):
    name = 'main-spider'
    start_urls = ['http://quotes.toscrape.com'] #Requerido pelo scrapy

    def parse(self, response):
        self.log('Estou aqui {}'.format(response.url))
        texts = response.xpath('//span[@class="text"]/text()').extract()

        for text in texts:
            yield {
                'text2': texts
            }