import sqlite3

db = sqlite3.connect("contacts.sqlite")

new_email = "anotherupdateddd@malpa.com"
phone = input("Please enter the phone number ")

update_sql = "UPDATE contacts SET email = '{}' WHERE phone = {}".format(new_email, phone)
update_cursor = db.cursor()
update_cursor.executescript(update_sql) # execute i executescript
print("{} rows updated".format(update_cursor.rowcount))

print()
print("Are connections the same: {}".format(update_cursor.connection == db))
print()

update_cursor.connection.commit()
update_cursor.close()

for row in db.execute("SELECT * FROM contacts"):
    print(row)

db.close()
