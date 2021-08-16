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
    # year = int(request.query_params["year"])
    
    if(request.query_params["jan"]):
        jan = float(request.query_params["jan"])
    else:
        jan = 66.9
    if(request.query_params["feb"]):
        feb = float(request.query_params["feb"])
    else:
        feb = 74.9
    if(request.query_params["mar"]):
        mar = float(request.query_params["mar"])
    else:
        mar = 83.8
    if(request.query_params["april"]):
        april = float(request.query_params["april"])
    else:
        april = 60.3
    if(request.query_params["may"]):
        may = float(request.query_params["may"])
    else:
        may = 45.6
    if(request.query_params["june"]):
        june = float(request.query_params["june"])
    else:
        june = 44.9
    if(request.query_params["jul"]):
        jul = float(request.query_params["jul"])
    else:
        jul = 111.7
    if(request.query_params["aug"]):
        aug = float(request.query_params["aug"])
    else:
        aug = 112.6
    if(request.query_params["sept"]):
        sept = float(request.query_params["sept"])
    else:
        sept = 57.5
    if(request.query_params["oct"]):
        oct = float(request.query_params["oct"])
    else:
        oct = 26.2
    if(request.query_params["nov"]):
        nov = float(request.query_params["nov"])
    else:
        nov = 17.2
    if(request.query_params["dec"]):
        dec = float(request.query_params["dec"])
    else:
        dec = 37.2

    annual = jan + feb + mar + april + may + june + jul + aug + sept + oct + nov + dec
    JF = jan + feb
    MAM = mar + april + may
    JJAS = june + jul + aug + sept
    OND = oct + nov + dec

    # load the trained modal
    loaded_model = pickle.load(open('../saved-models/modelSaved_refinedV1.sav', 'rb'))
    finalOP = loaded_model.predict([[jan,feb,mar,april,may,june,jul,aug,sept,oct,nov,dec,annual,JF,MAM,JJAS,OND]])
    print(finalOP)
    prid = loaded_model.predict_proba([[jan,feb,mar,april,may,june,jul,aug,sept,oct,nov,dec,annual,JF,MAM,JJAS,OND]])
    print(prid)
    print(format(prid[0][1], '.3f'))
    prediction = format(prid[0][1], '.3f')
    
    # print("Prams: "+str(request.query_params["year"]))
    return templates.TemplateResponse("engine.html", {"request": request, "result": finalOP[0], "prediction": prediction})
    