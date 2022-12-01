from fastapi import APIRouter, Body, Request, Response, HTTPException, status, Form
from fastapi.encoders import jsonable_encoder
from models import userInfo
from fernet import fernet_key
from dotenv import dotenv_values

router = APIRouter()


@router.post("/", response_description="upate daily actively", status_code=status.HTTP_201_CREATED, response_model=userInfo)
def update_info(request: Request, user: userInfo = Body(...)):
    user = jsonable_encoder(user)
    key = dotenv_values(".env")["FERNET_KEY"]
    fernet_key.encrpyt(user["calories"], key)
    fernet_key.encrpyt(user["rest_heart_rate"], key)
    fernet_key.encrpyt(user["sleep_time"], key)
    fernet_key.encrpyt(user["steps"], key)
    new_user = request.app.database["HealthData"].insert_one(user)
    created_user = request.app.database["HealthData"].find_one(
        {"_id": new_user.inserted_id}
    )
    return


