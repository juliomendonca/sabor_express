import os


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


def escolher_opcao():
    opcao_escolhida = int(input("Escolha uma opção: "))

    # função para controlar escolha das opções
    if opcao_escolhida == 1:
        nome_restaurante = input("Digite o nome do restaurante: ")
        endereco_restaurante = input("Digite o endereço do restaurante: ")
        telefone_restaurante = input("Digite o telefone do restaurante: ")
        print(
            f"Restaurante {nome_restaurante} cadastrado com sucesso! Endereço: {endereco_restaurante}, Telefone: {telefone_restaurante}."
        )
    elif opcao_escolhida == 2:
        print("Listando restaurantes...")
        # Aqui você pode adicionar a lógica para listar os restaurantes cadastrados
    elif opcao_escolhida == 3:
        nome_restaurante = input("Digite o nome do restaurante a ser ativado: ")
        print(f"Restaurante {nome_restaurante} ativado com sucesso!")
    else:
        finalizar_app()


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
