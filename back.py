import mysql.connector
import datetime


def conexao():
    c = mysql.connector.connect(
        host='localhost',
        database='db_vendas',
        user='root',
        password='admin')

    # INFORMAÇÃO SOBRE A CONEXÃO
    if c.is_connected():
        info = c.get_server_info()
        print(f"Conectado ao servidor MySQL versão {info}")

    # CURSOR PARA REALIZAR AS OPERAÇÕES NO PYTHON
    connect = c

    return connect


cnx = conexao()
cursor = cnx.cursor()


def realizar_venda(data, funcionario, produto, quantidade):
    # SELECIONA O PRODUTO ESCOLHIDO PELO USUÁRIO
    valor_produto = cursor.execute(f"select prod_venda from produto where prod_cod = {produto}")
    valor_produto = cursor.fetchall()

    # MULTIPLICA PELA QUANTIDADE INSERIDA
    preco_total = (valor_produto[0][0]) * quantidade

    # REDUZ A QUANTIDADE DO ESTOQUE
    estoque = cursor.execute(f"select prod_estoque from produto where prod_cod = {produto}")
    estoque = cursor.fetchall()
    atualizacao = (estoque[0][0]) - quantidade

    # INSERÇÃO DA NOVA VENDA COM REDUÇÃO DO ESTOQUE
    cursor.execute(f"update produto set prod_estoque = {atualizacao} where prod_cod = {produto}")
    cursor.execute(f"insert into venda ("
                   f"ven_data,"
                   f"ven_total,"
                   f"ven_cod_fun,"
                   f"ven_cod_produto,"
                   f"ven_quant) values ("
                   f"'{data}', "
                   f"{preco_total}, "
                   f"{funcionario}, "
                   f"{produto}, "
                   f"{quantidade})")
    # REALIZAR TODAS OPERAÇÕES NO BANCO DE DADOS
    cnx.commit()

# TESTE PARA REALIZAR VENDA
    # realizar_venda('13/09/2022', 20220902, 780, 1)


def filtrar_venda(funcionario):
    minhas_vendas = cursor.execute(f"select ven_data, "
                                   f"ven_total from venda "
                                   f"where ven_cod_fun = {funcionario}")
    minhas_vendas = cursor.fetchall()

    for dados in minhas_vendas:
        print(dados)

    cnx.commit()

    return minhas_vendas

# TESTE VENDA FILTRADA
    # filtrar_venda(20220902)


def consultar_produtos():
    produtos = cursor.execute("select prod_cod, prod_item, prod_venda from produto where prod_estoque > 0")
    produtos = cursor.fetchall()

    for dados_produto in produtos:
        print(dados_produto)
    cnx.commit()
    return produtos

# TESTE PARA CONSULTAR PRODUTOS
    # consultar_produtos()


def cadastrar_produtos(item, marca, custo, venda, tipo, estoque):
    produtos = cursor.execute(f"insert into produto ("
                              f"prod_item, "
                              f"prod_marca, "
                              f"prod_custo, "
                              f"prod_venda, "
                              f"prod_tipo, "
                              f"prod_estoque) values "
                              f"('{item}', "
                              f"'{marca}', "
                              f"{custo}, "
                              f"{venda}, "
                              f"'{tipo}', "
                              f"{estoque})")
    produtos = cursor.fetchall()

    for dados_produto in produtos:
        print(dados_produto)

    cnx.commit()


# cadastrar_produtos('Camiseta Eagle Fly Free', 'White Metal', 42.50, 89.90, 'Camiseta', 9)
# consultar_produtos()


def data_atual():
    DataAtual = datetime.date.today()
    data = DataAtual.strftime("%d/%m/%Y")
    print(data)
    return data
