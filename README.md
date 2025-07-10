# 🎌 Anime Recommendation System with Streamlit

Aplikasi web interaktif untuk merekomendasikan anime berdasarkan sinopsis menggunakan pendekatan ensemble NLP: SBERT, BERT, dan TF-IDF. Dibuat dengan Python, Streamlit, dan cosine similarity.

## 🚀 Fitur

- 🔍 Input sinopsis atau judul anime favorit
- 🧠 Rekomendasi berbasis kemiripan semantik (dengan cosine similarity)
- 🤖 Kombinasi model SBERT + BERT + TF-IDF untuk hasil yang lebih akurat
- 📊 Tampilkan top-5 hasil rekomendasi
- 🌐 Tautan langsung ke MyAnimeList
- 💡 Berdasarkan cosine similarity antar vektor sinopsis anime

## 🧠 Teknologi

- **Python 3.11+**
- **Streamlit** untuk UI interaktif
- **sBERT (Sentence-BERT)** untuk sentence-level embeddings
- **BERT (transformers / bert-base-uncased)** untuk contextual embeddings
- **TF-IDF (TfidfVectorizer)** untuk representasi statistik klasik
- **scikit-learn** scikit-learn untuk cosine similarity dan pre-processing
- **pandas**, **numpy** untuk manipulasi data

## ⚙️ Pendekatan Ensemble

Model ini menggabungkan hasil dari tiga teknik representasi teks:

1. ✅ SBERT: untuk menangkap kemiripan semantik antar sinopsis
2. ✅ BERT (CLS pooling): untuk memahami konteks kalimat
3. ✅ TF-IDF: untuk menangkap keyword penting dan statistik lokal

Output ketiganya digabungkan dengan weighted average sebelum digunakan untuk menentukan kemiripan.

## 🗂 Dataset

Menggunakan data dari [Jikan API](https://jikan.moe/) yang telah disimpan dalam CSV:

- Judul anime
- Sinopsis
- Skor
- Genre
- Gambar
- URL MyAnimeList

Contoh data:

```csv
title,synopsis,score,genres,image_url,mal_url
"Attack on Titan","Humans fight titans in a walled city...",8.9,"Action, Drama",...
```

## 🖥️ Cara Menjalankan Lokal

### 1. Clone repositori ini

```bash
git clone https://github.com/Ashafaatadhis/anime-recomendation.git
cd anime-recommendation
```

### 2. Install dependensi

```bash
pip install -r requirements.txt
```

### 3. Jalankan aplikasi

```bash
streamlit run app.py
```

## 📂 Struktur Folder

```bash
.
├── app.py                 # File utama Streamlit
├── anime_data.csv         # Dataset lokal hasil dari Jikan API
├── model_utils.py         # Utilitas untuk embedding & similarity
├── requirements.txt       # Daftar dependensi Python
└── README.md              # Dokumentasi proyek
```

## 🌐 Demo Online

Kunjungi versi demo di Hugging Face Spaces:
🔗 https://ashafaatadhis-anime-recommended.hf.space

## 🧪 Cara Menggunakan

1. Masukkan sinopsis atau judul anime yang kamu suka.
2. Klik tombol **"Recommend"**.
3. Lihat hasil rekomendasi anime yang paling mirip.
4. Kamu bisa atur jumlah rekomendasi yang ditampilkan (**Top N**).

---

## ✅ To-Do (Roadmap)

- [ ] Filter berdasarkan genre
- [ ] Tambah rating minimal
- [ ] Mode collaborative filtering (berbasis user)
- [ ] Tambah bookmark/favorit
- [ ] Deploy ke personal domain

---

## 📬 Kontak

Dikembangkan oleh [@ashafaatadhis](https://github.com/ashafaatadhis)  
📧 Email: ashafaatadhis@gmail.com
