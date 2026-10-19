# UTS Graf Sains Data

Repositori ini berisi hasil pengerjaan Ujian Tengah Semester (UTS) mata kuliah Graf Sains Data menggunakan Python, Neo4j, dan dataset RetailRocket.

## Dataset

Dataset yang digunakan adalah **RetailRocket E-Commerce Dataset**, yang berisi data interaksi pengunjung dengan produk, seperti `view`, `addtocart`, dan `transaction`.

Sumber dataset: https://www.kaggle.com/datasets/retailrocket/ecommerce-dataset

Data dibagi berdasarkan waktu menjadi dua periode:

- **P1 (Training):** 16–23 Agustus 2015, sebanyak 141.416 interaksi.
- **P2 (Testing):** 24–29 Agustus 2015, sebanyak 111.532 interaksi.

Kedua file hasil filter tersedia dalam folder `dataset/hasil_filter/`.

File asli `events.csv` tidak disertakan dalam repositori. Jika ingin menjalankan proses pengolahan dari awal, unduh dataset dari Kaggle dan letakkan `events.csv` di folder `dataset/`.

## Isi Repositori

- `UTS_Graf_Sains_Data.ipynb` — Notebook utama yang berisi kode, hasil pengujian, visualisasi, dan penjelasan.
- `latihan_driver_neo4j.py` — Program latihan koneksi Python dengan Neo4j.
- `requirements.txt` — Daftar dependensi Python.
- `dataset/hasil_filter/events_p1_train.csv` — Dataset training P1.
- `dataset/hasil_filter/events_p2_test.csv` — Dataset testing P2.
- `visualisation.png` — Visualisasi graf pertemanan Neo4j.
- `graf_sebelum_similarity.png` — Graf sebelum penambahan hubungan similarity.
- `graf_sesudah_similarity.png` — Graf setelah penambahan hubungan similarity.

## Tahapan Pengerjaan

Pengerjaan UTS meliputi persiapan lingkungan Python, penggunaan Python Driver Neo4j, filtering dataset, dan impor data RetailRocket ke Neo4j.

Analisis dilanjutkan dengan pembuatan Vector Space Modelling (VSM) untuk User dan Item, visualisasi graf menggunakan NetworkX, perbandingan proyeksi User–User dan Item–Item, serta perhitungan Cosine Similarity.

Tahap akhir menggunakan Item-Based KNN dengan `k = 5` untuk membuat rekomendasi produk. Hasil rekomendasi dievaluasi menggunakan `Hit@5` dan `NDCG@5`.

## Hasil Evaluasi

Pengujian dilakukan terhadap User `382867` yang dipilih secara acak dengan `seed = 185` dari kelompok User yang memenuhi kriteria pemilihan.

Hasil evaluasi yang diperoleh:

- **Hit@5:** 0
- **NDCG@5:** 0,0000

Lima rekomendasi teratas belum sesuai dengan Item baru yang diakses User pada periode testing. Pemeriksaan tambahan menunjukkan bahwa Item relevan tersedia dalam data training, tetapi tidak memiliki kemiripan langsung dengan Item riwayat User berdasarkan Cosine Similarity yang digunakan.

Hasil evaluasi ini hanya berlaku untuk User yang diuji dan belum mewakili performa sistem rekomendasi secara keseluruhan.

## Cara Menjalankan

Proyek dikerjakan menggunakan Python 3.10 dan Neo4j Desktop.

1. Siapkan Python dan virtual environment.
2. Instal dependensi dari `requirements.txt` serta library lain yang digunakan dalam notebook jika belum tersedia.
3. Siapkan Neo4j Desktop dan database `neo4j`.
4. Unduh dataset asli jika ingin mengulangi proses filtering.
5. Buka `UTS_Graf_Sains_Data.ipynb` menggunakan Jupyter Notebook.
6. Jalankan kode sesuai urutan pengerjaan. Proses impor Neo4j memerlukan database yang masih kosong agar data tidak terimpor berulang.

Hasil eksekusi dan penjelasan dari pengerjaan sebelumnya sudah disimpan dalam notebook.
