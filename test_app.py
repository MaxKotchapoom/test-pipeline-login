import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# 1. ทดสอบว่าหน้า HTML โหลดได้ปกติ (GET /login)
def test_login_page_renders(client):
    response = client.get('/login')
    assert response.status_code == 200
    # ตรวจสอบว่ามีข้อความจาก HTML ปรากฏอยู่จริง
    assert "เข้าสู่ระบบ" in response.get_data(as_text=True)

# 2. ทดสอบส่งข้อมูลถูก (POST /login)
def test_login_success(client):
    response = client.post('/login', data={
        'username': 'admin',
        'password': '1234'
    })
    assert response.status_code == 200
    assert "เข้าสู่ระบบสำเร็จ" in response.get_data(as_text=True)

# 3. ทดสอบส่งรหัสผ่านผิด
def test_login_wrong_password(client):
    response = client.post('/login', data={
        'username': 'admin',
        'password': 'wrongpassword'
    })
    assert response.status_code == 401
    assert "ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง" in response.get_data(as_text=True)