import  dotenv 
from cryptography.fernet import Fernet

class fernet_key:   

    def generate_key():
        config = dotenv.dotenv_values(".env")
        # print("key before: ", config["FERNET_KEY"])
        key = Fernet.generate_key()
        # print("key: ", type(key))
        # print("key: ", key)
        dotenv.set_key("./.env", "FERNET_KEY", key.decode())
        return

    def encrpyt(message: dict, key: str):
        f = Fernet(key)
        # print("message: ",message)
        for key, value in message.items():
            message[key]=f.encrypt(value.encode())
        return message

    def decrypt(message: bytes, key: str):
        # print(message)
        f = Fernet(key)
        return f.decrypt(message).decode()