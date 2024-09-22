import sqlalchemy as sa
from sqlalchemy.orm import relationship

from api.models.base import BaseTableModel

class User(BaseTableModel):
    __tablename__ = 'users'
    
    email = sa.Column(sa.String, unique=True, index=True, nullable=False)
    first_name = sa.Column(sa.String, nullable=False)
    last_name = sa.Column(sa.String, nullable=False)

    borrowed_books = relationship("BorrowedBook", back_populates="user")
    