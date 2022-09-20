import PySimpleGUI as sg
import back
from webbrowser import open

gitLink = 'https://app.powerbi.com/' \
          'view?r=eyJrIjoiZDQ5M2RlMGQtMzZ' \
          'jZi00Y2U2LWE0YWUtZTMwNmZkYjM0N2E' \
          'zIiwidCI6ImZhNGNkYjlhLThkMDQtNDJmMy1i' \
          'ODMwLWU0N2I3YmFmMTdmZiIsImMiOjF9'
sg.theme('DarkBlue14')


def front():
    global fun_cod
    # LAYOUT DA JANELA INICIAL
    flayout = [
        [sg.Text('')],
        [sg.Text('Usuario'), sg.Input(key='usuario', size=(20, 1))],
        [sg.Text('Senha  '), sg.Input(key='senha', password_char='*', size=(20, 1))],
        [sg.Text('')],
        [sg.Text('                '), sg.Button('Entrar', size=(6, 2))]
    ]

    # ATRIBUINDO E CONFIGURANDO A JANELA
    janela = sg.Window('Página Inicial', flayout, size=(239, 150))

    # VERIFICAÇÃO LOGIN E SENHA
    while True:
        # ATRIBUIÇÃO DA CONEXÃO COM A FUNÇÃO E DO CURSOR
        cnx = back.conexao()
        cursor = cnx.cursor()

        # RECEBIMENTO DOS EVENTOS E VALORES DA JANELA FRONT
        evento, valores = janela.read()

        if evento == sg.WINDOW_CLOSED:
            break

        if evento == 'Entrar':
            usuariopy = int(valores['usuario'])
            senhapy = int(valores['senha'])

            cursor.execute(f"select fun_cod from funcionario where fun_cod = {usuariopy}")
            usuariosql = cursor.fetchall()

            # VERIFICAÇÃO DO CÓDIGO DO USUÁRIO
            if not usuariosql:
                print("Usuário Não Encontrado!")

            # VERIFICAÇÃO DA SENHA DO USUÁRIO
            elif usuariopy in usuariosql[0]:
                cursor.execute(f"select fun_senha from funcionario where fun_cod= {usuariopy}")
                senhasql = cursor.fetchall()
                fun_cod = usuariopy
                if senhapy in senhasql[0]:
                    print("Login Realizado Com Sucesso!")
                    janela.close()
                    selecao()
                else:
                    print("Senha Inválida!")

            cnx.commit()
            cnx.close()


def selecao():
    # PÁGINA PARA SELEÇÃO DOS SETORES
    pagina_selecao = [
        [sg.Text(' ')],
        [sg.Text('Selecione o Setor')],
        [sg.Text(' ')],
        [sg.Button('Vendas', size=(8, 3)), sg.Button('Produtos', size=(8, 3))],
        [sg.Text(' ')],
        [sg.Text('Acessar Relatório', enable_events=True, key='Link'), sg.Text('|'),
         sg.Text('Finalizar Acesso', enable_events=True, key='Sair')],
    ]

    # ATRIBUIÇÃO DOS EVENTOS E VALORES
    pagina_2 = sg.Window('Setores', pagina_selecao, size=(300, 210), element_justification='center')
    evento_pag_2, valor_pag_2 = pagina_2.read()

    # EXECUÇÃO DA JANELA E AÇÕES
    while True:

        if evento_pag_2 == sg.WINDOW_CLOSED:
            pagina_2.close()

        if evento_pag_2 == 'Link':
            open(gitLink)
            break

        if evento_pag_2 == 'Vendas':
            back.filtrar_venda(fun_cod)
            pagina_2.close()
            area_vendas()

        if evento_pag_2 == 'Produtos':
            pagina_2.close()
            area_produtos()

        if evento_pag_2 == 'Sair':
            pagina_2.close()


def area_vendas():
    minhas_vendas = list(back.filtrar_venda(fun_cod))
    print(back.filtrar_venda(fun_cod))
    cabecalho = ['Cód. Venda', 'Data da Venda', 'Total da Venda']
    area_venda = [
        [sg.Text('Minhas Vendas')],
        [sg.Table(
            values=minhas_vendas,
            headings=cabecalho,
            header_border_width=3,
            header_text_color='#FFFFFF',
            header_background_color='#3C3F41',
            row_height=22,
            alternating_row_color='#0765B6',
            background_color='#283B5B',
            num_rows=10,
            key='minha_venda',
            auto_size_columns=True,
            justification='center')],
        [sg.Button('Voltar', size=(20, 2)), sg.Button('Realizar Venda', size=(20, 2))]
    ]
    pagina_3 = sg.Window('Área de Vendas', area_venda, element_justification='center')
    evento_pag_3, valor_pag_3 = pagina_3.read()

    while True:

        if evento_pag_3 == sg.WINDOW_CLOSED:
            pagina_3.close()

        if evento_pag_3 == 'Voltar':
            pagina_3.close()
            selecao()

        if evento_pag_3 == 'Realizar Venda':
            pagina_3.close()
            realizar_venda()


