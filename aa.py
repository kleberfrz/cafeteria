# Sistema Cafeteria Tia Rosa

# Listas para armazenar dados
produtos = []
clientes = []
pedidos = []

# Função para cadastrar produto
def cadastrar_produto():
    print("\n📦 Cadastro de Produto")
    nome = input("Nome: ")
    preco = float(input("Preço: R$ "))
    ingredientes = input("Ingredientes: ")
    promocao = input("Está em promoção? (s/n): ").lower() == 's'
    produtos.append({
        "nome": nome,
        "preco": preco,
        "ingredientes": ingredientes,
        "promocao": promocao
    })
    print("✅ Produto cadastrado com sucesso!")

# Função para listar produtos
def listar_produtos():
    print("\n📋 Cardápio:")
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    for p in produtos:
        promo = "🔥 Promoção!" if p["promocao"] else ""
        print(f"- {p['nome']} | R$ {p['preco']:.2f} | {p['ingredientes']} {promo}")

# Função para cadastrar cliente
def cadastrar_cliente():
    print("\n🧑 Cadastro de Cliente")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    cpf = input("CPF: ")
    clientes.append({
        "nome": nome,
        "telefone": telefone,
        "cpf": cpf
    })
    print("✅ Cliente cadastrado com sucesso!")

# Função para registrar pedido
def registrar_pedido():
    print("\n📝 Registro de Pedido")
    cpf = input("CPF do cliente: ")
    cliente = next((c for c in clientes if c["cpf"] == cpf), None)
    if not cliente:
        print("❌ Cliente não encontrado. Cadastre primeiro.")
        return

    listar_produtos()
    pedido = []
    while True:
        item = input("Digite o nome do produto (ou 'fim' para encerrar): ")
        if item.lower() == 'fim':
            break
        produto = next((p for p in produtos if p["nome"].lower() == item.lower()), None)
        if produto:
            pedido.append(produto)
        else:
            print("❌ Produto não encontrado.")

    if not pedido:
        print("⚠️ Nenhum item foi selecionado.")
        return

    total = sum(p["preco"] for p in pedido)
    pedidos.append({
        "cliente": cliente,
        "itens": pedido,
        "total": total
    })
    print(f"✅ Pedido registrado! Total: R$ {total:.2f}")

# Função para relatório de vendas
def relatorio_vendas():
    print("\n📊 Relatório de Vendas")
    if not pedidos:
        print("Nenhum pedido registrado.")
        return
    total_geral = 0
    for p in pedidos:
        print(f"- Cliente: {p['cliente']['nome']} | Total: R$ {p['total']:.2f}")
        total_geral += p["total"]
    print(f"\n💰 Total arrecadado: R$ {total_geral:.2f}")

# Menu principal
def menu():
    while True:
        print("\n=== Sistema Cafeteria Tia Rosa ===")
        print("1. Cadastrar produto")
        print("2. Listar produtos")
        print("3. Cadastrar cliente")
        print("4. Registrar pedido")
        print("5. Relatório de vendas")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            cadastrar_cliente()
        elif opcao == "4":
            registrar_pedido()
        elif opcao == "5":
            relatorio_vendas()
        elif opcao == "0":
            print("👋 Saindo do sistema...")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

# Iniciar o sistema
menu()
