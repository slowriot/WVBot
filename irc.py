'''
    This class abstracts all the IRC stuff into a simple API
'''
import logging

from tornado import tcpclient, gen, ioloop

loopinstance = ioloop.IOLoop.instance()

logging.basicConfig(level=logging.DEBUG)

class IRC(object):
    def __init__(self):
        self.host = "irc.imaginarynet.org.uk"
        self.port = 6667
        self.nick = "WVBot"
        self.conn = None

    # Connects to the IRC server and returns a future
    @gen.coroutine
    def connect(self):
        logging.info("Connecting to IRC server - {0}:{1}".format(self.host, self.port))
        tcpclient_factory = tcpclient.TCPClient()
        self.conn = yield tcpclient_factory.connect(self.host, self.port)
        logging.info("Connected")

    # Returns a future that will return a line retrieved from the server
    def schedule_line(self):
        return self.conn.read_until(b'\n')

    # Sends a line of text to the server, used by other functions in this class
    def _write_line(self, data):
        if data[-1] != '\n':
            data += '\n'

        self.conn.write(data.encode('utf8'))

    def ident(self):
        self._write_line("USER {0} {1} {2} {3}".format(self.nick, self.nick, self.nick, self.nick))
        self._write_line("NICK {0}".format(self.nick))


irc = IRC()

def main():

    logging.debug("Adding callback")
    loopinstance.add_future(irc.connect(), connection_complete)
    
    logging.debug("Starting Loop Instance")
    loopinstance.start()


def connection_complete(data):
    irc.ident()
    loopinstance.add_future(irc.schedule_line(), line_received)

def line_received(line):
    print(line.result())

    loopinstance.add_future(irc.schedule_line(), line_received)

if __name__ == '__main__':
    main()
