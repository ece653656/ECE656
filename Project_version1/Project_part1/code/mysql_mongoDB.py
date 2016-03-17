import pymongo
import mysql.connector
import json
import timeit

def mysql_mongodb(cursor,db):
    bus=""
    
    query = 'select business_id, name from business where name="Emil\'s Lounge"'
    cursor.execute(query)
    for (business_id,name) in cursor:
        bus= business_id

    listTemp = db.checkin.find( {"business_id": bus } )
    for elem in listTemp:
        print(elem)
    return


## mysql
config = {
      'user': 'root',
      'password': '831022',
      'host': 'localhost',
      'database': 'ece656a1',
      'raise_on_warnings': True,
    }
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

## mongodb
from pymongo import MongoClient
client = MongoClient()
db = client.ECE656projtest

t1 = timeit.Timer(lambda:mysql_mongodb(cursor,db))
print t1.timeit(1)

## mysql
cursor.close()
cnx.close()
