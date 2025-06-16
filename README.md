# 🛒 Flask E-Commerce Server

Sebuah server e-commerce berbasis Flask yang mendukung autentikasi pengguna, pengelolaan produk, web scraping dengan Selenium, serta integrasi dengan aplikasi mobile.

---

## 🚀 Instalasi & Menjalankan Proyek

Ikuti langkah-langkah di bawah ini untuk mengatur dan menjalankan proyek ini di lingkungan lokal Anda.

### 1. Klon Repositori

```bash
git clone https://github.com/Efind2/flask-ecommerce-server.git
cd flask-ecommerce-server
```

### 2. Buat dan Aktifkan Virtual Environment

Disarankan menggunakan virtual environment agar dependensi tidak bercampur dengan sistem global.

```bash
python -m venv venv
# Di Windows
.env\Scriptsctivate
# Di macOS/Linux
source venv/bin/activate
```

### 3. Instal Dependensi

```bash
pip install -r requirements.txt
```

> ⚠️ **Catatan:**  
> Pastikan Anda telah menginstal ChromeDriver dan PATH-nya sudah terdaftar di sistem Anda. Jika tidak, sesuaikan path di `app/services/crawler_service.py`.

---

### 4. Konfigurasi Database PostgreSQL

- Pastikan PostgreSQL sudah terinstal dan berjalan.
- Buat database baru, contoh: `mobileDB`.
- Perbarui `SQLALCHEMY_DATABASE_URI` di `app/config.py` sesuai kredensial Anda:

```python
# app/config.py
class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or         'postgresql://postgres:123@localhost:5432/mobileDB'
```

> 🔧 Ganti `postgres` dengan username PostgreSQL Anda, `123` dengan password, dan `mobileDB` dengan nama database Anda.

---

### 5. Inisialisasi Database

Gunakan `psql` atau alat database lain untuk menjalankan skrip SQL:

```bash
psql -U your_username -d mobileDB -f server.sql
```

> 🛑 **Penting:**  
> Ganti `your_username` dan `mobileDB` sesuai konfigurasi PostgreSQL Anda.

---

### 6. Jalankan Aplikasi Flask

```bash
python run.py
```

Aplikasi akan berjalan di `http://127.0.0.1:5000/`. Scheduler crawling akan otomatis dimulai di background.

---

## 📊 Menggunakan Fitur Utama

### 1. Autentikasi Pengguna

- **Registrasi:**  
  `POST /api/auth/register`  
  Body: `username`, `email`, `password`

- **Login:**  
  `POST /api/auth/login`  
  Mendapatkan token Bearer untuk akses API.

- **Membuka Toko (Penjual):**  
  `POST /api/auth/open_store`  
  Diperlukan token login. Body: `brand_name`

---

### 2. Mengelola Produk

- **Melihat Semua Produk:**  
  `GET /api/products/`  
  Mendukung query: `?q=keyword&category_id=1&sort_by=price&page=1&per_page=10`

- **Melihat Detail Produk:**  
  `GET /api/products/<product_id>`

- **Membuat Produk Baru (Penjual):**  
  `POST /api/products/create`  
  Diperlukan token Bearer. Body berisi nama produk, deskripsi, harga, gambar, dll.

---

### 3. Web Crawler (Scraping)

Crawler dapat berjalan otomatis dan juga dapat dipicu secara manual.

- **Mulai Scraping Manual (Admin):**  
  `POST /api/crawler/start-jakmall-selenium`  
  Body JSON:

```json
{
  "seed_url": "https://www.jakmall.com/search?q=aksesoris+fashion",
  "crawling_limit": 50
}
```

- **Ekspor Data Scraping (Admin):**  
  `GET /api/crawler/export?format=csv`  
  Format bisa `csv` atau `json`.

---

### 4. Mengimpor Produk dari CSV

- Siapkan file CSV (misal: `my_products.csv`) di folder utama.
- Sesuaikan file pada `import_products_from_csv.py`:

```python
# import_products_from_csv.py
csv_path = 'my_products.csv'
```

- Jalankan skrip:

```bash
python import_products_from_csv.py
```

---

### 5. Integrasi dengan Aplikasi Mobile

Server akan mengirim notifikasi produk baru ke endpoint:

```
http://10.0.2.2:8080/api/new_product_batch
```

Pastikan aplikasi mobile Anda siap menerima request `POST` di endpoint tersebut.

---

## 📂 Struktur Proyek (Singkat)

```
flask-ecommerce-server/
├── app/
│   ├── config.py
│   ├── models/
│   ├── routes/
│   ├── schemas/
│   ├── services/
│   └── ...
├── server.sql
├── run.py
├── requirements.txt
└── import_products_from_csv.py
```

---

## 📫 Kontak & Kontribusi

Pull request dan issue sangat terbuka! Jika Anda ingin berkontribusi atau menemukan bug, silakan buka [Issue](https://github.com/Efind2/flask-ecommerce-server/issues) atau buat PR baru.

---


Selamat membangun e-commerce Anda! 🚀
