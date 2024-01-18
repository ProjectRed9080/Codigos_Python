import random

chars = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890!#$%&/(=)"

password = ""

for i in range(16):
    password += random.choice(chars)

print(f"Contraseña aleatoria: {password}")
