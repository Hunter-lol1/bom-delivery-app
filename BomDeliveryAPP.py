import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False},
                {'nome':'Pizza Suprema', 'categoria':'pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Francesa', 'ativo':False}]

def exibir_nome_do_programa():
    '''Exibe o nome estilizado do programa na tela'''
    print('''
██████╗░░█████╗░███╗░░░███╗  ██████╗░███████╗██╗░░░░░██╗██╗░░░██╗███████╗██████╗░██╗░░░██╗
██╔══██╗██╔══██╗████╗░████║  ██╔══██╗██╔════╝██║░░░░░██║██║░░░██║██╔════╝██╔══██╗╚██╗░██╔╝
██████╦╝██║░░██║██╔████╔██║  ██║░░██║█████╗░░██║░░░░░██║╚██╗░██╔╝█████╗░░██████╔╝░╚████╔╝░
██╔══██╗██║░░██║██║╚██╔╝██║  ██║░░██║██╔══╝░░██║░░░░░██║░╚████╔╝░██╔══╝░░██╔══██╗░░╚██╔╝░░
██████╦╝╚█████╔╝██║░╚═╝░██║  ██████╔╝███████╗███████╗██║░░╚██╔╝░░███████╗██║░░██║░░░██║░░░
╚═════╝░░╚════╝░╚═╝░░░░░╚═╝  ╚═════╝░╚══════╝╚══════╝╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░
      ''')

def exibir_opcoes():
    '''Exibe as opções disponíveis no menu principal'''

    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''Exibe a mensagem de finalização do app'''

    exibir_subtitulo('Encerrando app')

def voltar_ao_menu_principal():
    '''Solicita uma tecla para voltar ao menu principal 
    
    Outputs:
    - Retorna ao menu principal

    '''
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def opcao_invalida():
    '''Exibe mensagem de opção inválida e retorna ao menu principal 
    
    Outputs:
    - Retorna ao menu principal

    '''
    print('Opção inválida\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    ''' Exibe um subtítulo estilizado na tela 
    
    Inputs:
    - texto: str - O texto do subtítulo

    '''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante
    
    Inputs:
    - nome
    - categoria
    
    Outputs:
    - adiciona um novo restaurante a lista de restaurantes

    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_restaurante = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria_restaurante, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')

    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Essa função é responsável por listar os restaurantes cadastrados
    
    Outputs:
   - Exibe a lista de restaurantes na tela
    
    '''
    exibir_subtitulo('Listando os restaurantes')
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo_restaurante = 'ativado' if  restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo_restaurante}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    '''Essa função é responsável por ativar ou desativar um restaurante cadastrado
    
    Outputs:
    - Exibe a mensagem indicando o sucesso na operação
    
    '''
    exibir_subtitulo('Alternando o estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado!')

    voltar_ao_menu_principal()

def escolher_opcao():
    '''Solicita e executa a opção escolhida pelo usuário
    
    Outputs:
    - Executa a opção escolhida pelo usuário
    
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except: opcao_invalida()

def main():
    '''Função principal que inicia o programa'''
    
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
