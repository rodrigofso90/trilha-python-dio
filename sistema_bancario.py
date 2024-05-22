# Neste projeto, você terá a oportunidade de criar um Sistema Bancário em Python. O objetivo é implementar três operações essenciais:
# depósito, saque e extrato. O sistema será desenvolvido para um banco que busca monetizar suas operações.
# Durante o desafio, você terá a chance de aplicar seus conhecimentos em programação Python e criar um sistema funcional que simule as 
# operações bancárias. Prepare-se para aprimorar suas habilidades e demonstrar sua capacidade de desenvolver soluções práticas e eficientes.

menu = """ <=

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    
=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == 'd':
        valor = float(input("Digite o valor que deseja depositar: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            
        else:
            print("Depósito falhou!!! Tente novamente!\n")
    
    elif opcao == "s":
        valor = float(input("Digite o valor de saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n<================ EXTRATO ================>")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("<================ EXTRATO ================>")

    elif opcao == "q":
        print("Acesso finalizado.")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        