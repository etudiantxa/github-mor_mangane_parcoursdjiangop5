import sqlite3
conn = sqlite3.connect('gestion_contact.db')
cur = conn.cursor()
req = "DELETE FROM contact WHERE id = 2"
cur.execute(req)
conn.commit()
conn.close()