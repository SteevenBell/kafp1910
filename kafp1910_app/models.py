from . import db
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSONB


class FormData(db.Model):
    __tablename__ = "form_data"

    id = db.Column(db.Integer, primary_key=True, index=True)
    data = db.Column(JSONB)
    created = db.Column(db.DateTime(), default=datetime.now)

    def __repr__(self):
        return f"ID: {self.id}; DATA: {self.data}"
