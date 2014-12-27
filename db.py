from sqlalchemy import create_engine, Column, Integer, String, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

engine = create_engine(config['Database']['connection_string'], echo=True)
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

# Retuns a list of messages for a given nick and channel
def get_user_messages(nick, channel):
    messages = session.query(VolunteerMessage).filter(VolunteerMessage.nick == nick, VolunteerMessage.channel == channel).all()
    return messages

# Get how many things a given nick has volunteered to do in a channel
def count_user_messages(nick, channel):
    count = len(get_user_messages(nick, channel))
    return count

Base.metadata.create_all(engine)