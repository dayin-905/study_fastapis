from fastapi import FastAPI

app = FastAPI() # app은 함수를 호출하는 클래스라는 뜻의 문장.
#웹사이트 구성하는 여러가지 함수가 들어간 클래스

# http://localhost:8000/
@app.get("/") # URL의 /가 클라이언트 호출
async def root():
    return {"message" : "Hello, World!"}

# http://localhost:8000/html
@app.get("/html")
async def root_html():
    html_content = '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <div>My name is Lia</div>
        </body>
        </html>
        '''
    return html_content

from fastapi.templating import Jinja2Templates # fast api 템플릿 사용
from fastapi import Request # 외부 요청이기 때문에 파라미터로 들어감.
templates = Jinja2Templates(directory="templates/") # 클래스 변수(함수 담는 값) = Jinja 템플릿 html경로 설정

# Toyprojects(한 메인파일에서 디렉토리 설정하는 방법을 모르겠음.)
# http://localhost:8000/toyproject_fastapis/index_html
@app.get("/toyproject_fastapis/index_html") 
async def index_html(request : Request): 
    return templates.TemplateResponse("toyproject_fastapis/index.html", {"request" : request})

# http://localhost:8000/toyproject_fastapis/admin_html
@app.get("/toyproject_fastapis/admin_html") # 네트워크용 함수 호출
async def admin_html(request : Request): # 파일 호출
    return templates.TemplateResponse("toyproject_fastapis/admin.html", {"request" : request}) # html 파일 자체가 호출됨.

# http://localhost:8000/toyproject_fastapis/bakery_html
@app.get("/toyproject_fastapis/bakery_html") 
async def bakery_html(request : Request): 
    return templates.TemplateResponse("toyproject_fastapis/bakery.html", {"request" : request})

# http://localhost:8000/main_html_context
@app.get("/toyproject_fastapis/main_html_context") # 네트워크용 함수 호출
async def main_html_context(request : Request): # 파일 호출
    # 템플릿에 전달할 데이터
    context = {
        "request": request,
        "title": "FastAPI + Jinja Example",
        "items": ["Apple", "Banana", "Cherry"],
        "user": {"name": "Sanghun", "age": 33}
    }
    return templates.TemplateResponse("main_context.html", context) # html 파일 자체가 호출됨.

# http://localhost:8000/users/list
@app.get("/users/list")
async def user_list(request : Request):
    users = [
    {"name": "Alice", "age": 25, "city": "Seoul"},
    {"name": "Bob", "age": 30, "city": "Busan"},
    {"name": "Charlie", "age": 28, "city": "Daegu"}
    ]

    context = {
        "request" : request
        , "user_list" : users
    }
    return templates.TemplateResponse( "users/list.html", context)
# 리턴 값 위치와 get 호출 url를 같은 걸로 만들지 않음.

# http://localhost:8000/quests/10_jina2
@app.get("/quests/10_jina2")
async def quest_10_jina2(request: Request):
    return templates.TemplateResponse("quests/10_jina2.html", {"request" : request})

# http://localhost:8000/board/detail_json?title=Third%20Post&content=This%20is%20the%20third%20post.
@app.get("/board/detail_json")
async def board_details_json(request : Request) :
    # request.method
    # request.query_params
    params = dict(request.query_params)

    # return {"title" : "Third Post", "content" : "This is the third post."}
    return {"title" : params['title'], "content" : params['content']}

# http://localhost:8000/board/detail_json?title=Third%20Post&content=This%20is%20the%20third%20post.
@app.post("/board/detail_post_json")
async def board_details_post_json(request : Request) : # request = Requset()
    # request.method
    # request.query_params
    params = dict(await request.form())

    # return {"title" : "Third Post", "content" : "This is the third post."}
    return {"title" : params['title'], "content" : params['content']}

# http://localhost:8000/board/detail_post_html
@app.get("/board/detail_post_html") # 네트워크용 함수 호출
async def main_html(request : Request): # 파일 호출
    return templates.TemplateResponse("board/detail.html", {"request" : request})

# http://localhost:8000/board/detail_html/{detail_id}
@app.get("/board/detail_html/{detail_id}") # 네트워크용 함수 호출
async def main_html(request : Request, detail_id): # 파일 호출
    return templates.TemplateResponse("board/detail.html", {"request" : request})

# 정적 파일 설정
from fastapi.staticfiles import StaticFiles
# http://localhost:8000/images/temp.jpg
app.mount("/images", StaticFiles(directory="resources/images"))
# http://localhost:8000/css/commons.css
app.mount("/css", StaticFiles(directory="resources/css"))

pass

