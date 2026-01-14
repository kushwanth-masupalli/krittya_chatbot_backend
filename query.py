from pinecone import Pinecone
import time

pc = Pinecone(api_key="pcsk_4o9kCn_UCiQQtp9DhCvVJeA2iGXVL7K3QmLgcRjcpfpLiFUy5DS7z1n8QxFdKzt3DQ53RB")

index_name = "krittay-vd"
index = pc.Index(index_name)

query = "what is krittya"

start_time = time.time()

results = index.search(
    namespace="example-namespace",
    query={
        "inputs": {"text": query},
        "top_k": 3
    }
)

end_time = time.time()

print(results)
print(f"Query execution time: {end_time - start_time:.4f} seconds")
