Required Packages to be imported in the app.py

from ast import For
from typing_extensions import Required
from fastapi import FastAPI, Request
from fastapi.params import Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import starlette.status as status
from starlette.responses import RedirectResponse, Response  

Install libraries

pip install jinja2
pip install python-multipart 

python -m pip install jinja2

python -m uvicorn app:app

db = DBcontroller("app.db")

q = "select * from users"
data = db.executeQuery(q)

q = "select * from users where username = ? and password = ?"
data = db.executeQuery(q,["madhu","12345"])

result = db.insert("users",{"username":"madhu","password":"12345"})
