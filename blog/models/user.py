from sqlalchemy import Column, Integer, String, Boolean
from blog.models.database import db
from flask_login import UserMixin
from sqlalchemy.orm import relationship


class User(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    is_staff = Column(Boolean, nullable=False, default=False)

def __repr__(self):
    return f"<User #{self.id} {self.username!r}>"



class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    author = relationship("Author", uselist=False, back_populates="user")

email = Column(String(255), nullable=False, default="", server_default="")