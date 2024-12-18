# LinkScraper - Pro


LinkScraper Pro adalah alat canggih untuk memindai dan menganalisis tautan (links) pada suatu situs web. Program ini dirancang untuk membantu pengguna memverifikasi dan mengelola tautan di halaman web, baik internal (tautan antar halaman di dalam situs) maupun eksternal (tautan menuju situs lain). Selain itu, alat ini juga memungkinkan pengguna untuk mendeteksi tautan rusak atau tidak valid, yang sangat penting untuk menjaga integritas dan keamanan situs web.

#


Fitur Utama:


Pindai Tautan Internal dan Eksternal: Mengidentifikasi dan mengelompokkan tautan dalam situs web menjadi tautan internal dan eksternal.


Deteksi Tautan Rusak: Mendeteksi tautan yang tidak valid atau yang memberikan kesalahan HTTP, membantu menjaga kualitas dan kinerja situs web.


Multi-Threading: Menggunakan teknik pemrograman multi-threading untuk memindai halaman lebih cepat dan efisien.


Ambil Metadata Halaman: Mengambil metadata dari halaman web, seperti judul dan deskripsi halaman, untuk analisis lebih lanjut.


Penyimpanan Hasil: Menyimpan hasil pemindaian dalam format JSON dan CSV untuk kemudahan analisis dan laporan.


#
Cara Penggunaan:


1. Clone Repository: Pertama, clone repository ini ke komputer Anda.


```git clone https://github.com/mr4wp/LinkScraper-Pro.git```

2. Instal Dependensi: Instal pustaka Python yang dibutuhkan, seperti requests, beautifulsoup4, dan concurrent.futures.


```pip install requests beautifulsoup4```



3. Jalankan Program:


Setelah semua dependensi terpasang, jalankan program dengan perintah berikut:


```python linkscraper.py```



Masukkan domain situs web yang ingin dipindai saat diminta.

#


4. Hasil:


Program akan menghasilkan dua file di folder output/:


links.json: File JSON yang berisi tautan internal, eksternal, tautan rusak, dan metadata halaman.


links.csv: File CSV yang berisi daftar tautan beserta status HTTP mereka.
#


Manfaat:


Web Developer: Memeriksa dan memastikan tautan di situs web berfungsi dengan baik dan tidak ada tautan rusak.


SEO Specialist: Memastikan tidak ada tautan rusak atau eksternal yang memengaruhi peringkat SEO situs.


Administrator Keamanan Web: Memeriksa situs web untuk memastikan tidak ada tautan berbahaya atau eksternal yang mengarah ke situs berisiko.


Penyedia Layanan Audit Web: Membantu dalam audit dan pemeliharaan situs untuk memastikan kelancaran navigasi dan pengalaman pengguna yang optimal.
#


Teknologi yang Digunakan:


Python: Bahasa pemrograman yang digunakan.


BeautifulSoup: Untuk parsing HTML dan mencari tautan.


Requests: Untuk melakukan permintaan HTTP dan memeriksa status tautan.


ThreadPoolExecutor: Untuk melakukan scraping dengan menggunakan multi-threading agar proses lebih cepat.
#


Kontribusi:

Jika Anda ingin berkontribusi dalam pengembangan lebih lanjut, Anda dapat melakukan fork repositori ini dan membuat pull request. Semua kontribusi sangat dihargai!
#


Lisensi:
Program ini dirilis di bawah lisensi MIT.
