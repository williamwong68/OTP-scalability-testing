import socket
import pyotp
import json

with open("secret.txt", "r") as secret_file:
	users = json.load(secret_file)

print(users)



s = socket.socket()
print("Socket successfully created")

port = 12345

s.bind(('', port))
print("socket binded to %s" %(port))

while True:
    	
		s.listen(5)
		print("socket is listening")
    	
		c, addr = s.accept()
		print('Got connection from', addr)


		request = c.recv(1024).decode()
		# print(request)
		request = json.loads(request)
		# print(request)
		username = request["user"]
		totps = pyotp.TOTP(users[username])
		
		# print(type(request))

		# print(type(totps.now()))

		print(request == totps.now())
		# request = request[:6]
		# print(len(request))
		print(request)
	
		PW = totps.verify(request["password"])

		c.send(f"Password is valid = {PW}".encode())

		c.close()
		# break


# base32secret = pyotp.random_base32()
# print('Secret: ', base32secret)

