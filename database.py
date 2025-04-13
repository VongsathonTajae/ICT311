import sqlite3

DATABASE_NAME = "database.db"

def connect_db():
    return sqlite3.connect(DATABASE_NAME)

# สร้างตารางถ้ายังไม่มี
def create_table():
    with connect_db() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS patients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                phone TEXT NOT NULL,
                treatment TEXT NOT NULL
            )
        ''')
        conn.commit()

# เรียกใช้เมื่อต้องการสร้างฐานข้อมูลครั้งแรก
create_table()