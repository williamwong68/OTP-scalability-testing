import pyotp
from server import *

port = 12345

totps = pyotp.TOTP(pyotp.random_base32)






# totp_uri = pyotp.totp.TOTP(base32secret).provisioning_uri(
# 	"alice@google.com",
# 	issuer_name = "Secure APP"
# )
# print(totp_uri)