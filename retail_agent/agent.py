# import vertexai
from google.adk.agents import LlmAgent, SequentialAgent, Agent
from .rag_tool import get_corpus_info

# vertexai.init(
#     project="PROJECT_ID",
#     location="LOCATION",
#     staging_bucket="gs://BUCKET_NAME",
# )

# Creates RAG grounded agent for answering questions about retail search and schema.org schemas.
schema_org_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="retail_search_agent",
    description="""An agent specializing in schema.org schemas and retail search requirements.""",
    global_instruction="Answer questions pertaining to schema.org and/or retail search also known as Vertex Search for Commerce.",
    tools=[get_corpus_info],
    output_key='rag_result'
)

# Creates an agent specializing in coding tasks using the output
# from the schema_org_agent to drive the specification
code_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="code_agent",
    description="""An agent specializing in writing json, python, go, or Java code for converting CSV formats using web service integration points for retail search.""",
    instruction="If the user has asked to generate code, use the rag_results to inform your response as the specification for the program or JSON output.",
)

# Creates the sequence of agents
pipeline_agent = SequentialAgent(
    name="ProcessPipeline",
    sub_agents=[
        schema_org_agent,
        code_agent,
    ]
)

# Exposes the primary agent as a router to the pipeline.
# Note, if my agent had a distinct purpose I would not put it
# into a pipeline.
root_agent = Agent(
    model="gemini-2.0-flash",
    name="retail_agent",
    instruction="You are a helpful agent solving retail search and schema.org problems.",
    description="""An agent specializing in schema.org schemas and retail search requirements and generating code to help implement retail search.""",
    sub_agents=[pipeline_agent]
)
