from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.models.qa_model import QAModel

app = FastAPI()

# Mount the static files (CSS)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Load templates
templates = Jinja2Templates(directory="app/templates")

# Initialize the Question Answering model
qa_model = QAModel()

@app.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "answer": None})

@app.post("/", response_class=HTMLResponse)
async def post_question(
    request: Request,
    question: str = Form(...),
    context: str = Form(...)
):
    # Use the model to get an answer
    answer = qa_model.answer_question(question, context)
    return templates.TemplateResponse("index.html", {"request": request, "answer": answer})
