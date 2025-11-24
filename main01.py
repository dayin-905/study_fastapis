from fastapi import FastAPI

app = FastAPI()

from fastapi.templating import Jinja2Templates # fast api 템플릿 사용
from fastapi import Request # 외부 요청이기 때문에 파라미터로 들어감.
templates = Jinja2Templates(directory="toyprojects_fastapis/") # 클래스 변수(함수 담는 값) = Jinja 템플릿 html경로 설정

# http://localhost:8000/index_html
@app.get("/index_html") 
async def index_html(request : Request): 
    return templates.TemplateResponse("index.html", {"request" : request})

# http://localhost:8000/admin_html
@app.get("/admin_html") # 네트워크용 함수 호출
async def admin_html(request : Request): # 파일 호출
    return templates.TemplateResponse("admin.html", {"request" : request}) # html 파일 자체가 호출됨.

# http://localhost:8000/bakey_html
@app.get("/bakery_html") 
async def bakery_html(request : Request): 
    return templates.TemplateResponse("bakery.html", {"request" : request})
                                      