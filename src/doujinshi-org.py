import os
import sqlite3


db_path = os.path.dirname(os.path.abspath(__file__))
con = sqlite3.connect(os.path.join(db_path, "Database", "doujinshi.org.db"))

cur = con.cursor()

res = cur.execute("SELECT * FROM Book LIMIT 10")

print(res.fetchall())

con.close()