import os

restaurantes = ["Pizza Mia", "Sushi House", "Burger King"]


def cadastrar_novo_restaurante():
    os.system("cls")
    print("Cadastro de novos restaurantes\n")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar:")
    restaurantes.append(nome_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!")
    voltar_menu_principal()


def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                print("Ativar restaurante")
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except Exception:
        opcao_invalida()


def exibir_nome_do_programa():
    print(
        """

    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """
    )


def exibir_opcoes():
    print("1. Cadastrar Restaurante")
    print("2. Listar Restaurantes")
    print("3. Ativar Restaurante")
    print("4. Sair\n")


# função para finalizar app
def finalizar_app():
    os.system("cls")
    print("Finalizando o aplicativo...\n")
    exit()


def listar_restaurantes():
    os.system("cls")
    print("Lista de Restaurantes\n")
    for i, restaurante in enumerate(restaurantes, start=1):
        print(f"{i}. {restaurante}")
    print("\n")
    voltar_menu_principal()


def opcao_invalida():
    print("Opção Inválida!\n")
    voltar_menu_principal()


def voltar_menu_principal():
    input("Digite uma tecla para voltar ao menu principal")
    main()


# função principal
def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

    while True:
        continuar = input("Deseja continuar? (s/n): ").lower()
        if continuar == "s":
            os.system("cls")
            exibir_opcoes()
            escolher_opcao()
        elif continuar == "n":
            finalizar_app()
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
