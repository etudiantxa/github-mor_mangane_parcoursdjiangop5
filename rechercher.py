import sqlite3
conn = sqlite3.connect('gestion_contact.db')
cur = conn.cursor()
req = "SELECT * FROM contact WHERE numtel = '777242643'"
cur.execute(req)
res = cur.fetchall()
for row in res:
    print(row)
conn.commit()
conn.close()