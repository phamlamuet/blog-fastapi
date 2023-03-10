from sqlalchemy.orm import Session
from datetime import datetime
from . import models, schemas


def get_articles(db: Session, page : int = 0, limit: int = 100):
    return db.query(models.Article).offset(page*limit).limit(limit).all()

def get_articles_by_category(db: Session, page : int = 0, limit: int = 100, category_id : int = 1):
    return db.query(models.Article).filter(models.Article.category_id == category_id).offset(page*limit).limit(limit).all()

def get_detail_of_an_article(db : Session, slug : str |None = None):
    return db.query(models.Article).filter(models.Article.slug == slug).all()
def create_article(db: Session, article: schemas.ArticleCreate):

    db_article = models.Article(title = article.title,excerpt = article.excerpt, slug = article.slug, published_at = datetime.now(), category_id = article.category_id, url_thumbnail = article.url_thumbnail, content = article.content)
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article


def get_categories(db: Session, skip: int = 0,limit: int = 100):
    return db.query(models.Category).offset(skip).limit(limit).all()
    
def get_categories_by_name(db : Session, name : str):
    return db.query(models.Category).filter(models.Category.name == name).first()

def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(name = category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category




