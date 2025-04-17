import os


def escolher_opcao():
    opcao_escolhida = int(input("Escolha uma opção: "))

    match opcao_escolhida:
        case 1:
            print("Adicionar restaurante")
        case 2:
            print("Listar restaurantes")
        case 3:
            print("Ativar restaurante")
        case 4:
            finalizar_app()
        case _:
            print("Opção inválida!")


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


# função principal
def main():
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
