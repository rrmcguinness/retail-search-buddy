# Copyright 2025 Google, LLC
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     https://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from vertexai import rag
from dotenv import load_dotenv

load_dotenv()

CORPUS_NAME = os.getenv("VERTEX_RAG_CORPUS_NAME")

rag_retrieval_config=rag.RagRetrievalConfig(
    top_k=3,  # Optional
    filter=rag.Filter(vector_distance_threshold=0.5)  # Optional
)

default_corpus = None

for corpus in rag.list_corpora():
    if corpus.display_name == CORPUS_NAME:
        default_corpus = corpus
        break


assert default_corpus is not None

def get_corpus_info(query: str) -> str:
    """Retrieves information about schema.org schemas and Google retail search.
    Args:
        query: The query to search for.
    Returns:
        The answer to the query.
    """
    response = rag.retrieval_query(
        rag_resources=[
            rag.RagResource(
                rag_corpus=default_corpus.name,
                # Optional: supply IDs from `rag.list_files()`.
                # rag_file_ids=["rag-file-1", "rag-file-2", ...],
            )
        ],
        text="Explain the product schema",
        rag_retrieval_config=rag_retrieval_config,
    )
    output = ""
    for ctx in response.contexts.contexts:
        output += ctx.text + "\n"
    
    return output
