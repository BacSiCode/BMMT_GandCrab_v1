# Phân tích và mô phỏng Ransomware GandCrab

## Giới thiệu
Đây là đồ án học phần Bảo mật máy tính với mục tiêu tìm hiểu cơ chế hoạt động của ransomware GandCrab và xây dựng chương trình mô phỏng quá trình mã hóa/giải mã dữ liệu trong môi trường lab.

Dự án phục vụ mục đích học tập và nghiên cứu an toàn thông tin, không sử dụng cho mục đích tấn công thực tế.

---

## Mục tiêu
- Tìm hiểu mô hình Ransomware-as-a-Service (RaaS)
- Phân tích cơ chế lây nhiễm qua email giả mạo
- Nghiên cứu thuật toán mã hóa AES + RSA
- Mô phỏng quá trình mã hóa dữ liệu và khôi phục
- Nâng cao nhận thức phòng chống ransomware

---

## Môi trường & Công cụ
- Kali Linux
- VMware Workstation (dựng máy ảo attacker/victim)
- Python (xây dựng chương trình mô phỏng + GUI)
- Windows (máy nạn nhân)

---

## Kịch bản mô phỏng (Demo Scenario)

### Bước 1 – Chuẩn bị môi trường
- Tạo 2 máy ảo: Attacker (Kali Linux) và Victim (Windows)
- Chuẩn bị các file dữ liệu mẫu trên máy nạn nhân

### Bước 2 – Phát tán
- Attacker gửi email giả mạo có file đính kèm chứa mã độc
- Nạn nhân tải và mở file

### Bước 3 – Lây nhiễm
- Chương trình mô phỏng được thực thi
- Tạo khóa mã hóa
- Quét và liệt kê các file trong thư mục mục tiêu

### Bước 4 – Mã hóa
- File được mã hóa bằng AES
- Khóa AES được bảo vệ bằng RSA
- Đổi đuôi file
- Hiển thị thông báo đòi tiền chuộc

### Bước 5 – Giải mã
- Người dùng nhập mật khẩu/khóa do attacker cung cấp
- Chương trình giải mã và khôi phục dữ liệu

---

## Nội dung đã thực hiện
- Dựng lab bằng máy ảo để cô lập môi trường
- Phân tích cách GandCrab lây nhiễm và mã hóa
- Viết chương trình Python mô phỏng mã hóa/giải mã
- Xây dựng giao diện GUI cho demo
- Ghi nhận kết quả và báo cáo

---

## Vai trò cá nhân
- Nhóm trưởng
- Dựng môi trường lab (VMware + Kali Linux)
- Phân tích kỹ thuật mã hóa
- Viết code mô phỏng bằng Python
- Thực hiện demo

---

## Kiến thức rút ra
- Hiểu rõ cơ chế hoạt động của ransomware
- Thực hành dựng môi trường lab an toàn
- Làm quen với phân tích malware cơ bản
- Nâng cao kỹ năng Linux, VM, scripting Python
- Nhận thức về tầm quan trọng của sao lưu dữ liệu

---

