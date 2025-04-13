from flask import Flask, request, render_template, redirect, url_for
from database import connect_db

app = Flask(__name__)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    with connect_db() as conn:
        patient = conn.execute("SELECT * FROM patients WHERE id=?", (id,)).fetchone()
    
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        phone = request.form['phone']
        treatment = request.form['treatment']

        with connect_db() as conn:
            conn.execute("UPDATE patients SET name=?, age=?, phone=?, treatment=? WHERE id=?", 
                         (name, age, phone, treatment, id))
            conn.commit()
        return redirect(url_for('index'))
    
    return render_template("update.html", patient=patient)

if __name__ == '__main__':
    app.run(debug=True)