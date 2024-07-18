from PessoaFisica import PessoaFisica
from Conta_Corrente import Conta_Corrente
from Saque import Saque
from Deposito import Deposito

def buscar_cliente(cpf, clientes):
    buscar = [cliente for cliente in clientes if cpf == cliente.cpf]
    return buscar[0] if buscar else None

def filtra_cliente(cliente):
    if not cliente.contas:
        print("\n Cliente não possui conta! ")
        return None
    return cliente.contas[0]

def cadastrar_cliente(clientes):
    cpf = input("Digite o CPF: ")
    cliente = buscar_cliente(cpf, clientes)
    if cliente:
        print("Cliente já cadastrado!")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    cliente = PessoaFisica(nome=nome, cpf=cpf, data_nascimento=data_nascimento, endereco=endereco)
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")

def criar_conta(numero_conta, clientes, contas):
    cpf = input("Digite o CPF: ")
    cliente = buscar_cliente(cpf, clientes)
    if not cliente:
        print("Cliente não encontrado!")
        return
    conta = Conta_Corrente(numero=numero_conta, cliente=cliente)
    contas.append(conta)
    cliente.adicionar_conta(conta)
    print("Conta criada com sucesso!")

def depositar_dinheiro(clientes):
    cpf = input("Digite o CPF: ")
    cliente = buscar_cliente(cpf, clientes)
    if not cliente:
        print("Cliente não encontrado!")
        return
    conta = filtra_cliente(cliente)
    if not conta:
        return
    valor = float(input("Digite o valor para depósito: "))
    deposito = Deposito(valor)
    cliente.realizar_transacao(conta, deposito)

def sacar_dinheiro(clientes):
    cpf = input("Digite o CPF: ")
    cliente = buscar_cliente(cpf, clientes)
    if not cliente:
        print("Cliente não encontrado!")
        return
    conta = filtra_cliente(cliente)
    if not conta:
        return
    valor = float(input("Digite o valor para saque: "))
    saque = Saque(valor)
    cliente.realizar_transacao(conta, saque)

def imprimir_extrato(clientes):
    cpf = input("Digite o CPF: ")
    cliente = buscar_cliente(cpf, clientes)
    if not cliente:
        print("Cliente não encontrado!")
        return
    conta = filtra_cliente(cliente)
    if not conta:
        return
    print("\nExtrato da Conta:")
    for transacao in conta.retorna_historico.transacao:
        print(f"{transacao['data']} - {transacao['tipo']}: {transacao['valor']}")
    print(f"Saldo atual: {conta.retorna_saldo}")

def main():
    clientes = []
    contas = []
    numero_conta = 1

    while True:
        print("\n=== Sistema Bancário ===")
        print("1. Cadastrar Cliente")
        print("2. Criar Conta")
        print("3. Depositar Dinheiro")
        print("4. Sacar Dinheiro")
        print("5. Imprimir Extrato")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_cliente(clientes)
        elif opcao == '2':
            criar_conta(numero_conta, clientes, contas)
            numero_conta += 1
        elif opcao == '3':
            depositar_dinheiro(clientes)
        elif opcao == '4':
            sacar_dinheiro(clientes)
        elif opcao == '5':
            imprimir_extrato(clientes)
        elif opcao == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
