import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import normalize
import tensorflow as tf
from transformers import TFBertModel, BertTokenizer
import os
import gdown

embedding_path = "anime_ensemble_embeddings.npy"
if not os.path.exists(embedding_path):
    gdown.download(
        "https://drive.google.com/uc?id=1x1RlYD1GcogqTYakXu9kUE8YUa6MAwZ5",
        embedding_path,
        quiet=False
    )

embeddings = np.load(embedding_path)


# --- Load all models and data ---
with open("anime_metadata.pkl", "rb") as f:
    df = pickle.load(f)

# embeddings = np.load("anime_ensemble_embeddings.npy")
genre_vecs = np.load("anime_genre_vecs.npy")
numeric_vecs = np.load("anime_numeric_vecs.npy")

with open("tfidf_vectorizer.pkl", "rb") as f:
    tfidf = pickle.load(f)

with open("mlb.pkl", "rb") as f:
    mlb = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# --- Cache SBERT & BERT ---
@st.cache_resource
def load_sbert():
    from sentence_transformers import SentenceTransformer
    return SentenceTransformer("all-MiniLM-L6-v2")

@st.cache_resource
def load_bert():
    return TFBertModel.from_pretrained("bert-base-uncased")

@st.cache_resource
def load_tokenizer():
    return BertTokenizer.from_pretrained("bert-base-uncased")

sbert_model = load_sbert()
bert_model = load_bert()
bert_tokenizer = load_tokenizer()

# --- Recommender function ---
# --- Recommender function dengan genre, score, members, year ---
def recommend_hybrid_ensemble(
    query_text,
    model_sbert,
    tfidf,
    model_bert,
    bert_tokenizer,
    mlb,
    scaler,
    anime_df,
    embeddings,
    genre_vecs,
    numeric_vecs,
    input_genres=None,
    input_score=None,
    input_members=None,
    input_year=None,
    top_k=5
):
    from sklearn.metrics.pairwise import cosine_similarity

    # 1. Embed sinopsis
    q_sbert = model_sbert.encode([query_text])
    q_tfidf = tfidf.transform([query_text]).toarray()
    inputs = bert_tokenizer(query_text, return_tensors="tf", padding=True, truncation=True)
    outputs = model_bert(inputs)
    q_bert = outputs.last_hidden_state[:, 0, :].numpy()
    q_ens = np.concatenate([q_sbert, q_tfidf, q_bert], axis=1)

    # 2. Inisialisasi
    query_parts = [q_ens[0]]
    base_parts = [embeddings]

    # 3. Genre
    if input_genres:
        genre_vec = mlb.transform([input_genres])[0]
        query_parts.append(genre_vec)
        base_parts.append(genre_vecs)

    # 4. Numeric
    if None not in (input_score, input_members, input_year):
        numeric_vec = scaler.transform([[input_score, input_members, input_year]])[0]
        query_parts.append(numeric_vec)
        base_parts.append(numeric_vecs)

    # 5. Gabungkan dan normalisasi
    query_vec = np.concatenate(query_parts).reshape(1, -1)
    base_vec = np.concatenate(base_parts, axis=1)

    query_vec = normalize(query_vec)
    base_vec = normalize(base_vec)

    st.write("Final query shape:", query_vec.shape)
    st.write("Final base shape:", base_vec.shape)

    # 6. Cosine similarity
    sim_scores = cosine_similarity(query_vec, base_vec)[0]
    top_idx = sim_scores.argsort()[::-1][:top_k]

    results = anime_df.iloc[top_idx].copy()
    results["similarity"] = sim_scores[top_idx]
    return results[['title', 'title_english', 'score', 'genres', 'url', 'image_url', 'similarity']]


# --- Streamlit UI ---
st.set_page_config(page_title="Anime Recommender", page_icon="🎬")
st.title("🎬 Anime Recommendation System (Hybrid Ensemble)")
 


query = st.text_input("Deskripsi sinopsis atau cerita yang kamu suka:")
selected_genres = st.multiselect("Genre favorit (opsional):", mlb.classes_.tolist())
score = st.slider("Skor minimal (opsional):", 0.0, 10.0, step=0.1)
members = st.number_input("Jumlah anggota minimal (opsional):", min_value=0, step=1000)
year = st.number_input("Tahun rilis (opsional):", min_value=1900, max_value=2025, step=1)
if st.button("🎯 Rekomendasikan"):
    if not query.strip():
        st.warning("Masukkan deskripsi anime terlebih dahulu.")
    else:
        results = recommend_hybrid_ensemble(
            query_text=query,
            model_sbert=sbert_model,
            tfidf=tfidf,
            model_bert=bert_model,
            bert_tokenizer=bert_tokenizer,
            mlb=mlb,
            scaler=scaler,
            anime_df=df,
            embeddings=embeddings,
            genre_vecs=genre_vecs,
            numeric_vecs=numeric_vecs,
            input_genres=selected_genres if selected_genres else None,
            input_score=score if score > 0 else None,
            input_members=members if members > 0 else None,
            input_year=year if year > 1900 else None,
            top_k=5
        )

        st.subheader("🔎 Hasil Rekomendasi:")
        for _, row in results.iterrows():
            st.markdown(f"### [{row['title']}]({row['url']})")
            st.markdown(f"**Skor**: {row['score']} | **Genres**: {row['genres']}")
            st.markdown(f"**Similarity**: {row['similarity']:.4f}")
            st.image(row["image_url"], width=200)
            st.markdown("---")
