from flask import Flask, render_template
from insert import insert_app  # ถ้ามี

app = Flask(__name__)

# Blueprint
app.register_blueprint(insert_app)

# หน้าแรก
@app.route('/')
def index():
    return render_template("index.html")

# เกี่ยวกับเรา
@app.route("/about")
def about():
    return render_template("about.html")

# บริการทั้งหมด
@app.route('/services')
def services():
    return render_template("services.html")

# หน้ารายละเอียดบริการ
@app.route('/services/<service_name>')
def service_detail(service_name):
    try:
        return render_template(f"service_{service_name}.html")
    except:
        return "ไม่พบหน้าบริการที่คุณต้องการ", 404

# โปรโมชั่นทั้งหมด
@app.route('/promotions')
def promotions():
    return render_template("promotions.html")

# หน้ารายละเอียดโปรโมชั่น
@app.route('/promotions/<promo_name>')
def promotion_detail(promo_name):
    try:
        return render_template(f"promotion_{promo_name}.html")
    except:
        return "ไม่พบหน้าโปรโมชั่นที่คุณต้องการ", 404

# ติดต่อเรา
@app.route("/contact")
def contact():
    return render_template("contact.html")

# Login
@app.route('/login')
def login():
    return render_template("login.html")

# Register
@app.route('/register')
def register():
    return render_template("register.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
