def Escrever(a):
    with open("Lista.txt","a") as list:
        list.write(f"""
{a}""")