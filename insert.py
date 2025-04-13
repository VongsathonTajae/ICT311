from flask import Blueprint, request, render_template, redirect, url_for
from database import connect_db

# สร้าง Blueprint ชื่อ insert_app
insert_app = Blueprint('insert_app', __name__, template_folder="templates")

# Route สำหรับเพิ่มข้อมูลผู้ป่วย (/insert)
@insert_app.route('/insert', methods=['GET', 'POST'])
def insert():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        phone = request.form['phone']
        treatment = request.form['treatment']

        with connect_db() as conn:
            conn.execute("INSERT INTO patients (name, age, phone, treatment) VALUES (?, ?, ?, ?)", 
                         (name, age, phone, treatment))
            conn.commit()
        return redirect(url_for('index'))
    
    return render_template("insert.html")
