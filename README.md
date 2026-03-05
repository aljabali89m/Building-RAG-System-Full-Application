# Building-RAG-System-Full-Application

# 📚 RAG (Retrieval-Augmented Generation) — Multi-Model PDF Q&A

A lightweight RAG pipeline that loads PDFs into a **ChromaDB** vector store and lets you query them using multiple LLM backends. Compare responses across **Ollama (local)**, **HuggingFace Router**, and **OpenRouter (Grok)** — all from the same vector database.

---

## 🗂️ Project Structure

```
rag/
├── data/                   # 📁 Put your PDF files here
├── chroma-db/              # 📁 Auto-generated vector store (gitignored)
├── fill_db.py              # Loads PDFs → chunks → stores in ChromaDB
├── ask_ollama.py           # Query via local Ollama model
├── hugging-face.py         # Query via HuggingFace Inference Router
├── open-ai-router-using-grok-model.py  # Query via OpenRouter (Grok-3-mini)
├── requirements.txt        # Python dependencies
└── README.md
```

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### 2. Create and activate a virtual environment

```bash
python -m venv .rag_env

# Windows
.rag_env\Scripts\activate

# macOS/Linux
source .rag_env/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your PDFs

Place all PDF files you want to query inside the `data/` folder.

### 5. Fill the vector database

```bash
python fill_db.py
```

This will chunk your PDFs and store embeddings in `chroma-db/`.

---

## 🚀 Running a Query

### 🖥️ Option A — Ollama (Local, Free)

Requires [Ollama](https://ollama.com/) installed and running locally.

```bash
ollama pull hf.co/Qwen/Qwen2.5-7B-Instruct-GGUF:latest
python ask_ollama.py
```

You'll be prompted to type your question interactively.

---

### 🤗 Option B — HuggingFace Router

1. Get a free API key at [huggingface.co](https://huggingface.co/settings/tokens)
2. Replace `"your hugging face api key"` in `hugging-face.py`
3. Run:

```bash
python hugging-face.py
```

Model used: `meta-llama/Llama-3.1-8B-Instruct` via Novita provider.

---

### ⚡ Option C — OpenRouter (Grok-3-mini)

1. Get an API key at [openrouter.ai](https://openrouter.ai/)
2. Replace `"openrouter.ai api key"` in `open-ai-router-using-grok-model.py`
3. Run:

```bash
python open-ai-router-using-grok-model.py
```

Model used: `x-ai/grok-3-mini`

---

## 🔬 Model Comparison

All three scripts were tested with the same query: **"Who is NICOLE LURIE?"** against the same ChromaDB vector store.

| Feature | Ollama (Qwen 2.5-7B) | HuggingFace (Llama 3.1-8B) | OpenRouter (Grok-3-mini) |
|---|---|---|---|
| **Cost** | 🆓 Free (local) | 🆓 Free tier available | 💰 Pay-per-token |
| **Privacy** | ✅ Fully local | ☁️ Cloud | ☁️ Cloud |
| **Speed** | ⚠️ Depends on hardware | ✅ Fast | ✅ Fast |
| **Answer quality** | ⭐⭐⭐ Good | ⭐⭐⭐ Good | ⭐⭐⭐⭐⭐ Excellent |
| **Answer depth** | Brief, factual | Brief, factual | Detailed, comprehensive |
| **Hallucination risk** | Low | Low | Low (grounded by RAG) |
| **Setup complexity** | Medium (install Ollama) | Easy | Easy |
| **Internet required** | ❌ No | ✅ Yes | ✅ Yes |

### 📝 Sample Answer Quality

**Query:** *"Who is NICOLE LURIE?"*

> **Ollama (Qwen 2.5-7B):**
> *Concise. Mentioned her award and clinical practice in Washington DC. Missed education details.*

> **HuggingFace (Llama 3.1-8B):**
> *Brief. Mentioned her award and clinical practice. Similar depth to Ollama.*

> **OpenRouter (Grok-3-mini):**
> *Comprehensive. Covered research areas, multiple awards, education (UPenn + UCLA), professional roles at Minnesota DOH and University of Minnesota — the most complete answer from the same retrieved chunks.*

---

## 🛠️ How It Works

```
PDFs → PyPDFLoader → Text Chunks (300 chars, 100 overlap)
                          ↓
                     ChromaDB (vector store with embeddings)
                          ↓
              User Query → Top 4 similar chunks retrieved
                          ↓
              Chunks injected into LLM system prompt
                          ↓
                     LLM generates grounded answer
```

---

## 📦 Dependencies

| Package | Purpose |
|---|---|
| `chromadb` | Vector database for storing/querying embeddings |
| `langchain` | PDF loading and text splitting |
| `pypdf` | PDF parsing |
| `openai` | OpenAI-compatible client (used for HuggingFace & OpenRouter) |
| `ollama` | Local model inference client |
| `python-dotenv` | Environment variable management |

---

## 🔒 API Keys

Never commit API keys to Git. Use a `.env` file:

```env
HUGGINGFACE_API_KEY=your_key_here
OPENROUTER_API_KEY=your_key_here
```

Add `.env` to your `.gitignore`:

```
.env
chroma-db/
.rag_env/
__pycache__/
```

---

## 📄 License

MIT License — free to use and modify.

