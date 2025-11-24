from fastapi import FastAPI

app = FastAPI()

from fastapi.templating import Jinja2Templates # fast api 템플릿 사용
from fastapi import Request # 외부 요청이기 때문에 파라미터로 들어감.
templates = Jinja2Templates(directory="templates/") # 클래스 변수(함수 담는 값) = Jinja 템플릿 html경로 설정

# admin.html
@app.get("/admin_html") # 네트워크용 함수 호출
async def main_html(request : Request): # 파일 호출
    return templates.TemplateResponse("admin.html", {"request" : request}) # html 파일 자체가 호출됨.

# http://localhost:8000/bakey_html
# bakery.html
@app.get("/bakery_html") 
async def main_html(request : Request): 
    return templates.TemplateResponse("bakery.html", {"request" : request})

# index.html
@app.get("/") 
async def main_html(request : Request): 
    return templates.TemplateResponse("index.html", {"request" : request})

pass