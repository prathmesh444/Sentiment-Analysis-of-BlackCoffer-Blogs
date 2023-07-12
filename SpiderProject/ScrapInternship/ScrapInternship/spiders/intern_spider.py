import scrapy
import pandas as pd

df = pd.read_excel("C:/Users/hp/MLprojects/Data/Input_urls.xlsx")
mapping = dict(zip(list(df.URL), list(df.URL_ID)))
class InternSpider(scrapy.Spider):
    name = "blog"
    start_urls = list(df.URL)

    def parse(self, response, **kwargs):
        url_id = mapping[response.url]

        content_query = "//div[@class='td-pb-span8 td-main-content']/div[@class='td-ss-main-content']/div[@class='td-post-content tagdiv-type']"
        title_query = "title::text"
        contents = response.xpath(content_query).css("p::text").extract()
        if(len(contents) == 0):
            content_query =  "//div[@class='tdb-block-inner td-fix-index']"
            contents = response.xpath(content_query).css("p::text").extract()
        contents += response.xpath(content_query).css("li::text").extract()
        contents += response.xpath(content_query).css("td::text").extract()
        contents += response.xpath(content_query).css("span::text").extract()
        contents += response.xpath("//div[@class='tdb-block-inner td-fix-index']/p/text()").extract()
        titles = response.css(title_query).extract()
        # for i in range(len(titles)):
        #     text = ""
        #     for content in contents:
        #         text += " "+content
        #     with open(f"C:/Users/hp/url_id-{url_id[i]}.txt", 'w') as f:
        #         f.writelines(titles[i])
        #         f.write(text)
        #

        yield {"url_id": url_id, "title": titles, "content": contents}