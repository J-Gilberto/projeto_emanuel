# def menu_principal():
#     print('\n===== Sistema de Gerenciamento de vendas =====')
#     print('1. Cadastrar novo produto.')
#     print('2. Registrar venda')
#     print('3. Consultar produtos em estoque.')
#     print('4. Relatório de produtos com estoque baixo.')
#     print('5. Valor todal do estoque.')
#     print('6. Análise de vendas por categoria.')
#     print('7. Sair')
#     return input('Esolha uma opção: ')

# def main():
#     estoque = {}
#     categorias = set()
#     vendas = []
#     while True:
#         opcao = menu_principal()
#         if menu_principal == '1':
#             nome = input('Entre com o nome do produto: ')

            
# if __name__ == '__main__':
#     main()



# Estruturas de Dados Iniciais
estoque = {}  # Dicionário para armazenar informações dos produtos
categorias = set()  # Conjunto para gerenciar categorias únicas
vendas = []  # Lista para guardar o histórico de vendas



# Funções do Sistema
def menu_principal():
    """Exibe o menu principal"""
    print("\n===== Sistema de Gerenciamento de Vendas =====")
    print("1. Cadastrar novo produto")
    print("2. Registrar venda")
    print("3. Consultar produtos disponíveis")
    print("4. Relatório de produtos com estoque baixo")
    print("5. Valor total do estoque")
    print("6. Análise de vendas por categoria")
    print("7. Sair")
    return input("Escolha uma opção: ")

def cadastrar_produto(estoque, categorias):
    """Função para cadastrar um novo produto"""
    codigo = input("Código do produto: ")
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: "))
    quantidade = int(input("Quantidade em estoque: "))
    categoria = input("Categoria do produto: ")

    estoque[codigo] = {"nome": nome, "preco": preco, "quantidade": quantidade, "categoria": categoria}
    categorias.add(categoria)
    print("Produto cadastrado com sucesso!")

def registrar_venda(estoque, vendas):
    """Função para registrar uma venda e atualizar o estoque"""
    codigo = input("Código do produto vendido: ")
    if codigo in estoque:
        quantidade_vendida = int(input("Quantidade vendida: "))
        if estoque[codigo]["quantidade"] >= quantidade_vendida:
            estoque[codigo]["quantidade"] -= quantidade_vendida
            vendas.append({"codigo": codigo, "quantidade": quantidade_vendida, "categoria": estoque[codigo]["categoria"]})
            print("Venda registrada com sucesso!")
        else:
            print("Estoque insuficiente!")
    else:
        print("Produto não encontrado!")

def consultar_produtos(estoque):
    """Exibe produtos disponíveis"""
    print("\nProdutos disponíveis:")
    for codigo, dados in estoque.items():
        print(f"Código: {codigo}, Nome: {dados['nome']}, Quantidade: {dados['quantidade']}")

def relatorio_estoque_baixo(estoque):
    """Relatório de produtos com estoque baixo"""
    print("\nProdutos com estoque baixo:")
    for codigo, dados in estoque.items():
        if dados["quantidade"] < 5:
            print(f"Código: {codigo}, Nome: {dados['nome']}, Quantidade: {dados['quantidade']}")

def valor_total_estoque(estoque):
    """Calcula o valor total do estoque"""
    total = sum(dados["preco"] * dados["quantidade"] for dados in estoque.values())
    print(f"\nValor total em estoque: R$ {total:.2f}")

def analise_vendas_categoria(vendas):
    """Análise de vendas por categoria"""
    categorias_vendas = {}
    for venda in vendas:
        categoria = venda["categoria"]
        categorias_vendas[categoria] = categorias_vendas.get(categoria, 0) + venda["quantidade"]

    print("\nVendas por categoria:")
    for categoria, quantidade in categorias_vendas.items():
        print(f"Categoria: {categoria}, Quantidade Vendida: {quantidade}")

# Função Principal
def main():
    while True:
        opcao = menu_principal()
        if opcao == "1":
            cadastrar_produto(estoque, categorias)
        elif opcao == "2":
            registrar_venda(estoque, vendas)
        elif opcao == "3":
            consultar_produtos(estoque)
        elif opcao == "4":
            relatorio_estoque_baixo(estoque)
        elif opcao == "5":
            valor_total_estoque(estoque)
        elif opcao == "6":
            analise_vendas_categoria(vendas)
        elif opcao == "7":
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()

    