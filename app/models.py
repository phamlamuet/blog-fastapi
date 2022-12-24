from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy import DateTime

from .database import Base

#feels like models are entities that mapped to db??

class Article(Base):
    __tablename__ = "article"

    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String,unique = True, index = True)
    title = Column(String)
    excerpt = Column(String)
    published_at = Column(String)
    url_thumbnail = Column(String)
    published_at = Column(DateTime, nullable=True)
    content = Column(String)

    category_id = Column(Integer,ForeignKey("category.id"))
  

class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String,unique = True)
  



