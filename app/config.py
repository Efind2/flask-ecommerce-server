import os
from datetime import timedelta

# Tentukan direktori root proyek Anda secara dinamis
# Ini penting agar UPLOAD_FOLDER selalu mengarah ke lokasi yang benar
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY') or 'kunci_rahasia_yang_sangat_kuat_dan_acak_di_produksi'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                                'postgresql://postgres:123@localhost:5432/mobileDB'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    STATIC_SALT = os.environ.get('STATIC_SALT') or 'ini_adalah_static_salt_anda_yang_super_panjang_dan_rahasia_di_dev'

    MOBILE_TOKEN_EXPIRY_DAYS = 90

    DEFAULT_PAGE_SIZE = 20
    MAX_PAGE_SIZE = 100

    # Konfigurasi Rentang Stok Acak
    MIN_STOCK_RANDOM = 10  # Stok minimum saat diacak
    MAX_STOCK_RANDOM = 100 # Stok maksimum saat diacak

    # --- TAMBAHKAN BARIS INI UNTUK UPLOAD_FOLDER ---
    UPLOAD_FOLDER = os.path.join(basedir, 'static', 'uploads')
    # Opsional: untuk validasi ekstensi file
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    # --- AKHIR TAMBAH ---

# import os
# from datetime import timedelta

# class Config:
#     SECRET_KEY = os.environ.get('FLASK_SECRET_KEY') or 'kunci_rahasia_yang_sangat_kuat_dan_acak_di_produksi'

#     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
#                             'postgresql://postgres:1234@localhost:5432/MobileDB'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False

#     STATIC_SALT = os.environ.get('STATIC_SALT') or 'ini_adalah_static_salt_anda_yang_super_panjang_dan_rahasia_di_dev'

#     MOBILE_TOKEN_EXPIRY_DAYS = 90

#     DEFAULT_PAGE_SIZE = 20
#     MAX_PAGE_SIZE = 100

#       # Konfigurasi Rentang Stok Acak
#     MIN_STOCK_RANDOM = 10  # Stok minimum saat diacak
#     MAX_STOCK_RANDOM = 100 # Stok maksimum saat diacak
