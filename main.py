import random

elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

panjang_password = int(input("Masukkan panjang kata sandi:"))

password = ""
for i in range(panjang_password):
    password += random.choice(elements)

print("Halo, password kamu sudah dibuat")
print(password)
