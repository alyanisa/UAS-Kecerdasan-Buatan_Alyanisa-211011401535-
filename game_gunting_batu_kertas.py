# Permainan Gunting, Batu, Kertas

Kode berikut adalah implementasi permainan "Gunting, Batu, Kertas" menggunakan bahasa pemrograman Python. Anda akan bermain melawan komputer yang memilih secara acak di setiap putaran.

# Mengimpor Modul Random
import random

# Inisialisasi Variabel
a = 0
s = int(input("Mau main berapa kali:")) # Pemain memasukkan ingin berapa kali main

# Loop untuk Setiap Putaran
while a < s:
    a = a + 1

    # Input Pemain dan Pilihan Komputer
    you = input("Masukkan pilihan antara gunting, batu, kertas: ")
    choose = ["gunting", "batu", "kertas"]
    computer = random.choice(choose)

    if you == computer:
        print("Seri") # Logika Permainan (Seri)
    # Logika Permainan (Pemain memilih Gunting)
    elif you == "gunting":
        if computer == "kertas":
            print("Computer=kertas kamu menang!!")
        else:
            print("Computer=batu kamu kalah!!")
    # Logika Permainan (Pemain memilih Batu)
    elif you == "batu":
        if computer == "gunting":
            print("Computer=gunting kamu menang!!")
        else:
            print("Computer=kertas kamu kalah!!")
    # Logika Permainan (Pemain Memilih Kertas)
    elif you == "kertas":
        if computer == "batu":
            print("Computer=batu kamu menang!!")
        else:
            print("Computer=gunting kamu kalah!!")
