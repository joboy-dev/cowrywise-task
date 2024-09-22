import sqlalchemy as sa
from sqlalchemy.orm import relationship

from api.models.base import BaseTableModel

class Book(BaseTableModel):
    __tablename__ = 'books'
    
    title = sa.Column(sa.String, nullable=False)
    publisher = sa.Column(sa.String, nullable=False)
    category = sa.Column(sa.String, nullable=False)
    available = sa.Column(sa.Boolean, default=True)
    available_on = sa.Column(sa.DateTime(timezone=True), nullable=True)


class BorrowedBook(BaseTableModel):
    __tablename__ = 'borrowed_books'
    
    user_id = sa.Column(sa.String, sa.ForeignKey("users.id"))
    book_id = sa.Column(sa.String, sa.ForeignKey("books.id"))
    borrowed_until = sa.Column(sa.DateTime(timezone=True), nullable=False)
    
    user = relationship("User", back_populates="borrowed_books")
    book = relationship("Book")
