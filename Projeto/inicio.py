estoque = {}
categorias = set()
vendas = []

def menu_inicial():
    print('\n***** Sistema de Gerenciamento de Vendas *****\n')
    print('Digite 1. Cadastro de novos produtos')
    print('Digite 2. Vendas')
    print('Digite 3. Consulta de produtos disponíveis')
    print('Digite 4. Relatório de itens com o estoque baixo.')
    print('Digite 5. Valor total em estoque.')
    print('Digite 6. Análise de vendas por categoria.')
    print('Digite 7. Para sair do programa.\n')
    return input("Escolha uma opção: ")

def cadastro(estoque, categorias):
    codigo = int(input('Entre com o código do produto: '))
    nome = input('Entre com o nome do produto: ')
    valor = float(input('Entre com o valor do produto: '))
    quantidade = int(input('Entre com a quantidade de itens: '))
    categoria = input('Entre com a categoria: ')

    estoque[codigo] = {'nome': nome, 'valor': valor, 'quantidade': quantidade, 'categoria': categoria}
    categorias.add(categoria)
    print('Cadastrado com sucesso!')

def registro_de_vendas(estoque, vendas):
    codigo = input('Código do produto vendido: ')
    if codigo in estoque:
        venda = int(input('Quantidade vendida: '))
        if int(estoque[codigo]['quantidade']) >= venda:
            estoque[codigo]['quantidade'] -= venda
            vendas.append({'codigo': codigo, 'quantidade': venda, 'categoria': estoque[codigo]['categoria']})
            print('Venda efetuada!')
        else:
            print('Estoque baixo, não é possível efetuar a venda.')
    else:
        print('Produto não localizado.')

def consulta_de_produtos(estoque):
    print('\n* Produtos no estoque *')
    for codigo, informacao in estoque.items():
        print(f'Código: {codigo}, Nome: {informacao["nome"]}, Quantidade: {informacao["quantidade"]}')

def informacao_estoque_em_baixa(estoque):
    print('\nProdutos com estoque em baixa:')
    for codigo, informacao in estoque.items():
        if int(informacao['quantidade']) < 5:
            print(f'Código: {codigo}, Nome: {informacao["nome"]}, Quantidade: {informacao["quantidade"]}')

def valor_total(estoque):
    total_valor = sum(float(informacao['valor']) * int(informacao['quantidade']) for informacao in estoque.values())
    print(f'\nValor total do estoque é R$ {total_valor:.2f}')

def analise_vendas(vendas):
    vendas_por_categorias = {}
    for venda in vendas:
        categoria = venda['categoria']
        vendas_por_categorias[categoria] = vendas_por_categorias.get(categoria, 0) + venda['quantidade']
    print('\nVendas por categoria:')
    for categoria, quantidade in vendas_por_categorias.items():
        print(f'Categoria: {categoria}, Total vendidos: {quantidade}')

def main():
    while True:
        opcao = int(menu_inicial())
        if opcao == 1:
            cadastro(estoque, categorias)
        elif opcao == 2:
            registro_de_vendas(estoque, vendas)
        elif opcao == 3:
            consulta_de_produtos(estoque)
        elif opcao == 4:
            informacao_estoque_em_baixa(estoque)
        elif opcao == 5:
            valor_total(estoque)
        elif opcao == 6:
            analise_vendas(vendas)
        elif opcao == 7:
            print('Saindo do programa!')
            break
        else:
            print('Opção inválida!')

if __name__ == "__main__":
    main()

'''
OBS: Preciso focar mais nestes assunto

    1° Conjuntos (set): A estrutura set é usada para armazenar elementos únicos, ou seja, 
    sem duplicatas. Se você tentar adicionar ao conjunto um valor que já existe, ele simplesmente 
    será ignorado, sem gerar erros.
    2° Função add: O método add() é utilizado em conjuntos para incluir um novo elemento. 
    Ele adiciona o valor apenas se ele ainda não estiver no conjunto.
'''

