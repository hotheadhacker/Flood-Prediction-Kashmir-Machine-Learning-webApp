from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Optional
from sklearn.linear_model import LogisticRegression
import pickle

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")






@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})
    
@app.get("/run-prediction", response_class=HTMLResponse)
async def read_item(request: Request):
    dummy = "hello i am dummy logic!"
    # print(jan)
    return templates.TemplateResponse("run-predict.html", {"request": request})

@app.get("/test/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("home.html", {"request": request, "id": id})

@app.get("/engine", response_class=HTMLResponse)
async def read_item(request: Request):
    year = int(request.query_params["year"])
    
    if(request.query_params["jan"]):
        jan = float(request.query_params["jan"])
    if(request.query_params["feb"]):
        feb = float(request.query_params["feb"])
    if(request.query_params["mar"]):
        mar = float(request.query_params["mar"])
    if(request.query_params["april"]):
        april = float(request.query_params["april"])
    if(request.query_params["may"]):
        may = float(request.query_params["may"])
    if(request.query_params["june"]):
        june = float(request.query_params["june"])
    if(request.query_params["jul"]):
        jul = float(request.query_params["jul"])
    if(request.query_params["aug"]):
        aug = float(request.query_params["aug"])
    if(request.query_params["sept"]):
        sept = float(request.query_params["sept"])
    if(request.query_params["oct"]):
        oct = float(request.query_params["oct"])
    if(request.query_params["nov"]):
        nov = float(request.query_params["nov"])
    if(request.query_params["dec"]):
        dec = float(request.query_params["dec"])

    annual = jan + feb + mar + april + may + june + jul + aug + sept + oct + nov + dec
    JF = jan + feb
    MAM = mar + april + may
    JJAS = june + jul + aug + sept
    OND = oct + nov + dec

    # load the trained modal
    loaded_model = pickle.load(open('../saved-models/modelSavedV2.sav', 'rb'))
    finalOP = loaded_model.predict([[year,jan,feb,mar,april,may,june,jul,aug,sept,oct,nov,dec,annual,JF,MAM,JJAS,OND]])
    print(finalOP)
    
    # print("Prams: "+str(request.query_params["year"]))
    return templates.TemplateResponse("engine.html", {"request": request, "result": finalOP[0]})
    