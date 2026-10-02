import os
from flask import Flask, render_template, request, redirect, url_for

# ระบุ Path โฟลเดอร์ templates ให้แน่ชัดสำหรับ Vercel
base_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(base_dir, 'templates')

app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == 'admin' and password == '1234':
            return 'เข้าสู่ระบบสำเร็จ', 200
        return 'ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง', 401
        
    return render_template('login.html')