import sqlite3
conn = sqlite3.connect('gestion_contact.db')
cur = conn.cursor()
req = "insert into contact (nom, prenom, Email, numtel, adress) values ('mame', 'mbaye', 'mbaye@gmail.com', '771254587', 'thies')"
cur.execute(req)
conn.commit()
conn.close()