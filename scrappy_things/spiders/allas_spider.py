import scrapy


class AllAsSpider(scrapy.Spider):

  name="allas"

  # def __init__(self):
  #   pass

  async def start(self):
    # Get the argument to extract the URL
    print("\n### Starting the spider ###\n")
    self.start_urls = [self.root]
    yield scrapy.Request(url=self.root, callback=self.parse)


  # Gather all links within an element
  async def collect(self, response):
    for anchor in response.css('a'):
      yield {
        "href": anchor.attrib['href'],
      }

  async def parse(self, response):
    # Extract the anchors of the page
    async for item in self.collect(response):
      yield item