
from __future__ import print_function    
from __future__ import division  


import pymongo
from utils.tile_qc_meta import process

client = pymongo.MongoClient('localhost', 27017)
db = client.Z100

data = {}
# db.tar.create_index([('metadata.grid', pymongo.ASCENDING)])
# data = db.tar.find_one({'tile_qc.failed' : False}, {'_id': 1})
data = db.tar.find_one({'metadata.grid' : {'$eq': '5000'}})
#data = db.tar.find({'metadata.grid' : '5000'}).explain("executionStats")
print (data)
