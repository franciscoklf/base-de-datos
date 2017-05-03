import sqlite3
base = sqlite3.connect("d:\pi.db") #base es para conectar es una variable
c = base.cursor()
c.execute('SELECT * FROM FABRICANTES')
a = c.fetchall()
print(a)
c.execute('SELECT * FROM ARTICULOS')
a = c.fetchall()
print(a)
print("mucho mas no puedo hacer.")
