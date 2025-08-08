def Escrever(tarefa):
    with open("Lista.txt","a") as list:
        list.write(f"{tarefa}"+"\n")
        

def Remover(nome_arquivo,linha_a_remover):
    with open(nome_arquivo,"r") as arquivo:
        linhas= arquivo.readlines()
        del linhas[linha_a_remover]
    with open(nome_arquivo,"w") as arquivo:
        arquivo.writelines(linhas)
    
def Marcar_concluido(nome_arquivo,linha_a_remover):
    with open(nome_arquivo,"r") as  arquivo:
        linhas= arquivo.readlines()
        linhas[linha_a_remover]=linhas[linha_a_remover].strip()+ " Concluido\n"
    with open(nome_arquivo,"w") as arquivo:
        arquivo.writelines(linhas)

def Reecrever(lista):
    with open("Lista.txt","w") as list:
        list.write(lista)