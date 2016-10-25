# sql.py - Create a SQLite3 table and populate it with data
import sqlite3

# create a new database if the database doesnt exist
with sqlite3.connect("blog.db") as connection:
	c = connection.cursor()

	# create table
	c.execute("CREATE TABLE posts (title TEXT, post TEXT)")

	# insert dummy data into table
	c.execute('INSERT INTO posts VALUES("Okay", "I\'m okay.")')
	c.execute('INSERT INTO posts VALUES("Well", "I\'m Well.")')
	c.execute('INSERT INTO posts VALUES("Excellent", "I\'m Excellent.")')
	c.execute('INSERT INTO posts VALUES("Good", "I\'m Good.")')
