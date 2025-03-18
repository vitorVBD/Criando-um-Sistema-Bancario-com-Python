import textwrap
from datetime import datetime
from models.cliente import Cliente
from models.conta_corrente import Conta_Corrente
from models.deposito import Deposito
from models.historico import Historico
from models.pessoa_fisica import Pessoa_Fisica
from models.saque import Saque
from models.transacao import Transacao
from models.contas_iterador import Contas_Iterador

def log_transacao(func):
    def envelope(*args, **kwargs):
        resultado = func(*args, **kwargs)
        print(f"{datetime.now()}: {func.__name__.upper()}")
        return resultado
    return envelope

def menu(): 
    menu = """\n
    ===============MENU===============

    [r]\tRealizar Transação
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuário
    [q]\tSair

=>"""
    return input(textwrap.dedent(menu))

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("Cliente não possui conta")
        return
    return cliente.contas[0]

@log_transacao
def transacao(clientes):
    cpf = input("Digite o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado")
        return

    tipo_transacao = input(""""
    "Digite o tipo de transação: 
    [d]\tDeposito
    [s]\tSaque
    """)

    if tipo_transacao == "d":
        valor = float(input("Digite o valor do depósito: "))
        transacao = Deposito(valor)
        
        conta = recuperar_conta_cliente(cliente)
        if not conta:
            print("Cliente não possui conta")
            return
    
        cliente.realizar_transacao(conta, transacao)

    elif tipo_transacao == "s":
        valor = float(input("Digite o valor do saque: "))
        transacao = Saque(valor)

        conta = recuperar_conta_cliente(cliente)
        if not conta:
            print("Cliente não possui conta")
            return
        
        cliente.realizar_transacao(conta, transacao)    


@log_transacao
def exibir_extrato(clientes):
    cpf = input("Digite o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado")
        return
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        print("Cliente não possui conta")
        return
    
    print("\n=================EXTRATO=================")
    extrato = ""
    tem_transacao = False
    for transacao in conta.historico.gerar_relatorio(tipo_transacao="saque"):
        tem_transacao = True
        extrato += f"{transacao['tipo']}:\n\tR${transacao['valor']:.2f}:\n\t"
    
    if not tem_transacao:
        extrato = "Não foram realizadas movimentações na conta"

    print(extrato)
    print(f"\nSaldo:\n\tR${conta.saldo:.2f}")
    print("========================================")

@log_transacao
def criar_conta(numero_conta, clientes, contas):
    cpf = input("Digite o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado")
        return

    conta = Conta_Corrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print(f"Conta criada com sucesso! Número da conta: {numero_conta}")

def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))

@log_transacao
def criar_cliente(clientes):
    cpf = input("Digite o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("Cliente já cadastrado")
        return
    
    nome = input("Digite o nome do cliente: ")
    data_nascimento = input("Digite a data de nascimento do cliente (dd-mm-aaaa): ")
    endereco = input("Digite o endereço do cliente (logradouro, nro - bairro - cidade/uf): ")

    cliente = Pessoa_Fisica(cpf=cpf, nome=nome, data_nascimento=data_nascimento, endereco=endereco)
    clientes.append(cliente)

    print("Cliente cadastrado com sucesso!")
    
def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "r":
            transacao(clientes)

        elif opcao == "e":
            exibir_extrato(clientes)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "nu":
            criar_cliente(clientes)

        elif opcao == "lc":
            listar_contas(contas)


        elif opcao == "q":
            print("Saindo do sistema")
            break

        else:
            print("Opção inválida")

main()