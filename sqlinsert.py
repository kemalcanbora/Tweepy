#!/usr/bin/python

import MySQLdb

db=MySQLdb.connect(host='111.111.111.11', user="root", passwd="some_pass", db='somedb')


cursor = db.cursor()
cursor.execute("""INSERT INTO Country (CountryName) VALUES (%s)""",('Germany'))
db.commit()
cursor.execute("select * from City")
rows = cursor.fetchall()
for eachRow in rows:
    print eachRow
db.close()