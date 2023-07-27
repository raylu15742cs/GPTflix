import pinecone
import os
index_name = "1kmovies"
pinecone.init(api_key=os.getenv("PINECONE_API_KEY"),environment="us-west1-gcp-free")

index = pinecone.Index(index_name)

index.delete(delete_all=True)

# clear index delete_response = index.delete(delete_all=True)

