from werkzeug.security import generate_password_hash,check_password_hash

hashed_passwd = generate_password_hash(password='supersecretpassword')
print(hashed_passwd)

check = check_password_hash(hashed_passwd,"supersecretpassword")
print(check)

