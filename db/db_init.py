import sqlite3

def init_db():
    with sqlite3.connect("db/database.db") as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            contact TEXT,
            diagnosis TEXT
        )''')
        c.execute('''CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER,
            date TEXT,
            duration INTEGER,
            fee REAL,
            FOREIGN KEY(patient_id) REFERENCES patients(id)
        )''')
        conn.commit()

if __name__ == "__main__":
    init_db()