def area_produtos():
    lista_produtos = list(back.consultar_produtos())
    cabecalho = ['Cód. Produto', 'Item', 'Valor', 'Estoque']
    area_produto = [
        [sg.Text('Lista de Produtos')],
        [sg.Table(
            values=lista_produtos,
            headings=cabecalho,
            header_border_width=3,
            header_text_color='#FFFFFF',
            header_background_color='#3C3F41',
            row_height=22,
            alternating_row_color='#0765B6',
            background_color='#283B5B',
            num_rows=10,
            key='box',
            auto_size_columns=True,
            justification='center')],
        [sg.Button('Voltar', size=(20, 2)), sg.Button('Cadastrar Produtos', size=(20, 2))]
    ]
    pagina_4 = sg.Window('Área dos Produtos', area_produto, element_justification='center')
    evento_pag_4, valor_pag_4 = pagina_4.read()

    while True:
        if evento_pag_4 == sg.WINDOW_CLOSED:
            pagina_4.close()

        if evento_pag_4 == 'Voltar':
            pagina_4.close()
            selecao()

        if evento_pag_4 == 'Cadastrar Produtos':
            pagina_4.close()
            cadastro_produtos()


def realizar_venda():
    lista_produtos = back.consultar_produtos()
    print(lista_produtos[0][0])
    cabecalho = ['Cód. Produto', 'Item', 'Valor', 'Estoque']
    inicial = 1

    venda = [
        [sg.Text('Selecione o Produto')],
        [sg.Table(
            values=lista_produtos,
            headings=cabecalho,
            header_border_width=3,
            header_text_color='#FFFFFF',
            header_background_color='#3C3F41',
            row_height=22,
            alternating_row_color='#0765B6',
            background_color='#283B5B',
            num_rows=10,
            key='produto_selecionado',
            auto_size_columns=True,
            justification='center')],
        [sg.Text('Quantidade '), sg.Input(f'{inicial}', size=(4, 2), key='quantidade')],
        [sg.Text('')],
        [sg.Button('Cancelar', size=(20, 2)), sg.Button('Realizar Venda', size=(20, 2))]
    ]

    pagina_venda = sg.Window('Realizar Venda', venda, element_justification='center')
    evento_pag_venda, valor_pag_venda = pagina_venda.read()

    linha = valor_pag_venda['produto_selecionado'][0]
    print(lista_produtos[linha][0])

    while True:

        if evento_pag_venda == sg.WINDOW_CLOSED or evento_pag_venda == 'Cancelar':
            pagina_venda.close()
            area_vendas()

        if evento_pag_venda == 'Realizar Venda':
            data_venda = back.data_atual()
            funcionario_venda = fun_cod
            produto = lista_produtos[linha][0]
            quantidade = int(valor_pag_venda['quantidade'])
            print('__________________')
            print(type(data_venda))
            print(data_venda)
            print(type(funcionario_venda))
            print(funcionario_venda)
            print(type(produto))
            print(produto)
            print(type(quantidade))
            print(quantidade)
            print('__________________')

            back.realizar_venda(data_venda, funcionario_venda, produto, quantidade)

            pagina_venda.close()
            area_vendas()


def cadastro_produtos():
    cadastro_produto = [
        [sg.Text('')],
        [sg.Text('Item')],
        [sg.InputText('', size=(50, 3), key='prod_nome')],
        [sg.Text('Marca')],
        [sg.InputText('', size=(50, 3), key='prod_marca')],
        [sg.Text('Tipo')],
        [sg.InputText('', size=(50, 3), key='prod_tipo')],
        [sg.Text('Preço de Custo')],
        [sg.InputText('', size=(15, 3), key='prod_custo')],
        [sg.Text('Preço de Venda')],
        [sg.InputText('', size=(15, 3), key='prod_venda')],
        [sg.Text('Quantidade')],
        [sg.InputText('', size=(15, 3), key='prod_quantidade')],
        [sg.Text('')],
        [sg.Button('Cancelar', size=(14, 2)), sg.Button('Cadastrar', size=(14, 2))]
    ]

    pagina_5 = sg.Window('Cadastro de Produtos', cadastro_produto)
    evento_pag_5, valor_pag_5 = pagina_5.read()

    while True:

        if evento_pag_5 == sg.WINDOW_CLOSED:
            pagina_5.close()
            area_produtos()

        if evento_pag_5 == 'Cancelar':
            pagina_5.close()
            area_produtos()

        if evento_pag_5 == 'Cadastrar':
            prod_nome = valor_pag_5['prod_nome']
            prod_marca = valor_pag_5['prod_marca']
            prod_custo = valor_pag_5['prod_custo']
            prod_venda = valor_pag_5['prod_venda']
            prod_tipo = valor_pag_5['prod_tipo']
            prod_quantidade = valor_pag_5['prod_quantidade']

            if (prod_nome != '') or \
                    (prod_marca != '') or \
                    (prod_custo != '') or \
                    (prod_venda != '') or \
                    (prod_tipo != '') or \
                    (prod_quantidade != ''):

                back.cadastrar_produtos(prod_nome, prod_marca, prod_custo, prod_venda, prod_tipo, prod_quantidade)
                pagina_5.close()
                area_produtos()

            else:
                pagina_5.close()
                area_produtos()


front()
