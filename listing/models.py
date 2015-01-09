#I imported String here
from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    String,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Integer)

#I created this model to hold the paste texts.changed sqlalchemy driver in developement.ini 
class Paste(Base):
    __tablename__ = 'pastes'
    email = Column(String(25), unique=True ,primary_key=True)
    text = Column(String(50))
    time = Column(String(30))


Index('my_index', MyModel.name, unique=True, mysql_length=255)
