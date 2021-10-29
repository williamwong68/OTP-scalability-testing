import pyotp
import socket
# from datetime import datetime
import time
import json

with open("secret.txt", "r") as secret_file:
	users = json.load(secret_file)

start = time.time()
print(start)

for i in range(len(users)):

    s = socket.socket()

    port = 12345

    s.connect(("localhost", port))

    
    totps = pyotp.TOTP(users[str(i)])
    password = totps.now()

    # s.send(f"{{'user':{str(i)}, 'password':{password}}}".encode())
    # s.send(f'{"user":{str(i)}, "password":{password}'.encode())
    # s.send(f'{{"user":{str(i)}, "password":{password}}}'.encode())
    s.send(f'{{"user":"{i}", "password":"{password}"}}'.encode())


    # print(start)
    print(password)

    # print(type(totps))

    print(s.recv(1024))

    # end = datetime.now()

    # print(end)
    print("\n")

    s.close()

end = time.time()
print(end)
print("Total time: ")
print(end - start)
    # print(timedelta(seconds = end - start))