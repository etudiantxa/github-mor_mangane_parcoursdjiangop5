import sqlite3
conn = sqlite3.connect('gestion_contact.db')
cur = conn.cursor()
req = "create table contact(id integer primary key autoincrement, nom text, prenom text, Email text, numtel text, adress text)"
cur.execute(req)
conn.commit()
conn.close()

   