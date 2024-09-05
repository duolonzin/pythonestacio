# O programa em si é simples e direto para facil entendimento.
# Dicionário para armazenar os produtos e quantidades no estoque
estoque = {
    "Oleo comum": 5,
    "Cabo CG/Honda": 7,
    "Kit relacao padrao": 3,
    "Esticador de corrente": 6,
    "Camera de ar": 15,
    "Rele partida": 5,
    "Farol Yamaha": 7,
    "Piscas": 0,
    "Filtro ar": 0,
    "Filtro oleo": 0,
    "Manopla": 0
}

# Função para exibir o estoque atual
# Percorre o dicionário e exibe cada produto com sua respectiva quantidade


def exibir_estoque():
    print("\nEstoque atual da Leo Racing Motos:")
    for produto, quantidade in estoque.items():
        print(f"{produto}: {quantidade} unidades")

# Função para adicionar ou atualizar um produto no estoque
# Recebe o nome do produto e a quantidade e os armazena no dicionário


def adicionar_produto():
    produto = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade do produto: "))
    estoque[produto] = quantidade
    print(f"{produto} adicionado ao estoque da Leo Racing Motos com {
          quantidade} unidades.")


# Menu simples para navegação
# O loop continua até que o usuário escolha a opção de sair
while True:
    # Exibe as opções do menu
    print("\n--- Bem-vindo à Leo Racing Motos ---")
    print("1. Exibir estoque")
    print("2. Adicionar produto")
    print("3. Sair")

    # Lê a opção escolhida pelo usuário
    opcao = input("Escolha uma opção: ")

    # Opção 1: Exibe o estoque chamando a função exibir_estoque()
    if opcao == "1":
        exibir_estoque()

    # Opção 2: Permite adicionar ou atualizar um produto chamando a função adicionar_produto()
    elif opcao == "2":
        adicionar_produto()

    # Opção 3: Encerra o programa
    elif opcao == "3":
        print("Saindo do sistema da Leo Racing Motos...")
        break

    # Caso a opção não seja válida, exibe uma mensagem de erro
    else:
        print("Opção inválida. Tente novamente.")
