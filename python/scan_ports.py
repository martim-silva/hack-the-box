import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

for i in range(1, 9999):
    result = s.connect_ex(('127.0.0.1', i))

    if result == 0:
        print(f'port {i} is open')
    else:
        #print(f'port {i} is closed')
        pass


s.close()