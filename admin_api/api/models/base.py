""" This is the Base Model Class
"""
from uuid import uuid4
from fastapi import Depends
from db.database import Base
from sqlalchemy import (
    Column,
    String,
    DateTime,
    func
)

class BaseTableModel(Base):
    """This model creates helper methods for all models"""

    __abstract__ = True

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid4()))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    def to_dict(self):
        """returns a dictionary representation of the instance"""
        obj_dict = self.__dict__.copy()
        del obj_dict["_sa_instance_state"]
        obj_dict["id"] = self.id
        if self.created_at:
            obj_dict["created_at"] = self.created_at.isoformat()
        if self.updated_at:
            obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
