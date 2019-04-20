#!/usr/bin/env python3

import os
import socket
import time


HOST = os.getenv('APP_HOST', "127.0.0.1")  # The server's hostname or IP address
PORT = os.getenv('APP_PORT', "3000")         # The port used by the server

print("connecting at", HOST, PORT)
while True:
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.settimeout(5)
      s.connect((HOST, int(PORT)))
      s.sendall(b'Hello, world')
      data = s.recv(1024)

  print('Received', repr(data), flush=True)
  time.sleep(1)