def Escrever(a):
    with open("Lista.txt","r+") as list:
        list.write(f"{a}")