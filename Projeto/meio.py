
'''
 Você foi contratado para desenvolver um sistema básico de gerenciamento de vendas para uma
 pequena empresa. O sistema deve permitir o cadastro de produtos, registro de vendas, análise de
 estoque e geração de relatórios simples.
 Requisitos

 Desenvolva um programa em Python que atenda às seguintes funcionalidades:
 1. Cadastro de produtos (código, nome, preço, quantidade em estoque e categoria)
 2. Registro de vendas com atualização automática do estoque
 3. Consulta de produtos disponíveis
 4. Relatório de produtos com estoque baixo (menos de 5 unidades)
 5. Cálculo do valor total em estoque
 6. Análise de vendas por categoria

 Conceitos que devem ser aplicados

 1. Estruturas de dados
 Dicionários: Para armazenar informações dos produtos
 Listas: Para guardar histórico de vendas
 Conjuntos: Para manipular categorias de produtos sem repetição

 2. Programação estruturada
 Funções: Para organizar cada funcionalidade do sistema
 Estruturas condicionais: Para validação de dados e decisões lógicas
 Estruturas de repetição: Para percorrer coleções de dados
 Manipulação de textos: Para formatação de saídas
 Operações booleanas: Para validações e verificações

 3. Entrada e saída de dados
Captura de dados inseridos pelo usuário
 Exibição de informações formatadas no console
 Exemplo de Estrutura do Código

 # Inicialização de estruturas de dados
 estoque = {}  # Dicionário vazio para o estoque
 categorias = set()  # Conjunto vazio para categorias
 vendas = []  # Lista vazia para o histórico de vendas

 def menu_principal():
 """Exibe o menu principal do sistema"""
 print("\n===== Sistema de Gerenciamento de Vendas =====")
 print("1. Cadastrar novo produto")
 print("2. Registrar venda")
 print("3. Consultar produtos em estoque")
 print("4. Relatório de produtos com estoque baixo")
 print("5. Valor total do estoque")
 print("6. Análise de vendas por categoria")
 print("7. Sair")
 return input("Escolha uma opção: ")

 def cadastrar_produto(estoque, categorias):
 """
 Função para cadastrar um novo produto no sistema
 Retorna o estoque e categorias atualizados
 """
 # Implementar lógica de cadastro aqui
 pass
 def registrar_venda(estoque, vendas):
 """
 Função para registrar uma venda e atualizar o estoque
 Retorna o estoque e histórico de vendas atualizados
 """
 # Implementar lógica de vendas aqui
 pass
 # Demais funções para as outras funcionalidades
 # ...
 def main():
 """Função principal que executa o programa"""
 # Dicionário para armazenar os produtos
    estoque = {}
    
    # Conjunto para armazenar as categorias sem repetição
    categorias = set()
    
    # Lista para armazenar histórico de vendas
    vendas = []
    
    # Loop principal do programa
    while True:
        opcao = menu_principal()
        
        # Implementar estrutura condicional para as opções do menu
        # ...
 if __name__ == "__main__":
    main(
'''


estoque = {}
categorias = set()
vendas = []

def menu_inicial(): # menu inicial
    print(f'\n*** Sistema de Gereciamento de Vendas ***\n')
    print("1. Cadastrar novo produto")
    print("2. Registrar venda")
    print("3. Consultar produtos em estoque")
    print("4. Relatório de produtos com estoque baixo")
    print("5. Valor total do estoque")
    print("6. Análise de vendas por categoria")
    print("7. Sair\n")
    return input("Escolha uma opção: ")
# menu_inicial() vou manter todos os testes comentados.


def cadastro_item(estoque, categorias):
    codigo = int(input(f'Entre com o codigo do produto: '))
    nome = input(f'Entre com o nome do produto: ')
    categoria = input(f'Entre com a categoria do profuto: ')
    preco = float(input(f'Entre com o valor do produto: R$ '))
    quantidade = int(input(f'Entre com a quantidade do produto: '))

    estoque[codigo] = {
        'nome' : nome,
        'categoria' : categoria,
        'preco' : preco,
        'quantidade' : quantidade
        }
    categorias.add(categoria)
    print(f'Produto cadastrado com sucesso!')
# cadastro_item(estoque, categorias)


def registrar_venda(estoque, vendas):
    codigo = int(input(f'Entre com o codigo do item vendido: '))
    if codigo in estoque:
        venda = int(input(f'Entre com a quantidade de items vendidos: '))
        if int(estoque[codigo]['quantidade'] >= venda):
           estoque[codigo]['quantidade'] -= venda
           vendas.append({
               'codigo': codigo, 
               'quantidade' : venda,
               'categoria' : estoque[codigo]['categoria']
               })
           print(f'Venda concluida!')
        else:
            print(f'Estoque em baixa, não foi possivel efetuar a venda.') 
    else:
        print(f'Produto não localizado!')
# registrar_venda(estoque, vendas)

def consulta_item(estoque):
    print(f'\n*** Produtos do estoque ***\n')
    for codigo, info in estoque.items():
        print(f'Código: {codigo}, Nome: {info["nome"]}, Quantidade: {info["quantidade"]}')
consulta_item(estoque)           
    





