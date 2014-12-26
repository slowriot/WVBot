from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///:memory', echo=True)

Base = declarative_base()
class VolunteerMessage(Base):
    __tablename__ = 'volunteer_message'

    id = Column(Integer, primary_key=True)
    nick = Column(String)
    message = Column(String)

    def __repr__(self):
        return "<VolunteerMessage(id='{0}', nick='{1}', message='{2}')>".format(self.id, self.nick, self.message)

Base.metadata.create_all(engine) 