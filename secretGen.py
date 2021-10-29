import pyotp
import json

n = 500000
with open("secret.txt", "w") as secret_file:
    users = {}

    for i in range(n):
        secret = pyotp.random_base32()

        username = str(i)
        users[i] = secret

    json.dump(users, secret_file)

