import sqlite3
conn = sqlite3.connect('gestion_contact.db')
cur = conn.cursor()
req = "UPDATE contact SET Email = 'fall@gmail.om' where id = 2"
cur.execute(req)
conn.commit()
conn.close()