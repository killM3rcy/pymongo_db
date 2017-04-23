from pymongo import MongoClient
import sys
import pprint
# create a variable client to connect to database
client = MongoClient()
#create a database
db = client.student
#create a collection
col = db.student_information


choice = {1: "insert_data", 2: "display_all_documents" , 3:"find_document" ,4: "update document",5: "delete_document" }

print("enter choice")
for i in choice:
	print(i ,':' +choice[i])

num = input()
num = int(num)


args = { }
#  ALL DEFINED FUNCTIONS

def insert_document(*args):
	"""db.student_information.insert_one({"name" : args[0], "age" : args[1],
	"course" : args[2], "email" : args[3], "Date of Birth" : args[4]})"""
	print("Enter data to be inserted :)
	print("Format key:val")
	while (val != ""):
		dict{}
		doc = input('key:val').split(':')
		db.student_information.insert_one(doc)
		
	

def get_data():

	print("use # after every argument")
	name,age,course,email,dob = input("Enter students name,age,course,email,DOB\n").split("#")
	return [name,age,course,email,dob]


#	FIND A DOCUMENT	

	
def find_document():
	print('find document by :')
	print('"name" , "age", "course", "email", "Date of Birth"')
	# get key to be updated
	key = input()
	list_keys = ['name' , 'age', 'course', 'email', 'Date_of_birth']
	if key in list_keys:
		pass
	else:
		print('Enter correct key')
		find_document()
	print('Enter the val')
	# get value of key to be updated
	val = input()
	try:
		cursor = col.find({key:val},{'_id':0})
	except Exception as e:
		print("Unexpecred error", type(e),e)
	for doc in cursor:
		print(doc)
	
	
	# if update document		
	if (num == 4):
		
		#global update
		update = {key,val}
		update_document(update)
	
	if (num ==5):
		global update
		update = {key:val}
		print("Do you want to delete the foll deocument\ty/n?")
		cnf = input()
		if (cnf == 'y' or cnf == 'Y'):
		
			delete_document(update)
		else:
			pass
	
# update document
def update_document(update):
	print(update)
	key_tmp = update.keys()	
	val = update[1]
	print('Enter entries to be updated:')
	print('name' , 'age', 'course', 'email', 'Date_of_birth' ,'sepearte by #')
	list_key = ['name' , 'age', 'course', 'email', 'Date_of_birth']
	#list_key_update = []
	list_key_update = [input().split('#')]
	for key in list_key_update:
		print('Enter new value of ', key)
		new_val = input()
		col.update({update[0]:update[1]},{'$set':{update[0]:new_val}})
	import pprint
	pprint.pprint(col.find_one({update[0]:new_val}))
	
	
	
#delete a document
def delete_document(update):
	print(update)
	col.delete_one(update)
	
# DEFINED FUNCTIONS END


if (num == 1):

	while 1:
		opt = input("1 to continue 0 to exit ")
		if(opt is '1'):
			args = get_data()
			#pass the arguments to inserting data function
			insert_document(*args)
		else:
			break
		
if (num == 2):
	# print all documents
	import pprint	
	# use projection to not to print Object id
	for itr in col.find({},{'_id':0}):
		pprint.pprint(itr)

if (num == 3):
	find_document()	
	
	
if (num == 4):
	while True:
		opt = input("1 to continue 2 to exit")
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
			
			
			
		

