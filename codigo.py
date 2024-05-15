estoque = {}  # Dicionário para armazenar os produtos e seus estoques

def adicionar_produto():
    nome_produto = input("Digite o nome do produto: ")
    estoque_produto = int(input("Digite o estoque do produto: "))
    estoque[nome_produto] = estoque_produto
    print("Produto adicionado com sucesso!")

def remover_produto():
    nome_produto = input("Digite o nome do produto que deseja remover: ")
    if nome_produto in estoque:
        del estoque[nome_produto]
        print("Produto removido com sucesso!")
    else:
        print("O produto não está no estoque.")

def atualizar_produto():
    nome_produto = input("Digite o nome do produto que deseja atualizar: ")
    if nome_produto in estoque:
        novo_estoque = int(input("Digite o novo estoque do produto: "))
        estoque[nome_produto] = novo_estoque
        print("Estoque do produto atualizado com sucesso!")
    else:
        print("O produto não está no estoque.")

def exibir_estoque():
    print("Estoque da empresa:")
    for produto, quantidade in estoque.items():
        print(f"{produto}: {quantidade}")

# Menu de opções
def menu():
    while True:
        print("\n----- Menu de Opções -----")
        print("1. Adicionar produto")
        print("2. Remover produto")
        print("3. Atualizar estoque")
        print("4. Exibir estoque")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            adicionar_produto()
        elif escolha == '2':
            remover_produto()
        elif escolha == '3':
            atualizar_produto()
        elif escolha == '4':
            exibir_estoque()
        elif escolha == '5':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

# Executando o programa
menu()