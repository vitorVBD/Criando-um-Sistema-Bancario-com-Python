menu = """

    [d] - Depositar
    [s] - Sacar
    [e] - Extrato
    [q] - Sair

=>"""

balance = 0
limit = 500
statement = ""
withdrawals_historic = ""
deposit_historic = ""
number_of_withdrawals = 0
number_of_deposits = 0
WITHDRAW_LIMIT = 3

while True:

    option = input(menu)

    if option == 'd':
        value = float(input("Digite o valor do depósito: "))
        if value > 0:
            balance += value
            statement = f"\nDepósito de R$ {value:.2f}\nSeu saldo agora é de R$ {balance:.2f}\n"
            number_of_deposits += 1
            deposit_historic += f"\n{number_of_deposits}° depósito no valor de R$ {value:.2f}"
            print(statement)
        else:
            print("O valor do depósito deve ser positivo")

    elif option == 's':
        value = float(input("Digite o valor do saque: "))
        if value > 500:
            print("Valor máximo de saque é de R$ 500")
        else:
            if value > balance:
                print("Saldo insuficiente")
                print(f"Seu saldo é de R$ {balance:.2f}")
            elif number_of_withdrawals >= WITHDRAW_LIMIT:
                print("Limite de saques diários atingido")
            else:
                balance -= value
                statement = f"\nSaque no valor de R$ {value:.2f}\nSeu saldo agora é de R$ {balance:.2f}\n"
                number_of_withdrawals += 1
                withdrawals_historic += f"\n{number_of_withdrawals}° saque no valor de R$ {value:.2f}"
                print(statement)

        
    elif option == 'e':
        statement = f"\nSeu saldo é de R$ {balance:.2f}\n"
        print(f"Historico de depositos: {deposit_historic}")
        print(f"Histórico de saques: {withdrawals_historic}")
        print(statement)

    elif option == 'q':
        break

    else:
        print("Opção inválida, digite novamente")