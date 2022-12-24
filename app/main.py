from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import uvicorn
from . import crud, models, schemas
from .database import SessionLocal, engine, get_db
from fastapi_pagination import Page, add_pagination, paginate

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# define crud ops here


@app.get("/blog/articles/listall", response_model=list[schemas.Article])
def read_articles(limit: int = 100, page: int = 0, db: Session = Depends(get_db)):
    articles = crud.get_articles(db, page=page, limit=limit)
    return articles


@app.get("/blog/articles/category/article/")
def get_article_by_category(limit: int = 100, page: int = 0, db: Session = Depends(get_db), category_id: int = 1):
    articles = crud.get_articles_by_category(db=db, page=page, limit=limit, category_id=category_id)
    return articles

@app.post("/blog/articles/", response_model=schemas.Article)
def create_article(article: schemas.ArticleCreate, db: Session = Depends(get_db)):
    return crud.create_article(db=db, article=article)


@app.get("/categories/", response_model=list[schemas.Category])
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    categories = crud.get_categories(db, skip=skip, limit=limit)
    return categories


@app.post("/categories/", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db=db, category=category)

# uvicorn app.main:app --reload --port 5000


if __name__ == '__main__':
    uvicorn.run("app.main:app", port=5000, reload=True, access_log=False)
