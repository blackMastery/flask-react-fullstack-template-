import sqlite3

db = sqlite3.connect("testDB.db")
#Get a cursor object
cur  = db.cursor()
print("Connection was maded.....")
# cursor.execute('''
#     CREATE TABLE person(id INTEGER PRIMARY KEY, name TEXT,
#                        phone TEXT, email TEXT unique, password TEXT)
# ''')



cur.execute('SELECT SQLITE_VERSION()')

data = cur.execute('''
	SELECT "id", "topic", "description" from "references" where "id" < 10

	''')

list = {}
for idx, row in enumerate(data):
	list.append(row)
	print(row)





#data = cur.fetchone()
print("SQLite version: %s" % list  )     



# db.commit()
# cursor = db.cursor()
# name1 = 'Andres'
# phone1 = '3366858'
# email1 = 'user@example.com'
# # A very secure password
# password1 = '12345'
 
# name2 = 'John'
# phone2 = '5557241'
# email2 = 'johndoe@example.com'
# password2 = 'abcdef'
 
# # Insert user 1
# cursor.execute('''INSERT INTO person(name, phone, email, password)
#                   VALUES(?,?,?,?)''', (name1,phone1, email1, password1))
# print('First person inserted')
 
# # Insert user 2
# cursor.execute('''INSERT INTO person(name, phone, email, password)
#                   VALUES(?,?,?,?)''', (name2,phone2, email2, password2))
# print('Second person inserted')
 
# db.commit()