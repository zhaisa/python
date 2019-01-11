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
collection1 = db.report_trans
#查找集合中所有数据
# for item in collection.find({'transfer_id':{"$regex":"^3_0_"} }):
#    print(item["transfer_id"].replace("3_0_",""))
#data=db.collect_name.find({"transfer_id" : "3_0_19329"})
#print(data)
list2=[]
sum1=0
sum2=0
for item in collection.find({"source_target_code" : "YCWY1806-90-057"}):
    list1=item["transfer_amount"]
    list2.append(float(list1))

for ab in list2:
    sum1+=ab
print(sum1)
list4=[]
for item1 in collection1.find({"source_target_code" : "YCWY1806-90-057","trans_type_dec" : "承接"}):
    list3=item1["trans_money"]
    list4.append(float(list3))
for cd in list4:
    sum2+=cd
print(sum2)