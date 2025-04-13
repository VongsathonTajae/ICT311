from flask import Flask, request, render_template, redirect, url_for
from database import connect_db

app = Flask(__name__)

# หน้าสำหรับยืนยันการลบข้อมูล
@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_patient(id):
    if request.method == 'POST':
        with connect_db() as conn:
            conn.execute("DELETE FROM patients WHERE id=?", (id,))
            conn.commit()
        return redirect(url_for('index'))
    
    return render_template("delete.html", patient_id=id)

if __name__ == '__main__':
    app.run(debug=True)