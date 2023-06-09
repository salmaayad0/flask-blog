#database configuration

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, Unicode, String

db = SQLAlchemy() 


class Posts(db.Model):
    __tablename__ = 'Posts'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String)
    body = db.Column(db.Text)
    image = db.Column(db.String)


    def __str__(self):
        return self.title
    
    # all posts
    @classmethod
    def getAllPosts(cls):
        return cls.query.all()
    
    # one post
    @classmethod
    def getPost(cls, id):
        return cls.query.get_or_404(id)
    
    # delete
    def deletePost(self):
        db.session.delete(self)
        db.session.commit()
        return True
    
    # create
    def createPost(self):
        db.session.add(self)
        db.session.commit()
        return True
    
    # update
    
    
class Category(db.Model):
    __tablename__ = 'Category'
    id = db.Column(db.Integer,primary_key=True)
    category = db.Column(db.String)
    post_id = db.Column(db.Integer, db.ForeignKey("Posts.id"), nullable=True)
    
    
    def __init__(self):
        return self.category

    @classmethod
    def get_all_categories(cls):
        return cls.query.all()




