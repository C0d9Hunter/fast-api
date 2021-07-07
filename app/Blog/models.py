from sqlalchemy import Boolean,Text, Column, Integer, String, ForeignKey
from Blog.database import  Base
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__="blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(Text)
    published = Column(Boolean,default=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="blogs")


class User(Base):
    __tablename__="users"

    id = Column(Integer, primary_key=True,index=True)
    name = Column(String,nullable=False)
    email = Column(String,nullable=False,unique=True,)
    password = Column(String,nullable=False)
    is_active = Column(Boolean,default=True)
    blogs = relationship("Blog",back_populates="owner")