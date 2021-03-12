#!/usr/bin/env python3

import socket

# create socket obj, add socket family and type
serverSocket = socket.socket(
  socket.AF_INET, socket.SOCK_STREAM
)

# get host and set port
# host  = '192.168.1.9' <- same thing as below, just better
host = socket.gethostname()
port = 3000

# bind host and port to socket obj
serverSocket.bind((host, port))

# tcp listener
serverSocket.listen(3)

while True:
  # start the connection
  clientSocket, address = serverSocket.accept()

  print('Connected to %s' % str(address))
  message = 'HI' + '\r\n'
  # send to client
  clientSocket.send(message.encode('ascii'))
  # close connection
  clientSocket.close()
