import sqlite3

def create_table():
	conn = sqlite3.connect("sqlt3.db")
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)")
	conn.commit()
	cur.close()

def insert(item, quantity, price):
	conn = sqlite3.connect("sqlt3.db")
	cur = conn.cursor()
	cur.execute("INSERT INTO store VALUES(?,?,?)", (item, quantity, price))
	conn.commit()
	cur.close()


def view():
	conn = sqlite3.connect("sqlt3.db")
	cur = conn.cursor()
	cur.execute("SELECT * FROM store")
	res = cur.fetchall()
	cur.close()
	return res # result returned a Python list

def delete(item):
	conn = sqlite3.connect("sqlt3.db")
	cur = conn.cursor()
	cur.execute("DELETE FROM store WHERE item=?", (item,))
	conn.commit()
	cur.close()


def update(item, quantity, price):
	conn = sqlite3.connect("sqlt3.db")
	cur = conn.cursor()
	cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quantity, price, item))
	conn.commit()
	cur.close()


#create_table()
#insert("Coffee Cup", 10, 25)
#insert("Water Cup", 10, 12)
#insert("Tea Cup", 10, 20)
#delete("Water Cup")
#delete("Tea Cup")
#delete("Coffee Cup")
#update("Water Cup", 5, 30)
print(view())