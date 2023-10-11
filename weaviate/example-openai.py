#!/usr/bin/env python3
import weaviate
import json
import dotenv
#dotenv.load_dotenv()


client = weaviate.Client(
    url = weaviteServer,  # Replace with your endpoint
    auth_client_secret=weaviate.AuthApiKey(api_key=apiKey),  # Replace w/ your Weaviate instance API key
    additional_headers = {
        "X-OpenAI-Api-Key": openAI  # Replace with your inference API key
    }
)

class_obj = {
    "class": "Question",
    "vectorizer": "text2vec-openai",  # If set to "none" you must always provide vectors yourself. Could be any other "text2vec-*" also.
    "moduleConfig": {
        "text2vec-openai": {},
        "generative-openai": {}  # Ensure the `generative-openai` module is used for generative queries
    }
}

client.schema.create_class(class_obj)


