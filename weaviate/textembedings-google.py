#!/usr/bin/env python3

from vertexai.language_models import TextEmbeddingModel

def text_embedding() -> list:
    """Text embedding with a Large Language Model."""
    model = TextEmbeddingModel.from_pretrained("textembedding-gecko@001")
    embeddings = model.get_embeddings(["What is life?"])
    for embedding in embeddings:
        vector = embedding.values
       # print(f"Length of Embedding Vector: {len(vector)}")
        print(vector)
    return vector


if __name__ == "__main__":
    text_embedding()