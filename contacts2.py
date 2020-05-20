import sqlite3

db = sqlite3.connect("contacts.sqlite")

update_sql = "UPDATE contacts SET email = 'update@malpa.com'"
update_cursor = db.cursor()
update_cursor.execute(update_sql)
print("{} rows updated".format(update_cursor.rowcount))

print()
print("Are connections the same: {}".format(update_cursor.connection == db))
print()

update_cursor.connection.commit()
update_cursor.close()

for row in db.execute("SELECT * FROM contacts"):
    print(row)

db.close()
