__author__ = 'Ge Yang'

import socket
import sys

DEFAULT_URL = 'localhost:27182'


def connect(path):
    if not path:
        path = DEFAULT_URL
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    url, port = path.split(':')
    print('connecting to {url} {port}'.format(url=url, port=port), file=sys.stderr)
    sock.connect((url, int(port)))
