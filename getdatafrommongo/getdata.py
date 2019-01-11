from pymongo import MongoClient
import datetime
#client = MongoClient()
#uri = 'mongodb://' + user + ':' + pwd + '@' + server + ':' + port +'/'+ db_name
uri='mongodb://'+'prod_rbv2_dw_co_read'+':'+'QaJQp7QEZQnd6xelygmY'+'@' + 'dds-bp10b5bfb79d7c441.mongodb.rds.aliyuncs.com' + ':' + '3717' +'/'+ 'prod_rongbei_v2_dw_collect'
client = MongoClient(uri)
#连接所需数据库,test为数据库名
#db=client.test
db = client.prod_rongbei_v2_dw_collect
#连接所用集合，也就是我们通常所说的表，test为表名
#collection=db.test
collection = db.report_transfer_info
#查找集合中所有数据
#for item in collection.find({'transfer_id':{"$regex":"^3_0_"} }):
#    print(item["transfer_id"].replace("3_0_",""))
#data=db.collect_name.find({"transfer_id" : "3_0_19329"})
#print(data)
begintime=datetime.datetime
print(begintime)
aa=collection.find().count()
endtime=datetime.datetime
bb=collection.find().count()
