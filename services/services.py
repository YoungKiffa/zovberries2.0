from sqlalchemy.orm import Session
from models.tovar import *


class ZovService:
    def __init__(self, db: Session):
        self.db = db


    def add_tovar(self, tovar_name: str, tovar_status: str):
        try:
            new_tovar = Tovar(
                tovar_name=tovar_name,
                tovar_status=tovar_status
            )
            self.db.add(new_tovar)
            self.db.commit()
            self.db.refresh(new_tovar)
            print(f"Added Tovar: {new_tovar.tovar_name}")
        except Exception as e:
            print(e)
        return new_tovar

    def get_all_tovars(self):
        tovars = self.db.query(Tovar.tovar_id, Tovar.tovar_name, Tovar.tovar_status).all()
        return tovars

    def delete_tovar(self, tovar_id: int):
        tovar_to_delete = self.db.query(Tovar).get(tovar_id)

        if tovar_to_delete:
            self.db.delete(tovar_to_delete)
            self.db.commit()
            print(f"Deleted Tovar: {tovar_to_delete.tovar_id}")
        else:
            print("Tovar not found.")

    def update_data(self, tovar_id, tovar_name, tovar_status):
        tovar_updete = self.db.query(Tovar).filter(Tovar.tovar_id == tovar_id).first()
        tovar_updete.tovar_id = tovar_id
        tovar_updete.tovar_name = tovar_name
        tovar_updete.tovar_status = tovar_status
        self.db.commit()



