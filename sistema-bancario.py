menu= """
     SEJA MUITO BEM-VINDO!!!
    =========NETBANK=========
              MENU
      
      [1] Sacar
      [2] Deposito
      [3] Extrato
      [4] Sair do Sistema
      
    =========================
==>"""

saldo=0
limite=500
extrato= ""
numero_saque= 0
LIMITE_SAQUE= 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor que deseja sacar:"))

        limite_saldo = valor > saldo
        limite_maximo = valor > limite
        limite_saques = numero_saque >= LIMITE_SAQUE

        if limite_saldo:
            print("Operação Falhou! Valor insuficiente, Deposite seu Dinheiro")

        elif limite_maximo:
            print("Operação Falhou! O valor do saque excede o limite.")
        
        elif limite_saques:
            print("Operação Falhou! Limite de Saque já foram exercidas, espero pro proximo dia.")

        elif valor > 0:
         saldo -= valor
         extrato += f"Saque: R$ {valor:.2f}\n"
         numero_saque += 1

        else:
         ("Operação Falhou! Valor Informado Incorreto")


    elif opcao == "2":
        valor = float(input("Informe o valor do seu deposito:"))


        if valor > 0:
          saldo += valor
          extrato += f"Deposito: R$ {valor:.2f}\n"

        else:
           print("Operação Falhou, tente novamente.")


    
    elif opcao == "3":
       print("\n=================EXTRATO NETBANK=================")
       print("Não foram relizadas nenhuma movimentação" if not extrato else extrato)
       print(f"\nSaldo: R$ {saldo:.2f}") 
       print("===================================================")

       
    
    elif opcao == "4":
        break

    else:
        print("Opção Invalida, por favor, Seleciona a Opção Correta.")