from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates # html형식과 변수를 합해주는 프레임 워크

router = APIRouter()

# 템플릿 호출
templates = Jinja2Templates(directory="templates/")

# http://loaclhost:8000/todos/
def get_todos_html(request : Request) :
    context = {
        "request" : request
    }
    return templates.TemplateResponse("todos/merged_todo.html", context)