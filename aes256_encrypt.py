# ==========================================================
# AES-256 Encryption & Decryption Program (Final Version)
# ==========================================================
# Library yang digunakan:
# - cryptography: untuk AES-256
# - pandas: untuk membaca/menyimpan file CSV
# ==========================================================

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import hashlib
import os
import base64
import pandas as pd


# ==========================================================
# 1. Fungsi Hashing Key (Otomatis 32-byte dengan SHA-256)
# ==========================================================
def generate_key_from_input(key_input: str):
    """Mengubah input key menjadi 32-byte key menggunakan SHA-256"""
    key = hashlib.sha256(key_input.encode()).digest()
    return key


# ==========================================================
# 2. Fungsi Enkripsi AES-256
# ==========================================================
def encrypt_aes256(plaintext: str, key: bytes):
    """Melakukan enkripsi teks dengan AES-256 dalam mode CBC"""
    # Inisialisasi IV (Initialization Vector)
    iv = os.urandom(16)

    # Padding agar panjang data kelipatan 16 byte
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext.encode()) + padder.finalize()

    # Enkripsi menggunakan AES-CBC
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    # Gabungkan IV dan ciphertext, lalu encode ke base64 agar mudah disimpan
    return base64.b64encode(iv + ciphertext).decode()


# ==========================================================
# 3. Fungsi Dekripsi AES-256
# ==========================================================
def decrypt_aes256(ciphertext_base64: str, key: bytes):
    """Melakukan dekripsi teks terenkripsi AES-256 (base64)"""
    try:
        data = base64.b64decode(ciphertext_base64)
        iv = data[:16]
        ciphertext = data[16:]

        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted_padded = decryptor.update(ciphertext) + decryptor.finalize()

        # Hapus padding
        unpadder = padding.PKCS7(128).unpadder()
        decrypted_data = unpadder.update(decrypted_padded) + unpadder.finalize()

        return decrypted_data.decode()
    except Exception as e:
        return f"[Error] Gagal mendekripsi: {e}"


# ==============================================================
# 4. Fungsi Penyimpanan & Pembacaan Data CSV
# ==============================================================

def save_to_csv(filename, df):
    """Menyimpan DataFrame terenkripsi ke file CSV (otomatis ke folder data/)"""
    # Pastikan folder 'data' ada, kalau belum otomatis dibuat
    os.makedirs("data", exist_ok=True)
    
    # Buat path lengkap ke dalam folder data/
    filepath = os.path.join("data", filename)
    
    # Simpan DataFrame ke CSV
    df.to_csv(filepath, index=False)
    print(f"[✓] Data terenkripsi berhasil disimpan ke '{filepath}'")


def load_from_csv(filename):
    """Membaca file CSV terenkripsi dari folder data/"""
    filepath = os.path.join("data", filename)
    return pd.read_csv(filepath)

# ==========================================================
# 5. Fungsi Utama (Main)
# ==========================================================
def main():
    print("===== AES-256 Encryption Program =====")
    key_input = input("Masukkan key rahasia Anda: ")
    key = generate_key_from_input(key_input)

    pilihan = input("Pilih mode (1=Encrypt, 2=Decrypt): ")

    if pilihan == "1":
        plaintext = input("Masukkan teks yang ingin dienkripsi: ")
        ciphertext = encrypt_aes256(plaintext, key)
        print(f"Hasil Enkripsi (Base64): {ciphertext}")

        # Simpan ke CSV
        df = pd.DataFrame({"Plaintext": [plaintext], "Ciphertext": [ciphertext]})
        save_to_csv("encrypted_data.csv", df)

    elif pilihan == "2":
        try:
            ciphertext = input("Masukkan ciphertext (Base64): ")
            decrypted = decrypt_aes256(ciphertext, key)
            print(f"Hasil Dekripsi: {decrypted}")
        except Exception as e:
            print(f"[!] Dekripsi gagal: {e}")

    else:
        print("[!] Pilihan tidak valid.")


# ==========================================================
# Jalankan program
# ==========================================================
if __name__ == "__main__":
    main()
