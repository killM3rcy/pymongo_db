from pymongo import MongoClient
import sys
import pprint
from pymongo import errors


# create a variable client to connect to database
client = MongoClient()



lst[] = input("Enter database name")

#create a database
try:
	db = client.db_name
except pymongo.errors.AutoReconnect(msg = "Reconnecting to database..."):
	print(msg)


#create a collection
try:
	col = db.student_information
except pymongo.errors.AutoReconnect(msg = "Reconnecting to database..."):
	print(msg)

