from pydantic import BaseModel
from typing import Optional


class Create_contact(BaseModel):
    name : str 
    phone : str

class Print_contact(BaseModel):
    id : int
    name : str
    phone : str 

class Edit_contact(BaseModel):
    name : Optional[str] = None
    phone : Optional[str] = None