import uuid
from typing import Optional, Union
from pydantic import BaseModel, Field



class userInfo(BaseModel):
    id: str = Field(alias="_id")
    calories: dict= Field(...)
    rest_heart_rate: dict = Field(...)
    sleep_time: dict = Field(...)
    steps: dict = Field(...)

    class Config: 
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "c38a9c7225ed003a5b1297624b956254ffc6c906e3687a3c2a74ea9c9a717a6c",
                "calories": {
                    "10/1/2017": "2747",
                    "10/2/2017": "2502",
                    "10/3/2017": "2849",
                    "10/4/2017": "2297",
                    "10/5/2017": "2650",
                    "10/6/2017": "2503",
                    "10/7/2017": "3063"
                },
                "rest_heart_rate": {
                    "10/1/2017": "52",
                    "10/2/2017": "50", 
                    "10/3/2017": "51",
                    "10/4/2017": "53",
                    "10/5/2017": "55",
                    "10/6/2017": "57",
                    "10/7/2017": "58"
                },
                "sleep_time": {
                    "10/1/2017": "483",
                    "10/2/2017": "443",
                    "10/3/2017": "429",
                    "10/4/2017": "421",
                    "10/5/2017": "333",
                    "10/6/2017": "379",
                    "10/7/2017": "350"
                },
                "steps": {
                    "10/1/2017": "12578",
                    "10/2/2017": "8352",
                    "10/3/2017": "13299",
                    "10/4/2017": "6344",
                    "10/5/2017": "8347",
                    "10/6/2017": "6876",
                    "10/7/2017": "14591"
                }
            }
        }



class Book(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    title: str = Field(...)
    author: str = Field(...)
    synopsis: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "title": "Don Quixote",
                "author": "Miguel de Cervantes",
                "synopsis": "..."
            }
        }

class BookUpdate(BaseModel):
    title: Optional[str]
    author: Optional[str]
    synopsis: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "title": "Don Quixote",
                "author": "Miguel de Cervantes",
                "synopsis": "Don Quixote is a Spanish novel by Miguel de Cervantes..."
            }
        }