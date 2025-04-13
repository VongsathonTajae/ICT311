from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def get_db():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# สร้างตารางผู้ใช้
with get_db() as db:
    db.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT,
        birth_date TEXT,
        gender TEXT,
        phone TEXT,
        address TEXT,
        email TEXT UNIQUE,
        password TEXT
    )''')
    db.commit()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        db = get_db()
        user = db.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()
        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            flash('เข้าสู่ระบบสำเร็จ!', 'success')
            return redirect(url_for('index'))
        else:
            flash('อีเมลหรือรหัสผ่านไม่ถูกต้อง', 'error')

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        full_name = request.form['full_name']
        birth_date = request.form['birth_date']
        gender = request.form['gender']
        phone = request.form['phone']
        address = request.form['address']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash('รหัสผ่านไม่ตรงกัน', 'error')
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password)

        try:
            db = get_db()
            db.execute(
    'INSERT INTO users (full_name, birth_date, gender, phone, address, email, password) \
     VALUES (?, ?, ?, ?, ?, ?, ?)',
    (full_name, birth_date, gender, phone, address, email, hashed_password)
)
            db.commit()
            flash('ลงทะเบียนสำเร็จ! กรุณาเข้าสู่ระบบ', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('อีเมลนี้มีผู้ใช้งานแล้ว', 'error')

    return render_template('register.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('ออกจากระบบเรียบร้อยแล้ว', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)