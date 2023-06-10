from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base

# Create database engine and create a base class which will be used to create the table
database_engine = create_engine('sqlite:///db.sqlite3', echo=False, future=True)
Session = sessionmaker(bind=database_engine)
Base = declarative_base()

class Users(Base):
    # discord user info
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    discriminator = Column(String, nullable=False)
    global_name = Column(String, nullable=False)

    # bot info
    coins = Column(Integer)

class Cards(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    img = Column(String, nullable=False)
    description = Column(String, nullable=False)
    shiny = Column(Boolean, nullable=False)
    stars = Column(Integer, nullable=False)


def create_tables():
    Base.metadata.create_all(database_engine)