#!/usr/bin/env python3
import weaviate, json, os, requests
import dotenv

dotenv.load_dotenv()

# Now, you can access environment variables like this:

token = 'replace text'

client = weaviate.Client(
    url = os.getenv("URL"),  # Replace with your endpoint
    auth_client_secret=weaviate.AuthApiKey(api_key=os.getenv("KEY")),  # Replace w/ your Weaviate instance API key
    additional_headers = {
        "X-Palm-Api-Key": token  # Replace with your inference API key
    }
)
class_obj = {
    "class": "Question2",
    "vectorizer": "text2vec-palm",  # If set to "none" you must always provide vectors yourself. Could be any other "text2vec-*" also.
    "moduleConfig": {
        "text2vec-palm,": {
            "apiEndpoint": "https://us-central1-aiplatform.googleapis.com",
            "modelId": "textembedding-gecko@001",
            "projectId": "anthos-multi-cloud-335819",
            "vectorizeClassName": "true",
        },
        "generative-openai": {}  # Ensure the `generative-openai` module is used for generative queries
    }
}

client.schema.create_class(class_obj)


resp = requests.get('https://raw.githubusercontent.com/weaviate-tutorials/quickstart/main/data/jeopardy_tiny.json')
data = json.loads(resp.text)  # Load data

client.batch.configure(batch_size=100)  # Configure batch
with client.batch as batch:  # Initialize a batch process
    for i, d in enumerate(data):  # Batch import data
        print(f"importing question: {i+1}")
        properties = {
            "answer": d["Answer"],
            "question": d["Question"],
            "category": d["Category"],
        }
        batch.add_data_object(
            data_object=properties,
            class_name="Question2"
        )