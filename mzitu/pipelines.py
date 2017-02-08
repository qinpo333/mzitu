# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os,urllib

class MzituPipeline(object):
    def process_item(self, item, spider):
        if 'image_urls' in item:
            images = []
            dir_path = '/Users/cmcc/Pictures/'

            for image_url in item['image_urls']:
                file_path = '%s/%s' % (dir_path, item['name'][0])
                print(item['name'][0].encode('utf-8'))
                if os.path.exists(file_path):
                    urllib.urlretrieve(image_url, file_path + '/' + image_url.split('/')[5])
                else:
                    os.makedirs(file_path)

        return item
