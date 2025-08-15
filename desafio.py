# Olá! Sejam bem-vindos ao meu Projeto em Python.

print("=" * 40)
print("==== Bem-vindo ao Banco FinBank ===")
print("Sistema Bancário Simples em Python")
print("=" * 40)

saldo = 0
limite = 500
extrato = ""
LIMITE_SAQUE = 3
numero_saques = 0

def menu():
    print("\nAgora escolha uma das opções abaixo:")
    print("[1] - Depositar")
    print("[2] - Sacar")
    print("[3] - Extrato")
    print("[4] - Sair")
    return input("Digite o número da opção desejada: ")

while True:
    opcao = menu()  # chama a função menu

    if opcao == "1":  # Depósito
        valor = float(input("Informe o valor do depósito: R$ "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: +R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para depósito!")
    
    elif opcao == "2":  # Saque
        valor = float(input("Informe o valor para saque: R$ "))

        if numero_saques >= LIMITE_SAQUE:
            print("Limite de saques diários atingido.")
        elif valor > limite:
            print("O valor do saque excede o limite por operação!")
        elif valor > saldo:
            print("Saldo insuficiente.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: -R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para saque!")
    
    elif opcao == "3":  # Extrato
        print("\nExtrato Bancário")
        print("=" * 25)
        if extrato:
            print(extrato)
        else:
            print("Nenhuma movimentação registrada.")
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("=" * 25)
    
    elif opcao == "4":  # Sair
        print("Saindo do sistema... Obrigado por usar o FinBank!")
        break  # só sai do loop aqui

    else:
        print("Opção inválida! Escolha uma opção de 1 a 4.")

print("👏 Obrigado por acompanhar o projeto até o fim! Ele foi desenvolvido com objetivo de aprendizado e prática de Python.")

