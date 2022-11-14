import sqlite3

connection = sqlite3.connect("/Users/gracepichar/Desktop/SQl/chinook.db") #connect to data
print("Connect to DB Succedd !")
cursor = connection.execute("SELECT * FROM customers;") #qury
for row in cursor: #print row in customer table
    print('Customer ID:', row[0], row[2]) #array
connection.close()