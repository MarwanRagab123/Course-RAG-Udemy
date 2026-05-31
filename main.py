from sentence_transformers import SentenceTransformer
import chromadb
import os

# =====================
# INIT MODEL
# =====================
model = SentenceTransformer("all-MiniLM-L6-v2")

# =====================
# INIT VECTOR DB
# =====================
client = chromadb.Client()
collection = client.create_collection("demo_search")

print("✅ System Initialized")

# =====================
# LOAD FILES
# =====================
def load_files(folder):
    docs = []

    for file in os.listdir(folder):
        if file.endswith(".txt"):
            path = os.path.join(folder, file)

            with open(path, "r", encoding="utf-8") as f:
                text = f.read()
                docs.append((file, text))

    return docs


files = load_files("demo_files")
print("📂 Loaded files:", len(files))

# =====================
# INDEX FILES
# =====================
def index_files(files):
    for i, (name, text) in enumerate(files):

        embedding = model.encode(text).tolist()

        collection.add(
            documents=[text],
            embeddings=[embedding],
            ids=[str(i)],
            metadatas=[{"file": name}]
        )

    print("✅ Indexing Done")


index_files(files)

# =====================
# SEARCH
# =====================
def search(query):
    query_vec = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_vec],
        n_results=3
    )

    print("\n🔍 Results:\n")

    for i in range(len(results["documents"][0])):
        print("📄 File:", results["metadatas"][0][i]["file"])
        print(results["documents"][0][i])
        print("-" * 40)



while True:
    q = input("\n🔎 Enter search query: ")
    search(q)