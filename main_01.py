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

# http://localhost:8000/main_html
@app.get("/main_html") # 네트워크용 함수 호출
async def main_html(request : Request): # 파일 호출
    return templates.TemplateResponse("main.html"   
                                      , {"request" : request}) # html 파일 자체가 호출됨.


pass

