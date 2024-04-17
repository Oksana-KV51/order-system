import sqlite3
conn = sqlite3.connect('example.db')
cur = conn.cursor()

cur.execute("SELECT * FROM users")
#Вводим функцию для выведения информации:
rows = cur.fetchall()
for row in rows:
    print(row)

#cur.execute("""
    #CREATE TABLE IF NOT EXISTS users
    #(id INTEGER PRIMARY KEY AUTOINCREMENT,
    #name TEXT NOT NULL,
    #age INTEGER NOT NULL)
    #""")

#conn.commit()

#cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Алексей', 30))
#cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Михаил', 33))
#conn.commit()
conn.close()
