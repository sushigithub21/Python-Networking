# Network scanner code

import socket

def is_port_open(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        s.shutdown(socket.SHUT_RDWR)
        return True
    except:
        return False
    finally:
        s.close()

for port in range(1, 1025):
    if is_port_open('127.0.0.1', port):
        print('Port', port, 'is open')
