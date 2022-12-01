from fastapi import FastAPI, Request, Form, HTTPException, APIRouter
from fastapi import FastAPI, Form
from dotenv import dotenv_values
from pymongo import MongoClient
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from hashlib import sha256
from graph import plotting
# from routes import router as book_router
from paths import router
from fernet import fernet_key

config = dotenv_values(".env")
if not config["FERNET_KEY"] !="":
    fernet_key.generate_key()
# else:
#     print(config["FERNET_KEY"])
    # fernet_key.generate_key()

app = FastAPI()
app.mount("/index", StaticFiles(directory="frontend", html = True), name="main")


@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["ATLAS_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]
    print("Connected to the MongoDB database!")

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()


def generate_html_response(info):
    key = config["FERNET_KEY"]
    plot = plotting(info, key)
    plot.plot_calories()
    plot.plot_heart_rate()
    plot.plot_sleep_time()
    plot.plot_steps()
    html_content = """
    <html lang="en">
    <head>
        <title>Activies</title>
        <!-- <link href="style.css"  type="text/css" rel="stylesheet" /> -->
    </head>
  
    <body>
        <div class="chart">
            <h2>calorie intake</h2>
            <img src="/calories.png" alt="calories" />
        </div>
        <div class="chart">
            <h2>Average Resting Heart Rate</h2>
            <img src="/heart_rate.png" alt="resting heart rate" />
        </div>
        <div class="chart">
            <h2>Steeps </h2>
            <img src="/steps.png" alt="resting heart rate" />
        </div>
        <div class="chart">
            <h2>Sleep time</h2>
            <img src="/sleep_time.png" alt="resting heart rate" />
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code = 200)

@app.post("/login", response_class=HTMLResponse)
def login(request: Request, uname: str = Form(...), psw: str = Form(...)):
    uid = sha256((uname + psw).encode()).hexdigest()
    # print("uid: ", uid)
    if(user := request.app.database["HealthData"].find_one({"_id": uid})) is not None: 
        return generate_html_response(user)
    raise HTTPException(status_code=404, detail=f"user ' {uname} 'not found")

@app.get("/login/", response_class=HTMLResponse)
def login(request: Request, uname: str, psw: str):
    uid = sha256((uname + psw).encode()).hexdigest()
    # print("uid: ", uid)
    if(user := request.app.database["HealthData"].find_one({"_id": uid})) is not None: 
        return generate_html_response(user)
    raise HTTPException(status_code=404, detail=f"user ' {uname} 'not found")

@app.get("/calories.png")
def getImage():
    return FileResponse(config["ROOT_PATH"]+"/dataVisuals/calories.png")


@app.get("/heart_rate.png")
def getImage():
    return FileResponse(config["ROOT_PATH"]+"/dataVisuals/heart_rate.png")

@app.get("/sleep_time.png")
def getImage():
    return FileResponse(config["ROOT_PATH"]+"/dataVisuals/sleep_time.png")

@app.get("/steps.png")
def getImage():
    return FileResponse(config["ROOT_PATH"]+"/dataVisuals/steps.png")


app.include_router(router, tags=["Sensor"], prefix="/HealthData")

