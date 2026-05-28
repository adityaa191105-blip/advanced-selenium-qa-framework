```markdown
# Advanced Selenium QA Framework

Repository ini berisi framework pengujian otomasi perangkat lunak (Automated Software Testing) berbasis antarmuka web (UI). Pengujian dibangun menggunakan **Selenium WebDriver** dan **Pytest**, serta dilengkapi dengan sistem pelaporan visual menggunakan **Allure Report**. 

Project ini juga sudah terintegrasi dengan Continuous Integration (CI) menggunakan **GitHub Actions**.

## 🚀 Teknologi yang Digunakan
*   **Python 3**
*   **Selenium WebDriver** (Automasi Browser)
*   **Pytest** (Framework Pengujian)
*   **Allure Report** (Sistem Pelaporan)
*   **GitHub Actions** (CI/CD Pipeline)

## 📦 Persiapan & Instalasi (Lokal)
Jika Anda ingin menjalankan project ini di komputer lokal, ikuti langkah-langkah berikut:

1. Pastikan Anda sudah menginstal Python (disarankan versi 3.10 atau lebih baru).
2. Clone repository ini:
```bash
   git clone [https://github.com/adityaa191105-blip/advanced-selenium-qa-framework.git](https://github.com/adityaa191105-blip/advanced-selenium-qa-framework.git)

```

3. Masuk ke direktori project:

```bash
   cd advanced-selenium-qa-framework

```

4. Install semua *library* pendukung yang dibutuhkan:

```bash
   pip install selenium pytest allure-pytest

```

## ⚙️ Cara Menjalankan Pengujian

Untuk mengeksekusi *test case* dan sekaligus menyimpan data mentah untuk laporan Allure, jalankan perintah berikut di Terminal/Command Prompt:

```bash
pytest --alluredir=allure-results

```

## 📊 Cara Melihat Laporan Allure

Setelah pengujian selesai dijalankan, Anda bisa merender dan melihat laporan HTML interaktif dari Allure dengan perintah:

```bash
allure serve allure-results

```

*(Catatan: Pastikan Anda sudah menginstal Allure Commandline di OS Windows/Linux/Mac Anda untuk membuka laporan ini).*

## 🔄 CI/CD Pipeline

Project ini dikonfigurasi untuk menjalankan pengujian secara otomatis di server GitHub (menggunakan GitHub Actions) setiap kali terdapat aksi `push` atau `pull_request` ke dalam *branch* `main`. Pengujian diatur agar berjalan menggunakan Chrome dalam mode *headless* (tanpa GUI).

```

***

### Cara Mengunggah `README.md` ke GitHub

Setelah file tersebut Anda buat dan simpan di dalam folder `advanced-selenium-qa`, Anda tinggal mengunggahnya ke GitHub dengan perintah Terminal yang sudah biasa Anda gunakan:

```bash
git add README.md
git commit -m "Menambahkan dokumentasi project di README.md"
git push origin main

```

Nanti, begitu Anda me-*refresh* halaman *repository* GitHub Anda, tampilan teks di atas akan langsung muncul dengan rapi di bagian bawah daftar file.

Semoga tugasnya mendapatkan nilai yang maksimal, ya!
