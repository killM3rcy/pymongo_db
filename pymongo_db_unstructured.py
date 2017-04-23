from pymongo import MongoClient
import sys
import pprint
from pymongo import errors


# create a variable client to connect to database
client = MongoClient()


#create a database
try:
	db = client.student
except pymongo.errors.AutoReconnect(msg = "Reconnecting to database..."):
	print(msg)


#create a collection
try:
	col = db.student_information
except pymongo.errors.AutoReconnect(msg = "Reconnecting to database..."):
	print(msg)

	
choice = {1: "insert_data", 2: "display_all_documents" , 3:"find_document" ,4: "update document",5: "delete_document" }

print("enter choice")
for i in choice:
	print(i ,':' +choice[i])

num = input()
num = int(num)


args = { }
#  ALL DEFINED FUNCTIONS


#								***********INSEET***********


def insert_document():
	"""db.student_information.insert_one({"name" : args[0], "age" : args[1],
	"course" : args[2], "email" : args[3], "Date of Birth" : args[4]})"""
	print("Enter data to be inserted :")
	print("Format key:val")

	doc = {}
	n = int(input("Enter no of keys in document to be inserted"))
	for i in range(n):
		key, val = input().split(':')
	
		doc[key] = val		

	col.insert_one(doc)


#							*************FIND****************

#	FIND A DOCUMENT	

def find_document():


	key, val = input("Enter in key:val format").split(':')
	find_doc = {key:val}
	
	cursor = col.find(find_doc,{'_id':0})
	
			

	if (cursor == "") :
		print("No documents found")
		return
	i = 1
	select = []
	for doc in cursor:
		print(i, doc)
		select.append(doc)
		i +=1
		#print(select)

	# if update document		
	if (num == 4):
	
		global update
		update = [key,val]
		update_document(select,update)
		# DONT USE UPDATE, USE TUPLE [INT] TO PASS TO UPDATE PARAMATERS
 	
	if (num == 5):
	
		global update
		update = {key:val}
		print("Do you want to delete the foll deocument\ty/n?")
		cnf = input()
		if (cnf == 'y' or cnf == 'Y'):
	
			delete_document(update)
		else:
			pass


#						***************UPDATE************

# update document
def update_document(select,update):
	print(update)
	cnt = 1
	for i in select:
		print(cnt,i)
		cnt +=1

	j = int(input("Enter doc no to be updated "))


	#print('Enter entries to be updated:')
	print("Enter the keys to be updated, split by # 	")
	list_key_update = []
	
	list_key_update = [input().split('#')]
	for key in list_key_update:
		print('Enter new value of ', key)
		new_val = input()
		try:
			col.update_one(select[j-1],{'$set':{update[0]:new_val}})
			
		except pymongo.errors.DuplicateKeyError as e:
			print("exception as :",e)
	import pprint
	pprint.pprint(col.find_one({update[0]:new_val}))

#							***********DELETE*********

#delete a document
def delete_document(select):
	cnt = 1
	for i in select:
		print(cnt,i)
		cnt +=1

	j = int(input("Enter doc no to be updated"))
	
	col.delete_one(select[j-1])

# DEFINED FUNCTIONS END


if (num == 1):

	while 1:
		opt = input("1 to continue 0 to exit ")
		if(opt is '1'):
		
			#pass the arguments to inserting data function
			insert_document()
		else:
			break
	
if (num == 2):
	# print all documents
	import pprint	
	# use projection to not to print Object id
	for itr in col.find({},{'_id':0}):
		pprint.pprint(itr)
	
	total = col.count()
	print("Total no of documents are ", total)

if (num == 3):
	find_document()	

# Find Document
if (num == 4):
	while True:
		opt = input("1 to find doc 2 to exit")
		opt = int(opt)
		if(opt == 1):
			find_document()
		else:
			break


if (num == 5):
	while True:
		opt = input("1 to continue 2 to exit")
		opt = int(opt)
		if(opt == 1):
			find_document()
		else:
			break
		
		
	

