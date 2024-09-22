import sqlalchemy as sa

from api.models.base import BaseTableModel

class Book(BaseTableModel):
    __tablename__ = 'books'
    
    title = sa.Column(sa.String, nullable=False)
    publisher = sa.Column(sa.String, nullable=False)
    category = sa.Column(sa.String, nullable=False)
    available = sa.Column(sa.Boolean, default=True)
    available_on = sa.Column(sa.DateTime(timezone=True), nullable=True)