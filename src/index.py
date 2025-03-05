import textwrap

def menu(): 
    menu = """\n
    ===============MENU===============

    [d] - Depositar
    [s] - Sacar
    [e] - Extrato
    [nc] - Nova Conta
    [lc] - Listar Contas
    [nu] - Novo Usuário
    [q] - Sair

=>"""
    return input(textwrap.dedent(menu))

def deposit(balance, value, statement, number_of_deposits, deposit_historic):
    if value > 0:
        balance += value
        statement = f"\nDepósito de R$ {value:.2f} realizado com sucesso! \nSeu saldo agora é de R$ {balance:.2f}\n"
        number_of_deposits += 1
        deposit_historic += f"\n{number_of_deposits}° depósito no valor de R$ {value:.2f}"
        print(statement)
    else:
        print("O valor do depósito deve ser positivo")
    return balance, statement, number_of_deposits, deposit_historic

def withdraw(*, balance, value, statement, number_of_withdrawals, withdrawals_historic, limit, WITHDRAW_LIMIT):
    if value > limit:
        print("Valor máximo de saque é de R$ 500")
    elif value > balance:
        print("Saldo insuficiente")
        print(f"Seu saldo é de R$ {balance:.2f}")
    elif number_of_withdrawals >= WITHDRAW_LIMIT:
        print("Limite de saques diários atingido")
    else:
        balance -= value
        statement = f"\nSaque realizado com sucesso! no valor de R$ {value:.2f}\nSeu saldo agora é de R$ {balance:.2f}\n"
        number_of_withdrawals += 1
        withdrawals_historic += f"\n{number_of_withdrawals}° saque no valor de R$ {value:.2f}"
        print(statement)
    return balance, statement, number_of_withdrawals, withdrawals_historic

def show_statement(balance, statement, deposit_historic, withdrawals_historic):
    statement = f"\nSeu saldo é de R$ {balance:.2f}\n"
    print(f"Historico de depositos: {deposit_historic}")
    print(f"Histórico de saques: {withdrawals_historic}")
    print(statement)

def create_user(users):
    cpf = input("Digite o CPF do usuário: ")
    user = filter_user(cpf, users)

    if user:
        print("Usuário já cadastrado")
        return
    
    name = input("Digite o nome completo: ")
    birth_date = input("Digite a data de nascimento (dd-mm-aaaa): ")
    address = input("Digite o endereço (logradouro, numero - bairro - cidade/sigla estado): ")

    users.append({
        "cpf": cpf,
        "nome": name,
        "data_nascimento": birth_date,
        "endereco": address
    })

    print("Usuário cadastrado com sucesso")

def filter_user(cpf, users):
    users_filtered = [user for user in users if user["cpf"] == cpf]
    return users_filtered[0] if users_filtered else None

def create_account(account_number, users, AGENCY):
    cpf = input("Digite o CPF do usuário: ")
    user = filter_user(cpf, users)

    if user:
        print("Conta criada com sucesso")
        return {
            "agencia": AGENCY,
            "numero": account_number,
            "usuário": user
        }
    
    print("Usuário não encontrado")

def list_accounts(accounts):
    for account in accounts:
        line = f"Agência: {account['agencia']} - Conta: {account['numero']} - Titular: {account['usuário']['nome']}"
        print("=" * 100)
        print(textwrap.dedent(line))

def main():

    balance = 0
    limit = 500
    statement = ""
    withdrawals_historic = ""
    deposit_historic = ""
    number_of_withdrawals = 0
    number_of_deposits = 0
    users = []
    accounts = []
    account_number = 1
    WITHDRAW_LIMIT = 3
    AGENCY = "0001"

    while True:
        option = menu()

        if option == 'd':

            value = float(input("Digite o valor do depósito: "))
            balance, statement, number_of_deposits, deposit_historic = deposit(balance, value, statement, number_of_deposits, deposit_historic)

        elif option == 's':

            value = float(input("Digite o valor do saque: "))
            balance, statement, number_of_withdrawals, withdrawals_historic = withdraw(
                balance = balance,
                value = value,
                statement = statement,
                number_of_withdrawals = number_of_withdrawals,
                withdrawals_historic = withdrawals_historic,
                limit = limit,
                WITHDRAW_LIMIT = WITHDRAW_LIMIT
                )

        elif option == 'e':
            show_statement(balance, statement, deposit_historic, withdrawals_historic)

        elif option == 'nc':
            account = create_account(account_number, users, AGENCY)
            
            if account:
                accounts.append(account)
                account_number += 1

        elif option == 'lc':
            list_accounts(accounts)

        elif option == 'nu':
            create_user(users)

        elif option == 'q':
            break

        else:
            print("Opção inválida")

main()