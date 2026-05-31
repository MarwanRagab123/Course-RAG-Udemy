
# Retrieval-Augmented Generation (RAG)

Comprehensive collection of notebooks and assets used in a hands-on RAG course covering data ingestion, vector embeddings, vector databases, chunking strategies, hybrid search and multimodal examples.

**Contents**
- **Overview:** Practical, notebook-driven learning path for building RAG systems.
- **Notebooks & Code:** Step-by-step labs for data parsing, embedding generation, vector DBs (Chroma, FAISS), chunking, hybrid search and multimodal pipelines.
- **Data & Demos:** Sample text, JSON, and demo documents used by the notebooks.

**Repository Structure**
- [0-DataIngesionParsing](0-DataIngesionParsing): Notebooks for extracting and parsing documents (PDF, DPC, JSON, DB).
- [1-VectorEmbeddingAndDatabase](1-VectorEmbeddingAndDatabase): Embedding creation examples and experiments.
- [2-Vectordatabase](2-Vectordatabase): Working with Chroma and FAISS, plus saved DB files.
- [3-Advanced chunking](3-Advanced%20chunking): Chunking strategies and examples.
- [4-Hybrid_search](4-Hybrid_search): Hybrid/sparse-dense retrieval and reranking demos.
- [6-multimodal](6-multimodal): Multimodal notebook examples (text + images/audio if included).
- [demo_files](demo_files): Small demo documents used for quick testing.
- `main.py`: Minimal runner or entrypoint (if present).
- `requirements.txt` / `pyproject.toml`: Python dependencies for the course.

**Getting Started**

1. Prerequisites

- Python 3.10+ recommended
- Basic familiarity with Jupyter notebooks, Python, and machine learning concepts

2. Create and activate virtual environment

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Open notebooks

Launch Jupyter Lab/Notebook and open the notebooks in the folders listed above.

```bash
jupyter lab
```

**Notebooks Overview (quick guide)**
- [0-DataIngesionParsing](0-DataIngesionParsing): Parse structured and unstructured sources into plain text — includes `company_data.json`, `events.jsonl` and example text files.
- [1-VectorEmbeddingAndDatabase](1-VectorEmbeddingAndDatabase): Demonstrates embedding models and saving vectors for downstream retrieval.
- [2-Vectordatabase](2-Vectordatabase): Shows how to index vectors into Chroma and FAISS and how to query them; includes `chroma_db/chroma.sqlite3` and a FAISS index.
- [3-Advanced chunking](3-Advanced%20chunking): Strategies for semantic chunking to improve retrieval relevance.
- [4-Hybrid_search](4-Hybrid_search): Combines sparse and dense retrieval and covers reranking techniques.
- [6-multimodal](6-multimodal): Experiments mixing modalities for retrieval and retrieval-augmented generation.

**Common Workflows**
- Build a vector store: run the embedding notebook to produce embeddings and persist to a DB in [2-Vectordatabase](2-Vectordatabase).
- Query + RAG: load the vector DB, run retrieval, and pass retrieved context to a generative model for answer synthesis (see hybrid search and reranking notebooks).

**Tips & Notes**
- Notebooks are intentionally educational: they show intermediate outputs and exploration steps. For production, extract the core logic into Python modules and add tests.
- If you add large datasets or model files, avoid committing them to the repo. Use `.gitignore` and provide pointers to download scripts if needed.

**Demo files and data**
- Example demo documents are in [demo_files](demo_files) and sample data in `0-DataIngesionParsing/data/`.

**Contributing**
- Make incremental changes in new branches and open PRs. Prefer small, focused commits and include a short description of notebook changes.

**License & Attribution**
- Use these materials for learning and experimentation. If you reuse content publicly, please attribute the original course materials.



