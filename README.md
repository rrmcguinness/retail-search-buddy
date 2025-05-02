<!--
 Copyright 2025 Google, LLC
 
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
 
     https://www.apache.org/licenses/LICENSE-2.0
 
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
-->
# Retail Search Buddy

This is an example application for understanding schema.org and retail search documentation.
The ultimate goal is to help Google Cloud customers to adopt Vertex AI Search for Commerce.

## Copy the third_party/pdfs to a GCS bucket
1. Log into the Google Cloud console.
1. Search for `Buckets`
1. Click on the `Buckets` link.
1. Click on `Create`, give your bucket a unique name and use the default settings. E.g. - 
1. Upload all of the PDF files 

## Create a Vertex AI RAG Engine Project and import files

1. Log into the Google Cloud Console.
1. Search for `RAG Engine`
1. Click on `Create Corpus`
1. Setup the bucket created above as the source.

## Project Setup

1. [Install UV](https://docs.astral.sh/uv/guides/install-python/)
1. [Create a .env file](#create-env-file)
1. [Create your virtual environment](#create-virtual-environment)
1. Activate your virtual environment `source .venv/bin/activate`
1. Resolve dependencies `uv sync`
1. Run the agent: `adk web` or `adk run retail_agent` to test the command line.

#### Example Prompts:

User: 'Show me an example product in json format from schema.org'
Agent: ...

User: attaches file, 'Can you use this CSV file to write a python program to generate valid schema.org products?'
Agent: ...

User: attaches pdf of output documentation template, 'Given this template can you map the field of the CSV file to the appropriate fields and provide an explanation of why you chose the mapping?`
Agent: ...

### Create Virtual Environment

From the project directory run the following command:

```shell
# Create the environment with a pip instance
uv venv --seed
# Activate the environment
source .venv/bin/activate
```

### Create Env File

Using your favorite text editor, create a `.env` file in the `retail_agent` directory.

#### ./retail_agent/.env
```yaml
GOOGLE_GENAI_USE_VERTEXAI="False"
GOOGLE_API_KEY="<YOUR API KEY HERE>"
VERTEX_RAG_CORPUS_NAME="<YOUR RAG MODEL NAME HERE>"
```