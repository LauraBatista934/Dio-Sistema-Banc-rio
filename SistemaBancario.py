menu = """
[A] Adicionar saldo
[R] Realizar saque
[E] Exibir extrato
[X] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_depositos = 0
LIMITE_DEPOSITOS = 5

while True:

    opcao = input(menu)

    if opcao == "A":
        valor = float(input("Informe o valor a ser adicionado ao saldo: "))

        if valor > 0: # evita adicionar valores negativos
            saldo += valor # operaçao de adiçao
            extrato += f"Adição de saldo: R$ {valor:.2f}\n" # adiciona ao extrato com 2 casas decimais
            numero_depositos += 1 # Incrementa o número de depósitos
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "R":
        valor = float(input("Informe o valor do saque: "))

        excedeu_limite = valor > limite

        if excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif valor > 0:
            saldo -= valor # Subtraindo o valor do saque do saldo da conta
            extrato += f"Saque: R$ {valor:.2f}\n" # Atualizando o valor do extrato da conta
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "E":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "X":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
