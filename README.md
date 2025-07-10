# 🎌 Anime Recommendation System with Streamlit

Sebuah aplikasi web interaktif untuk merekomendasikan anime berdasarkan kemiripan sinopsis menggunakan NLP dan cosine similarity. Dibuat dengan Python, Streamlit, dan model `sBERT` (Sentence-BERT).

## 🚀 Fitur

- 🔍 Input anime favorit via judul atau sinopsis
- 🤖 Rekomendasi anime dengan sinopsis paling mirip
- 📊 Tampilkan top-5 hasil rekomendasi
- 💡 Berdasarkan cosine similarity antar vektor sinopsis anime

## 🧠 Teknologi

- **Python 3.11+**
- **Streamlit** untuk UI interaktif
- **sBERT (Sentence-BERT)** untuk embedding teks
- **scikit-learn** untuk cosine similarity
- **pandas**, **numpy** untuk manipulasi data

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
