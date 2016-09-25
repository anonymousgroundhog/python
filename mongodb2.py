#!/usr/bin/env python
import warnings
warnings.simplefilter("ignore", UserWarning)

import pymongo

# Connection to Mongo DB----------------------------------------
try:
    conn=pymongo.MongoClient()
    print "\n\nConnected successfully!!!"
except pymongo.errors.ConnectionFailure, e:
   print "\n\nCould not connect to MongoDB: %s" % e 
conn

db = conn.mydb
#CREATE COLLECTION---------------------------
collection = db.my_collection
print "------------------------------------------------------------\n\n"
print "COLLECTION: ", collection

#INSERT DATA INTO COLLECTION
doc = {"name":"Alberto","surname":"Negron","twitter":"@Altons"}

collection.insert(doc)

doc = {"name":"Sean","surname":"Negron","twitter":"@Sean"}

collection.insert(doc)


#PRINT OUT DB NAMES
print "------------------------------------------------------------\n"
print "\n DB NAMES: ", conn.database_names()

print "\nPOSTS FIND ONE: ", collection.find_one({"name":"Alberto"})


#query and post content
#listcontent = collection.find("name")

print "--------------------------------------------------------------------\n"
cursor = collection.find()

print "DATA FROM TABLE IS:\n"
for name in cursor:
 print name

#EMPTY TABLE
result = collection.delete_many({})

print "\n DELETED CONTENTS: ", result.deleted_count
