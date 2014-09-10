# -*- coding: utf-8 -*-
from __future__ import print_function
import time
import opensearch

key = ''
secret = ''
index_name = ''
table_name = ''

client = opensearch.SearchClient(key, secret)

index = opensearch.SearchIndex(index_name, client)
print('app list:', index.index())

doc = opensearch.SearchDoc(index_name, client)

items = [
    {
        "id": "12113313177",
        "title": "A test title 1",
        "content": "搜索， 内容",
    },
    {
        "id": "12113933131",
        "title": "A test Title 2",
        "content": "搜索， 内容2"
    }
]
item = items[0]
doc.add(item, table_name)  # add one doc
doc.add(items, table_name)  # add more than one docs

# time.sleep(4) # wait commit
print('doc detail:', doc.detail('12113313177', table_name))  # show doc detail

print('search result:', doc.search('query=搜索'))  # search on default field

doc.delete('12113933131', table_name)  # delete one doc
# delete more than one docs
doc.delete(['12113933131', '12113313177'], table_name)
