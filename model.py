"""
model.py

"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine("sqlite:///ratings.db", echo=False)
session = scoped_session(sessionmaker(bind=engine, autocommit = False, autoflush = False))

Base = declarative_base()
Base.query = session.query_property()

### Class declarations go here
class User(Base):
    __tablename__ = "users"
    
    """Import columns from U.user"""
    id = Column(Integer, primary_key = True)
    email = Column(String(64), nullable = True)
    password = Column(String(64), nullable = True)
    age = Column(Integer, nullable = True)
    zipcode = Column(String(15), nullable = True)


class Movie(Base):
    """Import columns from U.item"""
    __tablename__ = "movies"

    id = Column(Integer, primary_key = True)
    title = Column(String(64), nullable = False)
    released_at = Column(String(64), nullable = True)
    url = Column(String(300), nullable = True)


class Rating(Base):
    """Import columns from U.data"""
    __tablename__ = "ratings"

    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("users.id"))
    movie_id = Column(Integer, ForeignKey("movies.id"))
    rating = Column(Integer, nullable = False)
    
    user = relationship("User", backref=backref("ratings", order_by=id))
    movie = relationship("Movie", backref=backref("ratings", order_by=id))

### End class declarations

def connect():
    global engine
    global session

    engine = create_engine("sqlite:///ratings.db", echo = True)
    session = sessionmaker(bind = engine)

    return session()

def main():
    """Create main function just in case."""
    pass

if __name__ == "__main__":
    main()
