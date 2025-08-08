def Escrever(a):
    with open("Lista.txt","a") as list:
        list.write(f"""{a}
""")
        

def Remover(nome_arquivo,linha_a_remover):
    with open(nome_arquivo,"r") as  arquivo:
        linhas= arquivo.readlines()
        del linhas[linha_a_remover]
    with open(nome_arquivo,"w") as arquivo:
        arquivo.writelines(linhas)
    
def Marcar_concluido(nome_arquivo,linha_a_remover):
    with open(nome_arquivo,"r") as  arquivo:
        linhas= arquivo.readlines()
        linhas[linha_a_remover]=linhas[linha_a_remover] + " Concluido" 
    with open(nome_arquivo,"w") as arquivo:
        arquivo.writelines(linhas)