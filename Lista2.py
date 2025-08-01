#Lista de afazeres
from open import Escrever



while True:
    print(""" ____________________________
|                            |
|      lista de tarefas      |
|____________________________|
|                            |
|  1- INSERIR TAREFA         |
|                            |
|  2- LISTAR TAREFAS         |
|                            |
|  3- MARCAR COMO CONCLUIDO  |
|                            |
|  4- REMOVER TAREFA         |
|                            |
|  0- SAIR                   |
|____________________________|

""")
    with open("Lista.txt","r+") as lista:
        lista_de_tarefas=lista.read().split()
    

    pergunta=int(input("Oque voçê gostaria de fazer na sua lista? "))
    if pergunta == 1:
        tarefa=input("Qual seria a tarefa? ")
        Escrever(f"{tarefa}")
        print("Tarefa adicionada com sucesso!!")
        input("Aperte ENTER para continuar")        
    if pergunta == 2:
        a=0
        for x in lista_de_tarefas:
            print(f"""{a}-{x}""")
            a+=1
        print("Aqui estao suas tarefas!!")
        input("Aperte ENTER para continuar")
    if pergunta ==3:
        a=0
        for x in lista_de_tarefas:

            print(f"""{a}-{x}""")
            a+=1        
        item_N=int(input("Qual desses voçê gostaria de marcar como concluido? "))
        lista_de_tarefas[item_N]=lista_de_tarefas[item_N] + " ✓"
        print(f"Item N°{item_N} marcado como concluido")
        input("aperte ENTER para continuar")
    if pergunta ==4:
        a=0
        for x in lista_de_tarefas:

            print(f"""{a}-{x}""")
            a+=1
        item_N=int(input("Qual desses voçê gostaria de remover? ")) 
        del lista_de_tarefas[item_N]
        print(f"Item N°{item_N} removido com sucesso")
        input("aperte ENTER para continuar")
    if pergunta== 0:
        break
print(""",
""".join(lista_de_tarefas))
