import os

import openai
import uvicorn
from dotenv import load_dotenv
# from flask import Flask, redirect, render_template, request, session, url_for
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from models.bloom import initialize_index

load_dotenv()
app = FastAPI()
app.secret_key = os.environ.get('SECRET_KEY', 'my-secret-key')
openai.api_key = os.environ.get("OPENAI_API_KEY")

# mounts the static folder that contains the css file
app.mount("/static", StaticFiles(directory="static", html=True), name="static")

# locates the template files that will be modified at run time
# with the dialog form the user and bot
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse('chat.html', {"request": request})

@app.get("/chat")
async def chat(input: str):
    bot_reply = index.query(input)
    return {"bot_reply": bot_reply}

if __name__ == "__main__":
    index = initialize_index("index.json")
    uvicorn.run("main:app", reload=True)
