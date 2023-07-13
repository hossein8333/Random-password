import random
import string

class PasswordGenerator:
    def generate_password(self, length: int) -> str:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password
