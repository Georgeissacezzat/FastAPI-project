from fastapi import  APIRouter , HTTPException
from typing import List
from fastapi import status , Depends
from sqlalchemy.orm import Session
from src.models import Contact
from src.database import get_db
from src.schemas import Create_contact , Edit_contact , Print_contact

Con = APIRouter()

@Con.get("/{id}")
async def get_contact(id : int , db: Session = Depends(get_db)):
    check_contact = db.query(Contact).filter(Contact.id == id).first()
    if check_contact:
        return {
            "Name" : check_contact.name , 
            "phone" : check_contact.phone
        }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")


@Con.get("/" , response_model=List[Print_contact])
async def get_all_contacts (db: Session = Depends(get_db)):
    contacts = (
        db.query(Contact)
        .all()
    )
    if contacts:
        return contacts
    raise HTTPException(status_code=404, detail="No contacts found")


@Con.post("/" ,status_code = status.HTTP_201_CREATED)
async def create_contact (contact : Create_contact , db: Session = Depends(get_db)):
    new_contact = Contact(name = contact.name , phone = contact.phone)
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)
    return {"message": "Contact created successfully", "contact_id": new_contact.id}


@Con.patch("/{id}")
async def edit_contact(id : int , contact : Edit_contact , db : Session = Depends(get_db)):
    check_contact = db.query(Contact).filter(Contact.id == id).first()

    if check_contact :
        if contact.name is not None :
            check_contact.name = contact.name
        if contact.phone is not None :
            check_contact.phone = contact.phone
        db.commit()
        db.refresh(check_contact)
        return {
            "Name" : check_contact.name ,
            "Phone" : check_contact.phone 
        }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")

@Con.delete("/{id}")
async def delete_contact (id : int , db : Session = Depends(get_db)):
    check_contact = db.query(Contact).filter(Contact.id == id).first()
    if check_contact :
        db.delete(check_contact)
        db.commit()
        return {}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")

