from flask import Flask, render_template, request
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

# Khởi tạo Flask
app = Flask(__name__)

# Kết nối Firebase
cred = credentials.Certificate(r"ThoiTiet/dichvuknvscn-firebase-adminsdk-fbsvc-5699470664.json")
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

db = firestore.client()

@app.route('/')
def index():
    # Lấy tham số lọc
    name_filter = request.args.get("name", "").strip().lower()
    start_date = request.args.get("start_date", "").strip()
    end_date = request.args.get("end_date", "").strip()

    docs = db.collection("environment").stream()

    data_list = []
    for i, doc in enumerate(docs, start=1):
        item = doc.to_dict()
        item["STT"] = i
        data_list.append(item)

    # Lọc theo tên
    if name_filter:
        data_list = [d for d in data_list if name_filter in d.get("Name", "").lower()]

    # Lọc theo khoảng ngày
    if start_date or end_date:
        filtered_list = []
        for d in data_list:
            time_str = d.get("Time", "")
            try:
                # Chuyển string sang datetime
                time_obj = datetime.strptime(time_str, "%Y-%m-%dT%H:%M")
            except:
                continue  # Bỏ qua nếu format không hợp lệ

            ok = True
            if start_date:
                start_obj = datetime.strptime(start_date, "%Y-%m-%d")
                if time_obj.date() < start_obj.date():
                    ok = False
            if end_date:
                end_obj = datetime.strptime(end_date, "%Y-%m-%d")
                if time_obj.date() > end_obj.date():
                    ok = False

            if ok:
                filtered_list.append(d)

        data_list = filtered_list

    return render_template("giaodien.html", data=data_list)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
