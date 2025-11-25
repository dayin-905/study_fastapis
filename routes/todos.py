from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates # html형식과 변수를 합해주는 프레임 워크
from services.db import get_db_connection
from psycopg2.extras import DictCursor # postgre 연결, cursor_factory

router = APIRouter()

# 템플릿 호출
templates = Jinja2Templates(directory="templates/")

# http://localhost:8000/todos/
@router.get("/{todo_id}")
def get_todo(request : Request, todo_id : str):
    conn = get_db_connection() # DB 연결 테스트 통로
    with conn.cursor(cursor_factory=DictCursor) as cursor:
        cursor.execute(f"""SELECT id, item
                        FROM todo
                        WHERE id = '{todo_id}';""")
        todo = cursor.fetchone() # 결과를 하나만 가져옴.
    conn.close()

    context = {
        "request" : request,
        "todo" : todo
    }
    return templates.TemplateResponse("todos/merged_todo.html", context)

# http://localhost:8000/todos/
@router.get("/")
def get_todos_html(request : Request) :
    conn = get_db_connection() # DB 연결 테스트 통로
    with conn.cursor(cursor_factory=DictCursor) as cursor:
        cursor.execute("""SELECT id, item FROM todo;""")
        todos = cursor.fetchall()
    conn.close()

    context = {
        "request" : request,
        "todos" : todos # cursor_factory를 해줘서 dict 형식으로 바뀜
    }
    return templates.TemplateResponse("todos/merged_todo.html", context)

