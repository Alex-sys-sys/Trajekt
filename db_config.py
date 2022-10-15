import sqlite3


db = sqlite3.connect('ingridients.db')
cursor = db.cursor()

data = cursor.execute('SELECT * FROM ingr').fetchall()
print(data)
