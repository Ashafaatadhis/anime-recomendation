FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Buat folder untuk cache huggingface dan .streamlit
RUN mkdir -p /app/.streamlit \
    /app/huggingface_cache/transformers \
    /app/huggingface_cache/torch \
    && chmod -R 777 /app

# ✅ Set HOME agar streamlit nulis ke /app/.streamlit
ENV PYTHONUNBUFFERED=1 \
    HOME=/app \
    HF_HOME=/app/huggingface_cache \
    TRANSFORMERS_CACHE=/app/huggingface_cache/transformers \
    TORCH_HOME=/app/huggingface_cache/torch

COPY . .

CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.address=0.0.0.0"]
