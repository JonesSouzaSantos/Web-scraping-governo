import csv
import os
from datetime import datetime
from mysql.connector import (connection)

# Conexão com banco de dados
cnx = connection.MySQLConnection(user='root', password='minha_senha',
                                 host='127.0.0.1',
                                 database='chuvas_brasil')
cursor = cnx.cursor()


# Inserir os dados no banco de dados
def inser_dados(dados):
    sql = '''
    insert into chuvas 
    values(
        %(codigo_estacao)s,
        %(data_leitura)s,
        %(hora_leitura)s,
        %(precipitacao)s,
        %(tempmaxima)s,
        %(tempminima)s,
        %(insolacao)s,
        %(evaporacao_piche)s,
        %(temp_comp_media)s,
        %(umidade_relativa_media)s,
        %(velocidade_do_vento_media)s
    )
    '''
    # Tratar os dados
    if dados[3] == '':
        precipitacao = 0
    else:
        precipitacao = dados[3]

    if dados[4] == '':
        tempmaxima = 0
    else:
        tempmaxima = dados[4]

    if dados[5] == '':
        tempminima = 0
    else:
        tempminima = dados[5]

    if dados[6] == '':
        insolacao = 0
    else:
        insolacao = dados[6]

    if dados[7] == '':
        evaporacao_piche = 0
    else:
        evaporacao_piche = dados[7]

    if dados[8] == '':
        temp_comp_media = 0
    else:
        temp_comp_media = dados[8]

    if dados[9] == '':
        umidade_relativa_media = 0
    else:
        umidade_relativa_media = dados[9]

    if dados[10] == '':
        velocidade_do_vento_media = 0
    else:
        velocidade_do_vento_media = dados[10]

    dados_inseriro = {
        'codigo_estacao': dados[0],
        'data_leitura': datetime.strptime(dados[1], '%d/%m/%Y'),
        'hora_leitura': dados[2],
        'precipitacao': precipitacao,
        'tempmaxima': tempmaxima,
        'tempminima': tempminima,
        'insolacao': insolacao,
        'evaporacao_piche': evaporacao_piche,
        'temp_comp_media': temp_comp_media,
        'umidade_relativa_media': umidade_relativa_media,
        'velocidade_do_vento_media': velocidade_do_vento_media
    }
    print(dados[3], dados_inseriro)
    cursor.execute(sql, dados_inseriro)
    cnx.commit()


# Pasta que contem os arquivos
caminho_pasta = 'C:\Projetos Python\Web Scraping\Arquivo' + os.sep

nome_arquivo = os.listdir(caminho_pasta)
# começa a varrer a pasta e trazer o nome de todos os arquivos
for arquivos in nome_arquivo:
    # Monta o caminho absoluto do arquivo
    caminho_absoluto = caminho_pasta + arquivos
    abrir_arquivos = open(caminho_absoluto, 'rt')
    leitura = csv.reader(abrir_arquivos, delimiter=';')
    print(arquivos)
    for pular_linhas in range(48):
        next(leitura)
    for ler in leitura:
        if '</pre>' in ler:
            pass
        else:
            inser_dados(ler)
            # input()

cnx.close()
