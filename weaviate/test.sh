MODEL_ID="textembedding-gecko"
PROJECT_ID='anthos-multi-cloud-335819'

   curl \
    -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    https://us-central1-aiplatform.googleapis.com/v1/projects/${PROJECT_ID}/locations/us-central1/publishers/google/models/${MODEL_ID?}:predict -d \
    $'{
      "instances": [
        { "content": "life?"}
      ],
    }'

export ENABLE_MODULES='textembedding-gecko@001'