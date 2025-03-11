from sqlalchemy import Column, Integer, String
from database import Base



class Tovar(Base):
    __tablename__ = 'Tovars'

    tovar_id = Column(Integer, primary_key=True, index=True)
    tovar_name = Column(String, nullable=True)
    tovar_status = Column(String)