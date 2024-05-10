menu= """
     SEJA MUITO BEM-VINDO!!!
    =========NETBANK=========
              MENU
      
      [1] Sacar
      [2] Deposito
      [3] Extrato
      [4] Sair do Sistema
      
    =========================
"""

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
        limite_saques = valor >= LIMITE_SAQUE

        if limite_saldo:
            print("Operação Falhou! Saldo Insuficiente, Deposite seu Dinheiro")

        elif limite_maximo:
            print("Operação Falhou! O valor do saque excede o limite.")
        
        elif limite_saques:
            print("Operação Falhou! Limite de Saque já foram exercidas, espero pro proximo dia.")


    elif opcao == "2":
        print("Deposito")
    
    elif opcao == "3":
        print("Extrato")
    
    elif opcao == "4":
        break

    else:
        print("Opção Invalida, por favor, Seleciona a Opção Correta.")