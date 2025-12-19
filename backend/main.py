from fastapi import FastAPI
from api.repo import router as repo_router

app = FastAPI()

app.include_router(repo_router)
