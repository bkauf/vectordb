#!/usr/bin/env python3

from google.cloud import aiplatform
# aiplatform.init(
#         project=project,
#         location=location,
#         experiment=experiment,
#         staging_bucket=staging_bucket,
#         credentials=credentials,
#         encryption_spec_key_name=encryption_spec_key_name,
#         service_account=service_account,
#     )




from vertexai.preview.language_models import TextEmbeddingModel
model = TextEmbeddingModel.from_pretrained("textembedding-gecko")
embeddings = model.get_embeddings(["Dinner in New York City"])
for embedding in embeddings:
  vector = embedding.values
  print(vector)