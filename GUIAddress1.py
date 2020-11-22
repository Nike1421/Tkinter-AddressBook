import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS addresses (id INTEGER PRIMARY KEY,
            first_name text, last_name text, address text, city text, state text, pincode integer)""")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM addresses")
        rows = self.cur.fetchall()
        return rows

    def insert(self, f_name, l_name, address, city, state, pincode):
        self.cur.execute("INSERT INTO addresses VALUES (NULL, ?, ?, ?, ?, ?, ?)",
                         (f_name, l_name, address, city, state, pincode))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM addresses WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, f_name, l_name, address, city, state, pincode):
        self.cur.execute("UPDATE addresses SET first_name = ?, last_name = ?, address = ?, city = ?, state = ?, pincode = ? WHERE id = ?",
                         (f_name, l_name, address, city, state, pincode, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


#db = Database('address_book1.db')
#db.insert("Om", "Naik", "Ramedi", "Vasai", "Maharashtra", 401201)
#db.insert("Mike", "Henry", "Microcenter", "Florida", "Florida", 360)
