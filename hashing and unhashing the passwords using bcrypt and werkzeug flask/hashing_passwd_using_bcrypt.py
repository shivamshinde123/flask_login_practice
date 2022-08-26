from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


password = "supersecretpassword"

hashed_passwd = bcrypt.generate_password_hash(password=password)

print(hashed_passwd)

check = bcrypt.check_password_hash(hashed_passwd,'supersecretpassword')

print(check)