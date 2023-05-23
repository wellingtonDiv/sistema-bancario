menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    opcao = input(menu)

    if opcao =="d":
        valor = float(input("informe o valor de deposito: "))

        if valor > 0:
            saldo+= valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informando e invalido.")
                


    elif opcao== "s":
        valor= float(input("informe o valor de saque "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES
    
        if excedeu_saldo:
             print("Operação falhou! Você não tem saldo suficiente.")
        
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
             print("Operação falhou! Número máximo de saques excedido.")

        elif valor>0:
            valor-= saldo
            extrato += f"saque: R$ {valor:.2f}\n"
            numero_saques+=1
        else:
            print("Operação falhou! o valor informando e invalindo")


    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("nao foram realizadas movimentaçoes")
        print(f"\n saldo: R$ {saldo:.2f}")

    elif opcao == "q":
        break

    else:
        print("operação invalinda")






