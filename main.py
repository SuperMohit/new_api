from typing import Union
from fastapi import FastAPI
from news_cron import fetch_and_save

app = FastAPI()


@app.get("/")
async def read_root():
    return {"version": "v1"}


@app.get("/v1/news/cron")
async def read_item():
    fetch_and_save()