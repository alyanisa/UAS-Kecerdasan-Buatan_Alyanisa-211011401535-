import random

a=0
s=int(input("mau main berapa kali:"))

while a<s:
    a=a+1

    you=input("masukkan pilihan antara gunting batu kertas")
    choose=["gunting","batu","kertas"]
    computer=random.choice(choose)

    if you==computer:
        print("seri")
    elif you=="gunting":
        if computer=="kertas":
            print("computer=kertas kamu menang!!") 
        else:
            print("computer=batu kamu kalah!!")
    elif you=="batu":
        if computer=="gunting":
            print("computer=gunting kamu menang!!") 
        else:
            print("computer=kertas kamu kalah!!")
    elif you=="kertas":
        if computer=="batu":
            print("computer=batu kamu menang!!") 
        else:
            print("computer=gunting kamu kalah!!")