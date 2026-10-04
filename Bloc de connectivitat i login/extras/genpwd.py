from getpass import getpass
from werkzeug.security import generate_password_hash

password = getpass("Contrasenya: ")
hashed_password = generate_password_hash(password)

print(f"Hash per a la base de dades:\n{hashed_password}")
