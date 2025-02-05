import os

restaurantes = [
    {
        'nome': 'BK',
        'status': 'Desativado'
    },
    {
        'nome': 'MC',
        'status': 'Ativado'
    }
]

def exibir_nome_programa():
    print('Sabor Express\n')

def voltar_ao_menu():
    input('Digite qualquer tecla para tentar novamente:')
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alterar status do restaurante')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls')
    print('Finalizando o app')

def opcao_invalida():
    print('Opção inválida\n')
    voltar_ao_menu()

def alterar_status_restaurante(index_escolhido):
    for index, restaurante in enumerate(restaurantes):
        if index+1 == index_escolhido:
            nome_restaurante = restaurante['nome']
            status_atual = True if restaurante['status'] == 'Ativado' else False
            novo_status = ''
            if status_atual:
                novo_status = 'Desativado'
                restaurante['status'] = novo_status
            else:
                novo_status = 'Ativado'
                restaurante['status'] = novo_status
    print(f'Status do restaurante {nome_restaurante} foi alterado para {novo_status.lower()}')
    listar_restaurantes(0)


def listar_restaurantes(opcao):
    print(f"{'Número'.ljust(10)} {'Nome'.ljust(20)} {'Status'.ljust(6)}")
    for index, restaurante in enumerate(restaurantes):
        nome_restaurante = restaurante['nome']
        status_restaurante = restaurante['status']
        index_restaurante = str(index + 1)
        print(f'{index_restaurante.ljust(10)} {nome_restaurante.ljust(20)} | {status_restaurante.ljust(10)}')
    if opcao != 3: 
        voltar_ao_menu()

def cadastrar_novo_restaurante():
     novo_restaurante = str(input('Digite o nome do restaurante:'))
     status = int(input('[1] Ativado [2] Desativado: '))
     restaurantes.append({'nome': novo_restaurante, 'status': 'Ativado' if status == 1 else 'Desativado'})
     print(f'Restaurante {novo_restaurante} foi cadastrado com sucesso!')
     voltar_ao_menu()

def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma das opções:'))
        if opcao_escolhida == 1:
            exibir_subtitulo('Cadastrar restaurante')
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            exibir_subtitulo('Listar restaurantes')
            listar_restaurantes(2)
        elif opcao_escolhida == 3:
            exibir_subtitulo('Alterar status do restaurante')
            listar_restaurantes(3)
            escolha_restaurante_status = int(input('Digite o número do restaurante:'))
            alterar_status_restaurante(escolha_restaurante_status)
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcoes()


if __name__ == '__main__':
    main()