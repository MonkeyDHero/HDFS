# -*- coding: UTF-8 -*-
import socket
import struct
HOST, PORT = '127.0.0.1', 9997
data= struct.pack('2B6H',1,2,05056,259,260,261,262,263)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
sock.send(data)
sock.close()