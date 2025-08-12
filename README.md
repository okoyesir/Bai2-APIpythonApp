# 🌱 Quản lý & Thống kê Dữ liệu Môi Trường – Flask + Firebase

## 1. Giới thiệu
Dự án gồm **2 ứng dụng Flask**:

- **App1**: Quản lý dữ liệu môi trường, lưu trữ vào **Firebase Firestore** và cung cấp API.
- **App2**: Lấy dữ liệu từ App1 (hoặc trực tiếp từ Firestore) để hiển thị, thống kê và lọc tìm kiếm.

Cả hai ứng dụng có thể giao tiếp qua **HTTP API** hoặc kết nối chung tới Firebase.

---

## 2. Cấu trúc chức năng

### **App1** – Quản lý dữ liệu + API
**Giao diện web**:
- Thêm dữ liệu môi trường
- Xóa dữ liệu môi trường

**API JSON**:
- `GET /api/environment` → Lấy toàn bộ dữ liệu môi trường

**Dữ liệu lưu**:

| Trường       | Mô tả              |
|--------------|--------------------|
| Name         | Tên địa điểm       |
| Time         | Thời gian đo       |
| Temperature  | Nhiệt độ (°C)      |
| Humidity     | Độ ẩm (%)          |
| Wind         | Tốc độ gió (m/s)   |
| Pressure     | Áp suất (hPa)      |

---

### **App2** – Hiển thị & thống kê
- Hiển thị bảng dữ liệu môi trường
- Thống kê số lượng bản ghi, giá trị trung bình, min, max
- Tìm kiếm theo tên địa điểm
- Lọc dữ liệu theo **ngày bắt đầu** và **ngày kết thúc**

---

## 3. Công nghệ sử dụng
- **Ngôn ngữ**: Python 3
- **Framework**: Flask
- **CSDL**: Firebase Firestore

---

## 4. Giao diện
- Giao diện App1
<img width="1919" height="1030" alt="Screenshot 2025-08-12 110902" src="https://github.com/user-attachments/assets/e21429a4-eca2-4b0e-84f6-ddbc5c8062f6" />
- Giao diện App2
<img width="1919" height="536" alt="Screenshot 2025-08-12 110911" src="https://github.com/user-attachments/assets/acd09e29-e37d-47b5-b3a5-d77dd1d96ad6" />

---

## 5. Mục tiêu
- Xây dựng hệ thống quản lý dữ liệu môi trường đơn giản.
- Tách thành 2 ứng dụng:
- **App1**: CRUD dữ liệu và cung cấp API.
- **App2**: Lấy dữ liệu từ App1/Firebase, hiển thị và thống kê.
- Học cách:
- Kết nối Flask với Firebase Firestore.
- Tạo API JSON để chia sẻ dữ liệu.
- Hiển thị dữ liệu + biểu đồ Chart.js.
- Lọc dữ liệu theo khoảng thời gian (từ ngày - đến ngày).
