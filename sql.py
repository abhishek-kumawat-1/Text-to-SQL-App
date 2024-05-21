import sqlite3

#Connect to sqlite3
connection=sqlite3.connect("student.db")

#Create a cursor object to insert record, create table, retrieve
cursor=connection.cursor()

#Create a table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT) 
"""
cursor.execute(table_info)

#Insert some records
cursor.execute('''Insert Into STUDENT values('Ashutosh','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Abhishek','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Akash','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Arnesh','DevOps','A',50)''')
cursor.execute('''Insert Into STUDENT values('Aditya','DevOps','A',35)''')

#Display all the records
print("The inserted records are")

data=cursor.execute('''Select * From STUDENT''')

for row in data:
    print(row)

#Close the connection

connection.commit()
connection.close()
