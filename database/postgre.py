import psycopg2

def create_table():
	conn = psycopg2.connect("dbname='pypostgres' user='postgres' password='postgres' host='localhost' port='5432'")
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)")
	conn.commit()
	cur.close()

def insert(item, quantity, price):
	conn = psycopg2.connect("dbname='pypostgres' user='postgres' password='postgres' host='localhost' port='5432'")
	cur = conn.cursor()
	cur.execute("INSERT INTO store VALUES(%s,%s,%s)", (item, quantity, price))
	conn.commit()
	cur.close()


def view():
	conn = psycopg2.connect("dbname='pypostgres' user='postgres' password='postgres' host='localhost' port='5432'")
	cur = conn.cursor()
	cur.execute("SELECT * FROM store")
	res = cur.fetchall()
	cur.close()
	return res # result returned a Python list

def delete(item):
	conn = psycopg2.connect("dbname='pypostgres' user='postgres' password='postgres' host='localhost' port='5432'")
	cur = conn.cursor()
	cur.execute("DELETE FROM store WHERE item=%s", (item,))
	conn.commit()
	cur.close()


def update(item, quantity, price):
	conn = psycopg2.connect("dbname='pypostgres' user='postgres' password='postgres' host='localhost' port='5432'")
	cur = conn.cursor()
	cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
	conn.commit()
	cur.close()


#create_table()
#insert("Coffee", 20, 250)
insert("Syrup", 10, 400)
#insert("Tea Cup", 10, 20)
#delete("Water Cup")
#delete("Tea Cup")
#delete("Tea")
update("Coffee", 5, 300)
print(view())