import random

angka_rahasia = random.randint(1, 100)
tebakan = None

while tebakan != angka_rahasia:
    tebakan = int(input("Tebak sebuah angka antara 1 dan 100: "))
    if tebakan < angka_rahasia:
        print("Terlalu kecil!")
    elif tebakan > angka_rahasia:
        print("Terlalu besar!")
    else:
        print(f"Selamat! Anda menebak angka yang benar: {angka_rahasia}")
