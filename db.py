from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///db.sqlite', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
class VolunteerMessage(Base):
    __tablename__ = 'volunteer_message'

    id = Column(Integer, primary_key=True)
    nick = Column(String)
    message = Column(String)
    channel = Column(String)

    def __repr__(self):
        return "<VolunteerMessage(id='{0}', nick='{1}', message='{2}', channel='{3}')>".format(self.id, self.nick, self.message, self.channel)

def insert_message(nick, message, channel):
    volunteer_message = VolunteerMessage(nick=nick, message=message, channel=channel)
    session.add(volunteer_message)
    session.commit()

Base.metadata.create_all(engine)