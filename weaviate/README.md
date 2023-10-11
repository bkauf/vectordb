

### Create an account on Weaviate Cloud
https://weaviate.io/developers/wcs/quickstart

### Install Client Library 

```sh
pip install weaviate-client
```

### Install Google API library
```sh
pip3 install google-cloud-aiplatform&gt;=1.25
```

### For local Development 
Create a [service account Key](https://cloud.google.com/iam/docs/keys-create-delete#creating) and store it's path in the envornmental variable
```sh
export GOOGLE_APPLICATION_CREDENTIALS='/path/to/service/account/keys.json'
```

###Enable the VertexAPI on your Project

[enable Vertex API](https://console.cloud.google.com/flows/enableapi?apiid=aiplatform.googleapis.com)

### Install the vertex library for Python
```sh
https://cloud.google.com/vertex-ai/docs/start/install-sdk
```