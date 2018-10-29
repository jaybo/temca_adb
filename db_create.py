
from __future__ import print_function    
from __future__ import division  


from pymongo import MongoClient
from utils.tile_qc_meta import process

client = MongoClient('localhost', 27017)
db = client.Z100

class Bunch(object):
    ''' http://code.activestate.com/recipes/52308-the-simple-but-handy-collector-of-a-bunch-of-named/?in=user-97991'''
    def __init__(self, **kwds):
        self.__dict__.update(kwds)

args = Bunch(
    directory = r"C:\data\TEMCA1\001925\0", 
    image_directory = None,
    config_file = r"c:\temca\temca1\config\TEMCA_cfg.yml",
    results_file = None,
    visualization = 0)

output = process(args)

tar = db.tar
tar.remove({}) # empty it

for j in range(25000):
    output['_id'] = j
    output['metadata']['grid'] = str(j)
    result = tar.insert_one(output)
    print('added: {0}'.format(result.inserted_id))

# data = db.tar.find_one({'tile_qc.failed' : False}, {'_id': 1})
data = db.tar.find_one({'metadata.grid' : {'$eq': '5'}})
print (len(data))
