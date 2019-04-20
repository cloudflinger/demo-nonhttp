#!/usr/bin/env python3

import socket
import sys

HOST = '0.0.0.0'  # Standard loopback interface address (localhost)
PORT = 3000        # Port to listen on (non-privileged ports are > 1023)

# this only handles a single connection at a time
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr, flush=True)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
