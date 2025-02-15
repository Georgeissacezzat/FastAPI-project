from src.database import Base , engine
from sqlalchemy import Column, Integer, String


class Contact(Base):
    __tablename__ = 'contacts'  
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False) 

Base.metadata.create_all(engine)