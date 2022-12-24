from pydantic import BaseModel
from typing import Optional
from datetime import datetime
# pydantic models somehow look like DTOs or views??

class CategoryBase(BaseModel):
    name: str


class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True

class CategoryCreate(CategoryBase):
    pass


class ArticleBase(BaseModel):
    title: str
    excerpt: str
    category_id : Optional[int]
    slug : str
    url_thumbnail : Optional[str]
    


class ArticleCreate(ArticleBase):
    published_at: Optional[datetime] 
    pass


class Article(ArticleBase):
    id: int
    published_at: Optional[datetime] 
    category_id: Optional[int]
    
    class Config:
        orm_mode = True


