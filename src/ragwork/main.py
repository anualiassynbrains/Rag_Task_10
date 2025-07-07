# main.py
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from rag.graphqlschema import Query # you defined above
import strawberry
import os
import warnings

# Setup environment before imports
os.environ["TRANSFORMERS_NO_TF"] = "1"
os.environ["USE_TF"] = "0"

# Suppress warnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", message=".*np.object.*")



schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
