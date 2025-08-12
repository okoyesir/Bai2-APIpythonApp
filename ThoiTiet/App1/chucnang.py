from flask import Flask, render_template, request, redirect, url_for, flash
import firebase_admin
from firebase_admin import credentials, firestore
import uuid

# Kết nối Firebase
cred = credentials.Certificate("ThoiTiet/dichvuknvscn-firebase-adminsdk-fbsvc-5699470664.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = {
            "ID": str(uuid.uuid4())[:8],
            "Name": request.form.get("name"),
            "Time": request.form.get("time"),
            "Temperature": float(request.form.get("temperature")),
            "Humidity": float(request.form.get("humidity")),
            "Wind": float(request.form.get("wind")),
            "Pressure": float(request.form.get("pressure"))
        }
        db.collection("environment").add(data)
        flash("✅ Dữ liệu môi trường đã được lưu!", "success")
        return redirect(url_for("index"))

    # Lấy dữ liệu từ Firestore
    docs = db.collection("environment").stream()
    data_list = [doc.to_dict() | {"doc_id": doc.id} for doc in docs]

    return render_template("giaodien.html", data=data_list)

@app.route("/delete/<doc_id>")
def delete_data(doc_id):
    db.collection("environment").document(doc_id).delete()
    flash("Đã xóa dữ liệu!", "warning")
    return redirect(url_for("index"))

@app.route("/edit/<doc_id>", methods=["GET", "POST"])
def edit_data(doc_id):
    doc_ref = db.collection("environment").document(doc_id)

    if request.method == "POST":
        doc_ref.update({
            "Name": request.form.get("name"),
            "Time": request.form.get("time"),
            "Temperature": float(request.form.get("temperature")),
            "Humidity": float(request.form.get("humidity")),
            "Wind": float(request.form.get("wind")),
            "Pressure": float(request.form.get("pressure"))
        })
        flash("Đã cập nhật dữ liệu!", "info")
        return redirect(url_for("index"))

    doc = doc_ref.get()
    if doc.exists:
        return render_template("edit.html", data=doc.to_dict(), doc_id=doc_id)
    else:
        flash("Không tìm thấy dữ liệu!", "danger")
        return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True, port=5000)
