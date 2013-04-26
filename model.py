from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

ENGINE = None
Session = None

Base = declarative_base()

### Class declarations go here
class User(Base):
    __tablename__ = "users"
    
    """Import columns from U.user"""
    id = Column(Integer, primary_key = True)
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
    user_id = Column(Integer, nullable = True)
    movie_id = Column(Integer, nullable = True)
    rating = Column(Integer, nullable = False)
    

### End class declarations

def connect():
    global ENGINE
    global Session

    ENGINE = create_engine("sqlite:///ratings.db", echo = True)
    Session = sessionmaker(bind = ENGINE)

    return Session()

def main():
    """Create main function just in case."""
    pass

if __name__ == "__main__":
    main()
