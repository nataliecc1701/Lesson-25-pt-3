"""Models for Cupcake app."""

# SQLAlchemy Imports
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Cupcake(db.Model):
    '''Cupcake model'''
    
    __tablename__ = "cupcakes"
    
    id =        db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor =    db.Column(db.Text, nullable=False)
    size =      db.Column(db.Text, nullable=False)
    rating =    db.Column(db.Float, nullable=False)
    image =     db.Column(db.Text, nullable=False, default="https://tinyurl.com/demo-cupcake")
    
    def to_dict(self):
        '''returns a python dictionary containing all properties'''
        return {"id":   self.id,
             "flavor":  self.flavor,
             "size":    self.size,
             "rating":  self.rating,
             "image":   self.image}
        