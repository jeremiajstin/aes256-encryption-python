# 🔐 AES-256 Encryption & Decryption Program

## 📘 Deskripsi Proyek
Proyek ini merupakan implementasi algoritma **AES-256 (Advanced Encryption Standard)** untuk melakukan proses **enkripsi dan dekripsi data teks** menggunakan bahasa pemrograman **Python**.  
Program ini dibuat untuk tujuan pembelajaran keamanan data, khususnya dalam memahami cara kerja kriptografi simetris dan penerapannya di dunia nyata.

AES-256 bekerja dengan panjang kunci **256-bit**, menggunakan empat tahapan utama:
1. **SubBytes**  
2. **ShiftRows**  
3. **MixColumns**  
4. **AddRoundKey**

Setiap proses dilakukan berulang pada blok data 128-bit untuk menjamin keamanan dan kerahasiaan informasi.

---

## ⚙️ Fitur Program
- 🔑 **Hashing Key Otomatis**: Input kunci dari pengguna akan diubah menjadi 32-byte key menggunakan **SHA-256**.  
- 🔒 **AES-256 Mode CBC**: Enkripsi dengan IV (Initialization Vector) acak untuk setiap proses.  
- 📁 **Penyimpanan Data Otomatis**: Hasil enkripsi tersimpan ke folder `/data` dalam format `.csv`.  
- 🔄 **Dekripsi Otomatis**: Dapat mengembalikan ciphertext menjadi plaintext jika kunci benar.  
- 🧠 **Integrasi Pandas**: Mendukung input/output berbasis CSV untuk memudahkan analisis data.

---

## 📦 Library yang Digunakan
| Library | Fungsi |
|----------|--------|
| `cryptography` | Implementasi AES-256 (enkripsi & dekripsi) |
| `hashlib` | Hashing kunci dengan SHA-256 |
| `os` | Generate IV dan membuat direktori penyimpanan |
| `base64` | Encoding hasil enkripsi agar mudah disimpan |
| `pandas` | Membaca dan menyimpan data terenkripsi ke CSV |

Instalasi:
```bash
pip install cryptography pandas
