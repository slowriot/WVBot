import logging
from irc import IRC

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def main():
    irc = IRC(host="irc.imaginarynet.org.uk", port=6667, nick="WVBot", channel="#bottest")
    irc.channel_message_received_callback = channel_message
    irc.start_connection()

def channel_message(sender, channel, message):
    print("Message from {0} in {1}: {2}".format(sender, channel, message))

if __name__ == '__main__':
    main()