from manipula_dados import tabelas_lista_1,nomes_colunas
import MySQLdb
conn = MySQLdb.connect(user='root', passwd='Gze6dg30!', host='127.0.0.1', port=3306)
cursor = conn.cursor()


def recupera_os_nomes_das_colunas_com_aspas(tabela):
    nome_quoted = ""
    i = 1
    for nome in nomes_colunas[tabela]:
        if i == 1:
            nome_quoted = "'" + nome + "'"
        else:
            nome_quoted = nome_quoted + ", '" + nome + "'"
        i += 1
    return nome_quoted
def recupera_os_nomes_das_colunas_sem_aspas(tabela):
    nome_unquoted = ""
    i = 1
    for nome in nomes_colunas[tabela]:
        if i == 1:
            nome_unquoted = nome
        else:
            nome_unquoted = nome_unquoted + ", " + nome
        i += 1
    return nome_unquoted

tabelas_schema = ['tb_campos_preenchidos']
for tabela in tabelas_lista_1:
    tabelas_schema.append(tabela)


for tabela in tabelas_schema:
    teste_tb = {}
    teste_tb2 = {}
    nome_quoted = recupera_os_nomes_das_colunas_com_aspas(tabela)
    nome_unquoted = recupera_os_nomes_das_colunas_sem_aspas(tabela)
    csv = (f"""USE `flora`;
    SELECT {nome_quoted}
    UNION ALL
    SELECT {nome_unquoted}
    FROM {tabela}
    INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/{tabela}.csv'
    CHARACTER SET utf8
    FIELDS TERMINATED BY ';'
    optionally ENCLOSED BY '"'
    LINES TERMINATED BY '\n';""")
    cursor.execute(csv)
conn.close()
# CHARSET 'latin1'