# Sistem Pakar Penyakit Padi

Sistem Pakar Penyakit Padi adalah sebuah aplikasi web sederhana yang menggunakan metode forward chaining untuk mendiagnosis penyakit padi berdasarkan gejala-gejala yang dimasukkan oleh pengguna. Aplikasi ini dibuat dengan menggunakan Python dan Flask.

## Penyakit yang Didukung

- Tungro
- Kerdil Rumput
- Kerdil Hampa
- Daun Jingga
- Kerdil Kuning
- Hawar Daun Bakteri

## Instalasi

1. **Klon repository ini:**

   ```sh
   git clone https://github.com/sayyidfaruk/paddy-project.git
   cd paddy-project
   ```

2. **Buat virtual environment:**

   ```sh
   python -m venv venv
   ```

3. **Aktifkan virtual environment:**

   - **Windows:**
     ```sh
     venv\Scripts\activate
     ```
   - **MacOS/Linux:**
     ```sh
     source venv/bin/activate
     ```

4. **Instal dependensi:**

   ```sh
   pip install -r requirements.txt
   ```

## Menjalankan Aplikasi

1. **Jalankan server Flask:**

   ```sh
   flask run
   ```

2. Buka browser Anda dan pergi ke `http://127.0.0.1:5000` untuk mengakses aplikasi.

## Penggunaan

1. Buka aplikasi di browser.
2. Masukkan gejala-gejala yang dialami oleh tanaman padi Anda.
3. Aplikasi akan menampilkan hasil diagnosa berdasarkan gejala yang Anda masukkan.

---

Selamat menggunakan aplikasi Sistem Pakar Penyakit Padi!
```
