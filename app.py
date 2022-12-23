from fastapi.params import Form
from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from markupsafe import re
import starlette.status as status
from starlette.responses import RedirectResponse, Response  
from dbcontroller import DBController

app = FastAPI()

app.mount("/static",StaticFiles(directory="static"),"static")

templates = Jinja2Templates("templates")

db = DBController("app.db")


@app.get("/", response_class=HTMLResponse)
def index(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})

@app.post("/",response_class=HTMLResponse)
def index_post(request:Request, email:str = Form(...), password:str=Form(...)):
    row = db.executeQueryWithParams("select * from users where email = ? and password = ?",[email,password])
    if(len(row)==0):
        return templates.TemplateResponse("index.html",{"request":request, "msg":"invalid email and password" })
    return RedirectResponse("/",status_code=status.HTTP_302_FOUND)

@app.get("/create", response_class=HTMLResponse)
def create(request:Request):
    return templates.TemplateResponse("create.html",{"request":request})

@app.post("/create",response_class=HTMLResponse)
def create_post(request:Request, username:str = Form(...),password:str=Form(...),email:str = Form(...), phone:str=Form(...)):
    data = {"username":username,"password":password,"email":email,"phone":phone}
    if(db.insert("users",data=data)):
        return templates.TemplateResponse("create.html",{"request":request,"msg":"Account created successfully"})
    return templates.TemplateResponse("create.html",{"request":request,"msg":"Unable to create account"})