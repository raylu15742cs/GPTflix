import pinecone
import csv
import numpy as np
import os
from os.path import join, dirname
from dotenv import load_dotenv

class PineconeUpload:
    def __init__(
        self,
        pinecone_api_key,
        index_name,
        embeddings_csv,
        embedding_dims=1536,
        create_index=False,
    ) -> None:
        self.pinecone_api_key = pinecone_api_key
        self.index_name = index_name
        self.embeddings_csv = embeddings_csv
        self.embedding_dims = embedding_dims
        self.create_index = create_index
        self.pinecone_index = self.make_pinecone_index()

    def get_first_4000_chars(self, s):
        """Limit metadata character length to 4000."""
        if len(s) > 4000:
            return s[:4000]
        else:
            return s

    def make_pinecone_index(self):
        """Create the Pinecone index."""
        pinecone.init(api_key=self.pinecone_api_key, environment="asia-southeast1-gcp-free")

        if self.create_index:
            # Create an empty index if required
            pinecone.create_index(name=self.index_name, dimension=self.embedding_dims)

        index = pinecone.Index(self.index_name)

        # Get info about our new Pinecone index.
        print(f"Pinecone index info: {pinecone.whoami()} \n")
        return index

    def upsert_embeddings_batch(self, starting_index, data_batch, index_offset):
        """Upsert embeddings in batches."""
        # Convert the data to a list of Pinecone upsert requests
        upsert_requests = [
            (
                str(starting_index + i + index_offset),
                embedding,
                {"text": self.get_first_4000_chars(row[0])},
            )  # taking 1500 first characters because of meta size limit
            for i, row in enumerate(data_batch)
            for embedding in [np.array([float(x) for x in row[1:]]).tolist()]
        ]

        # Upsert the embeddings in batch
        upsert_response = self.pinecone_index.upsert(vectors=upsert_requests, append=True)
        return upsert_response

    def upsert_embeddings_to_index(self):
        # Load the data from the CSV file
        with open(self.embeddings_csv) as f:
            reader = csv.reader(f)
            next(reader)  # skip header row
            data = list(reader)

        # Get the current total number of vectors in the index
        current_vector_count = self.pinecone_index.describe_index_stats().get('total_vector_count', 0)

        # Upsert the embeddings in batches
        batch_size = 100
        index_offset = 0
        while index_offset < len(data):
            batch = data[index_offset: index_offset + batch_size]

            # Append vectors to index using the current vector count as the starting index
            self.upsert_embeddings_batch(current_vector_count, batch, index_offset)
            print("batch " + str(index_offset))

            # Increment the offset by the batch size and update the current vector count
            index_offset += batch_size
            current_vector_count += len(batch)

        print(f"Total vectors in the index: {self.pinecone_index.describe_index_stats().get('total_vector_count', 0)}")


if __name__ == "__main__":
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    # Define the name of the index and the dimensionality of the embeddings
    index_name = "1kmovies"
    embeddings_csv = "data_sample/playerd4.embeddings_maker_results.csv"
    embedding_dims = 1536
    create_index = False

    pinecone = PineconeUpload(
        pinecone_api_key=os.getenv("PINECONE_API_KEY"),
        index_name=index_name,
        embeddings_csv=embeddings_csv,
        embedding_dims=embedding_dims,
        create_index=create_index,
    )

    pinecone.upsert_embeddings_to_index()
