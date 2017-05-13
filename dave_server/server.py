__author__ = 'Ge Yang'

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = 'localhost'
port = 27182
print('starting up on {server_address}:{port}'.format(server_address=server_address, port=port), file=sys.stderr)
sock.bind((server_address, port))

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection', file=sys.stdout)
    connection, client_address = sock.accept()

    try:
        print('connection from', file=sys.stderr)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print('received {data}'.format(data=data), file=sys.stderr)
            if data:
                print('sending data back to client'.format(data=data), file=sys.stderr)
                connection.sendall(data)
            else:
                print('no more data from client {address}'.format(address=client_address), file=sys.stderr)
                break

    finally:
        # Clean up the connection
        connection.close()


class Daemon():
    def list(self):
        """returns all running instances"""
        return [{id: 'instance_id'}]

    def terminate(self, instance_id):
        """terminate instance by id"""
        # todo: look up library

    def log(self, instance_id):
        """get the log file of instance with id"""
        return {}


