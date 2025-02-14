import os

restaurantes = [{'nome' : 'Praça', 'catgoria' : 'Japonesa', 'ativo':False}, {}]

def exibir_nome_do_programa():
    print("PICANHA EXPRESS")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('finalizar app')

def voltar_ao_menu():
    input('Digite uma tecla voltar para menu principal: ')
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()


def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurante')
    print('Cadastro de restaurantes novos')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado')
    voltar_ao_menu()

def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')

    for restaurante in restaurantes:
        print(f".{restaurante}")

    voltar_ao_menu()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1: 
           cadastrar_novo_restaurante() 
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            print('Ativar restaurante')
        elif opcao_escolhida == 4: 
            finalizar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()