import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts(name, phone, email) VALUES('Tim', 6565678, 'time@malpa.com')")
db.execute("INSERT INTO contacts VALUES ('Brian', 1234, 'brian@malpa.pl')")

db.close()
