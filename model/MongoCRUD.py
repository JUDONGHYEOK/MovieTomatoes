# MongoDB Access and CRUD test

from pymongo import MongoClient

# conda install -c anaconda pymongo

# 1. MongoDB Connection

# 'localhost' == 127.0.0.1 == 192.168.0.5(Real)
client = MongoClient('localhost',27017)
db = client['local']
collection = db.get_collection('test')

data = {'name':'cherry','age':8}
collection.insert_one(data)

# MongoDB > database > collection > document
# 우리은행 > 우리은행 광주지점 > 예금 > 50,000 입금: 최철웅

# CRUD => Create, Read, Update, Delete

