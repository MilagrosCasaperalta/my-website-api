from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# CORS setup so your React app can talk to this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}


class Project(BaseModel):
        id: int
        title: str
        description: str
        link: str


#testing 

temp_projects = [
       {
        "id": 1,
        "title": "Personal Website",
        "description": "I built my personal website as a way to showcase my skills, projects, "
        "and journey as a developer. While it currently serves as a portfolio, I "
        "intentionally designed it to be expandable.",
        "link": "https://milagroscasaperalta.com",
       }
]


@app.get("/projects", response_model =List[Project])

def get_projects():
    return temp_projects