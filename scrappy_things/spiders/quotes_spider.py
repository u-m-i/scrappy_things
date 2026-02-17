import scrapy

class QuotesSpider(scrapy.Spider):
  name="quotes"

  async def start(self):
    print("\n### Starting the quotes ###\n")

    yield scrapy.Request(url="https://quotes.toscrape.com/page/1", callback=self.parse)
  
  async def parse(self, response):
    for quote in response.css('div.quote'):
      yield {
        "text": quote.css('span.text::text').get(),
      }


