import sqlite3
conn = sqlite3.connect('gestion_contact.db')
cur = conn.cursor()
req = "SELECT * FROM contact "
cur.execute(req)
res = cur.fetchall()

for row in res:
    print("id: ", row[0])
    print("nom: ", row[1])
    print("prenom: ", row[2])
    print("Email: ", row[3])
    print("numtel: ", row[4])
    print("adress: ", row[5])
conn.commit()
conn.close()