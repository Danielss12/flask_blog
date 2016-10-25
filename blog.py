# blog.py - controller/this script will define the imports, configurations, and each view

#imports
from flask import Flask, render_template, request, session, flash, redirect, url_for, g

#configuration
DATABASE = 'blog.db'

app = FLASK(__name__)

# pulls in app configuration by looking for UPPERCASE variables
app.config.from_object(__name__)

#function used for connection to the database
def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

if __name__ == '__main__':
	app.run(debug=True)

	