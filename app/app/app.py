menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[ncl] Novo cliente
[nco] Nova conta
[mcl] Mostrar clientes
[mco] Mostrar contas
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA = '0001'
usuarios = []
contas = []

def criar_usuario(usuarios):
    cpf = (input("Digite o número do CPF: "))
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("Já existe um cliente com esse CPF.")
            return
        
    else:
        nome = input("Digite o nome completo do cliente: ")
        data_nascimento = input("Digite a data de nascimento: ")
        rua = input("Endereço \n Digite o nome da rua: ")
        numero = input("Digite o número da casa: ")
        bairro = input("Digite o bairro: ")
        cidade = input("Digite a cidade: ")
        estado = input("Digite a sigla do estado: ")
        endereco = (f"{rua}, {numero} - {bairro} - {cidade}/{estado}")
        usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
        return usuarios

def mostrar_clientes(usuarios):
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    for usuario in usuarios:
        print(f"Nome: {usuario['nome']}, CPF: {usuario['cpf']}")
    
def mostrar_contas(contas):
    if not contas:
        print("Nenhuma conta cadastrado.")
    for conta in contas:
        print(f"Agência: {conta['agencia']}.\nNúmero da conta: {conta['numero_conta']}.\nNome do Cliente: {conta['usuario']['nome']}.")

def criar_conta(agencia, contas, usuarios):
    cpf = input("informe o CPF do cliente: ")
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            numero_conta = len(contas) + 1
            contas.append({"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario})
            print(f"Conta criada com sucesso! Número da conta: {numero_conta}")
            return contas
    print("CPF não cadastrado.")

def depositar(valor_deposito, saldo, extrato,/):
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Deposito de R$ {valor_deposito:.2f}\n"
    else:
        print("Valor de depósito inválido.")
    return saldo, extrato

def sacar(valor_sacar, saldo, extrato,limite, numero_saques, LIMITE_SAQUES, /,):
    if valor_sacar > saldo:
        print(f"Valor do saque maior que o saldo, tente um valor menor ou igual à R$ {saldo:.2f}.")
        
    elif valor_sacar > limite:
        print("Valor do saque maior que o limite por operação, tente um valor menor ou igual à R$ 500,00")
        
    elif numero_saques > LIMITE_SAQUES:
        print("Limite de saques diarios atingidos")

    elif valor_sacar > 0:
        saldo -= valor_sacar
        extrato += f"Saque de R$ {valor_sacar:.2f}\n"
        numero_saques += 1 
            
    else:    
        print("Valor de saque invalido.")
    return saldo, extrato, numero_saques

def gerar_extrato(saldo,/,*,extrato):
    print("##############EXTRATO##############")
    print("Sem movimentações na conta" if not extrato else extrato)
    print(f"Saldo na conta é de R$ {saldo:.2f}")
    print("###################################")
    return saldo, extrato

while True:
    opcao = input(menu)

    if opcao == "d":
         deposito = int(input("Digite o valor para depósito: "))
         saldo, extrato = depositar(deposito, saldo, extrato)

    elif opcao == "s":
        valor_sacar = int(input("Digite o valor a ser sacado: "))
        saldo, extrato, numero_saques = sacar(valor_sacar, saldo, extrato, limite, numero_saques, LIMITE_SAQUES)
       
    elif opcao == "ncl":
        criar_usuario(usuarios)

    elif opcao == "nco":
        contas = criar_conta(AGENCIA, contas, usuarios)

    elif opcao == "mcl":
        mostrar_clientes(usuarios)

    elif opcao == "mco":
        mostrar_contas(contas)

    elif opcao == "e":
        saldo, extrato = gerar_extrato(saldo,extrato = extrato)
    
    elif opcao == "q":
        break
    
    else:
        print("Operação invalida, por favor selecionar novamente a opção desejada.")
    