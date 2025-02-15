from fastapi import FastAPI 
from src.routes import Con


app = FastAPI()

app.include_router(Con)