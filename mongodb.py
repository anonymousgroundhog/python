#!/usr/bin/env python
import warnings
warnings.simplefilter("ignore", UserWarning)

def get_db():

    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.myFirstMB
    return db

def add_country(db):
    db.countries.insert({"name" : "Canada"})
    db.countries.insert({"name" : "United States"})
    
def get_country(db):
	return db.countries.find_one() 

def get_country_list(db):
   return db.countries.find({"name": "United States"})

if __name__ == "__main__":

    db = get_db() 
    add_country(db)
    print get_country(db)
    print get_country_list(db)



