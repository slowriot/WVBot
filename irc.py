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

    @gen.coroutine
    def connect(self):
        logging.info("Connecting to IRC server - {0}:{1}".format(self.host, self.port))
        tcpclient_factory = tcpclient.TCPClient()
        self.conn = yield tcpclient_factory.connect(self.host, self.port)
        logging.info("Connected")
        self.schedule_line()

    def schedule_line(self):
        self.conn.read_until(b'\n', self.line_callback)

    def line_callback(self, data):
        print(data)

        # if data == b'NOTICE AUTH :*** Found your hostname\r\n':
        #     self.write_line("JOIN #wvbot")

        self.schedule_line()

    def write_line(self, data):
        if data[-1] != '\n':
            data += '\n'

        self.conn.write(data.encode('utf8'))

def main():

    logging.debug("Adding callback")
    irc = IRC()
    loopinstance.add_callback(irc.connect)

    logging.debug("Starting Loop Instance")
    loopinstance.start()

if __name__ == '__main__':
    main()
