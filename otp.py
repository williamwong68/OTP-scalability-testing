# import socket
# import sys
# import pyotp
# import sys
# from datetime import datetime as dt
# import time


# this only showing how to get the website ip
# try:
# 	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 	print("Socket successfully created")
# except socket.error as err:
# 	print("Socket creation failed with error %s" %(err))

# # default port for socket
# port = 80

# try:
# 	host_ip = socket.gethostbyname('www.google.com')
# except socket.gaierror:

# 	# this means could not resolve the host
# 	print("there was an error resolving the host")
# 	sys.exit()

# # connecting to the server
# s.connect((host_ip, port))

# print("the socket has successfully connected to google")

# print("on port ==", host_ip)



# n = 10 #TODO: adjust number when testing

# totps = [0] * n
# times = [0] * n
# otps = [0] * n
# now = dt.now()





# # generate OTPs
# for i in range(n):    
# 	totps[i] = pyotp.TOTP(pyotp.random_base32())
# 	times[i] = dt.now()
# 	otps[i] = totps[i].at(times[i])
# 	print("generaate time:")
# 	print(now)

# end_test = dt.now()
# #verify OTPs
# start = time.time()
# for i in range(n):
# 	totps[i].verify(otps[i], for_time=times[i])
# 	print("verify time: ")
# 	print(end_test) 

# end = time.time()

# print(end - start)


# # No network here, should be server and client