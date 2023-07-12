# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapinternshipPipeline:
    def process_item(self, item, spider):
        text = ""
        for content in item["content"]:
            text += " "+content
        with open(f"C:/Users/hp/MLprojects/Data/internship_files/Scrapped_data/url_id-{item['url_id']}.txt", 'w', encoding="utf-8") as f:
            f.write(item['title'][0])
            f.write(text)
        return item
