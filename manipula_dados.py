import pandas as pd
import os
import shutil
from sqlalchemy import create_engine
'pip install sqlalchemy'
import MySQLdb


#Extrai dois tipos de tabelas, as que tem uma linha só (incremental) e as que possuem várias linhas
#Prepara os dados e salva em dois dicionários (dict_incremental e dict_tabelas)
#As chaves do dicionários são os nomes das tabelas
#Renomeia as colunas de cada tabela
#Salva os dados nas respectivas tabelas do banco


#Cria engine
my_conn = create_engine('mysql+mysqldb://root:<senha>@localhost/flora')

pd.set_option('display.max_columns', 500)

nomes_colunas = {'tb_incremental':['file_name','data_bd','PK','nome_completo','empresa_usuario',
                                  'data_inicio','nu_processo','nu_expediente','data_entrada','marca_comercial',
                                  'empresa','cnpj','tipo_formulacao','sg_formulacao','finalidade_producao',
                                  'finalidade_importacao','finalidade_exportacao','finalidade_manipulacao',
                                  'finalidade_comercializacao','finalidade_utilizacao','finalidade_formulacao',
                                  'finalidade_outras','classe_herbicida','classe_inseticida','classe_fungicida',
                                  'classe_outras','pt_nao_aplicavel','assunto','co_codigo'],
                          'tb_pt':['FK','ordem','nome_ia','indice_ia','n_cas','marca_comercial_pt','nu_processo','nu_registro','pureza'],
      'tb_composicao_incremental':['FK','un_medida','utilizou_corretor_ph','corretores_ph','ph_min','ph_max','observação'],
                  'tb_composicao':['FK','ordem','segredo_industrial','nu_protocolo','n_cas','componente','funcao','c_nominal','c_minima','c_maxima',
                                   'protocolo_componente','componente_tox_relevante'],
    'tb_certificados_incremental':['FK','observação'],
                'tb_certificados':['FK','ordem','ingrediente_ativo','codigo','lote','fabricacao','validade','analise','c_analisada'],
          'tb_laudos_incremental':['FK', 'observação'],
                      'tb_laudos':['FK', 'ordem', 'ingrediente_ativo', 'codigo', 'lote', 'fabricacao', 'validade',
                                     'analise', 'c_analisada'],
    'tb_formuladores_incremental':['FK', 'observação'],
                'tb_formuladores':['FK','ordem','tipo','razao_social','cnpj','endereco','laudo','declaracao'],
              'tb_fq_incremental':['FK', 'observação'],
                          'tb_fq':['FK','ordem','estudo','laboratorio','BPL','cod_estudo','dt_conclusao','certificado',
                         'conclusao','desvios','desvios_descricao','desvios_argumentacao','desvios_impacto'],
          'tb_updown_incremental':['FK',	'titulo',	'codigo',	'laboratorio',	'bpl',	'protocolo','protocolo_outros',
                                   'dt_inicio',	'dt_conclusao',	'certificado','especie','linhagem',	'teste_limite',
                                   'sinais_relevantes',	'justificativa_apenas_machos','criterio_parada',
                                   'criterio_parada_justificativa',	'discussao_adicional','observacoes',
                                   'maior_que','dl50_oral','lt_minimo','lt_maximo','conclusao'],
                      'tb_updown':['FK','codigo','sequencia','dose','sexo','resposta','sinais_clinicos','necropsia'],
        'tb_dl50oral_incremental':['FK','titulo', 	'codigo', 	'laboratorio', 	'bpl', 	'protocolo','protocolo_outros',
                                   'dt_inicio','dt_conclusao', 	'certificado','especie','linhagem','sinais_relevantes',
                                   'discussao_adicional', 'observacoes','maior_que','dl50_oral','lt_minimo','lt_maximo',
                                   'conclusao'],
                    'tb_dl50oral':['FK','codigo','etapa','dose','no_machos','no_mortes_machos','no_femeas',
                                   'no_mortes_femeas','sinais_clinicos','necropsia'],
     'tb_dl50cutanea_incremental':['FK','dispensa','titulo','codigo','laboratorio','bpl','protocolo','protocolo_outros',
                                   'dt_inicio','dt_conclusao','certificado','especie','linhagem','sinais_relevantes',
                                   'discussao_adicional', 	'observacoes', 	'maior_que','dl50_cutanea',	'lt_minimo','lt_maximo',
                                   'conclusao'],
                   'tb_dl50cutanea': ['FK', 'codigo', 'etapa', 'dose', 'no_machos', 'no_mortes_machos', 'no_femeas',
                                 'no_mortes_femeas', 'sinais_clinicos', 'necropsia'],
            'tb_cl50_incremental':['FK','dispensa','dispensa_1','dispensa_outra','dispensa_justificativa','titulo',
                                   'codigo', 	'laboratorio', 	'bpl', 	'protocolo','protocolo_outros','dt_inicio',
                                   'dt_conclusao', 	'certificado', 	'especie', 	'linhagem', 	'exposicao_4h',
                                   'sinais_relevantes','discussao_adicional','observacoes',	'maior_que','cl50',
                                   'lt_minimo',	'lt_maximo','conclusao'],
                        'tb_cl50': ['FK','codigo','ordem','c_efetiva','no_machos','no_mortes_machos','no_femeas',
                                    'no_mortes_femeas','MMAD','GSD','sinais_clinicos','necropsia'],
 'tb_irritacao_ocular_incremental':['FK','MA_estudos','MA_observacoes',	'dispensa',	'dispensa_1','dispensa_2',
                                    'dispensa_outra','dispensa_justificativa', 	'titulo','codigo', 	'laboratorio',
                                    'bpl', 	'protocolo','protocolo_outros',	'dt_inicio','dt_conclusao','certificado',
                                    'especie', 	'linhagem','dose', 	'um_dose','lavagem_do_olho','horas_pos_aplicacao',
                                    'tempo_total','corrosao',	'sexo_1','sexo_2','sexo_3','lesoes_1','lesoes_2',
                                    'lesoes_3',	'lesoes_4',	'detalhamento_alteracoes','descricao_bula',
                                    'discussao_adicional','observacoes','conclusao'],
         'tb_irritacao_ocular_ma': ['FK', 'codigo', 'protocolo', 'resultados', 'classificacao'],
            'tb_irritacao_ocular': ['FK', 'codigo', 'ordem', 'alteracao', '24_1', '48_1', '72_1', '21_1', '24_2',
                                    '48_2', '72_2', '21_2', '24_3', '48_3', '72_3', '21_3',
                                    'media_1', 'media_2', 'media_3'],
'tb_irritacao_cutanea_incremental':['FK','MA_estudos', 	'MA_observacoes', 	'dispensa',	'dispensa_1','dispensa_2',
                                    'dispensa_outra','dispensa_justificativa', 	'titulo', 'codigo',	'laboratorio',
                                    'bpl', 	'protocolo','protocolo_outros',	'dt_inicio','dt_conclusao',	'certificado',
                                    'especie','linhagem','dose','diluicao','diluente','lavagem','tempo_apos_aplicacao',
                                    'tempo_total','lesoes_1',	'lesoes_2',	'lesoes_3',	'lesoes_4','lesoes_5','lesoes_6',
                                    'detalhamento_alteracoes','descricao_bula','discussao_adicional','observacoes',
                                    'conclusao'],
         'tb_irritacao_cutanea_ma': ['FK','codigo','protocolo','resultados','classificacao'],
            'tb_irritacao_cutanea': ['FK','codigo','ordem','sexo','eritema_1','edema_1','eritema_24','edema_24',
                                     'eritema_48','edema_48','eritema_72','edema_72',
                                     'eritema_media_24_48_72','edema_media_24_48_72'],
              'tb_llna_incremental':['FK','titulo',	'codigo','laboratorio','bpl','protocolo','protocolo_outros',
                                     'dt_inicio', 	'dt_conclusao', 'certificado','especie', 'linhagem','tipo_estudo',
                                     'possui_controle_positivo','possui_teste_confiabilidade',
                                     'dt_conclusao_confiabilidade','justificativa_confiabilidade','preliminar_teste',
                                     'preliminar_solubilidade',	'preliminar_espessura_orelha',
                                     'preliminar_eritema_superior_3','preliminar_resultados','definitivo_abordagem',
                                     'definitivo_sexo','definitivo_no_animais','definitivo_resultados',
                                     'discussao_adicional',	'observacoes','conclusao'],
    'tb_sensibilizacao_incremental':['FK','titulo', 	'codigo', 	'laboratorio', 	'bpl', 	'protocolo',
                                     'protocolo_outros','dt_inicio','dt_conclusao','certificado','especie','linhagem',
                                     'metodo','confiabilidade_teste','confiabilidade_dt_conducao',
                                     'confiabilidade_metodo','confiabilidade_ST','confiabilidade_dose',
                                     'confiabilidade_diluente','confiabilidade_resultado_24',
                                     'confiabilidade_resultado_48','preliminar_resultados',
                                     'preliminar_inducao_intradermica','preliminar_inducao_topica',
                                     'preliminar_desafio_topica','definitivo_no_animais_CN',
                                     'definitivo_no_animais_testados','inducao_intradermica_1','inducao_intradermica_2',
                                     'inducao_topica_1','inducao_topica_2',	'inducao_justificar_diferenca_doses',
                                     'inducao_alteracoes_clinicas','desafio_dose','desafio_justificar_diferenca_dose',
                                     'desafio_tempo_inducao_desafio','desafio_alteracoes_clinicas',
                                     'desafio_resultado_24', 	'desafio_resultado_48','redesafio_teste',
                                     'redesafio_tempo_desafio_redesafio','redesafio_dose',
                                     'redesafio_alteracoes_clinicas','redesafio_resultado_24','redesafio_resultado_48',
                                     'discussao_adicional', 'observacoes', 	'conclusao'],
               'tb_ames_incremental':['FK', 	'titulo', 	'codigo', 	'laboratorio', 	'bpl', 	'protocolo',
                                      'protocolo_outros', 	'dt_inicio', 	'dt_conclusao', 	'certificado',
                                      'especies', 	'unidade_medida','possui_atv_antimicrobiana',
                                      'efetuou_analises_geneticas', 	'esteve_entre_108_109',
                                      'utilizou_2_aminoantraceno', 	'utilizou_outro_mutageno','no_outro_mutageno',
                                      'comprovante_outro_mutageno', 	'metodo_ctrl_historico','discussao_adicional',
                                      'observacoes', 	'conclusao'],
        'tb_micronucleo_incremental':['FK', 	'titulo', 	'codigo', 	'laboratorio', 	'bpl', 	'protocolo',
                                      'protocolo_outros', 	'dt_inicio','dt_conclusao', 	'certificado', 	'especie',
                                      'linhagem', 	'amostra','via_administracao', 'qt_administracoes','tempo_coleta',
                                      'tempo_coleta_inicio', 	'tempo_coleta_termino', 	'tempo_coleta_unico',
                                      'st_controle_negativo','cn_foi_testado_mais_de_uma_vez', 	'st_controle_positivo',
                                      'qt_dose_cp','metodo','controle_historico_origem','controle_historico_periodo_1',
                                      'controle_historico_periodo_2', 	'controle_historico_qt_estudos_machos',
                                      'controle_historico_qt_estudos_femeas', 	'preliminar_teste',
                                      'preliminar_houve_diferenca_sexos','preliminar_estudo_sem_DMT',
                                      'preliminar_qt_dmt_machos', 	'preliminar_qt_dmt_femeas',
                                      'preliminar_dmt_utilizou_dl50', 	'preliminar_justificativa_escolha_da_dmt',
                                      'preliminar_dl50_mesma_especie', 	'preliminar_dl50_mesmo_sexo',
                                      'preliminar_dl50_machos','preliminar_dl50_femeas','preliminar_dl50_minima_machos',
                                      'preliminar_dl50_inermediaria_machos','preliminar_dl50_maxima_machos',
                                      'preliminar_dl50_minima_femeas','preliminar_dl50_inermediaria_femeas',
                                      'preliminar_dl50_maxima_femeas', 	'definitivo_sexo',
                                      'definitivo_estudo_complementacao','definitivo_evidencia_atingiu_medula',
                                      'definitivo_resultados_estatisticos', 	'definitivo_houve_aumento_epmn',
                                      'definitivo_houve_aumento_dose_resposta_epmn',
                                      'definitivo_resultados_fora_controle_historico','definitivo_alteracoes_clinicas',
                                      'discussao_adicional','observacoes','conclusao'],
          'tb_aditamentos_incremental':['FK', 	'assunto', 	'expediente', 	'data'],
'tb_aditamentos_discussao_incremental':['FK',	'discussao'],
             'tb_culturas_incremental':['FK',	'ordem',	'cultura',	'referencia'],
'tb_classificao_estudo_anvisa_incremental':['FK',	'desfecho',	'estudo',	'classificacao'],
'tb_classificao_estudo_empresa_incremental':['FK',	'desfecho',	'estudo',	'classificacao'],
 'tb_classificao_desfecho_incremental':['FK','desfecho','classificacao'],
         'tb_perguntas_nc_incremental':['FK','pergunta_1','pergunta_2','pergunta_3','pergunta_4','pergunta_5','pergunta_6'],
   'tb_comunicacao_perigo_incremental':['FK', 	'Palavra_advertencia', 	'frase_oral', 	'frase_cutanea',
                                        'frase_inalatoria', 	'frase_ocular','frase_irritacao_cutanea',
                                        'frase_sensibilizacao', 'frase_mutagenicidade','frase_1','frase_2','frase_3',
                                        'frase_4'],
                          'tb_desvios':['FK','estudo','codigo_estudo','desvio_descricao','desvio_argumentacao',
                                        'desvio_interferiu_nos_resultados'],
              'tb_alertas_incremental':['FK','estudo', 'ds_alerta','acao_tomada','alerta_gerado'],
                 'tb_campos_preenchidos':['FK',	'tb_incremental',	'tb_pt',	'tb_composicao_incremental',
                                          'tb_composicao',	'tb_certificados_incremental',	'tb_certificados',
                                          'tb_laudos_incremental',	'tb_laudos',	'tb_formuladores_incremental',
                                          'tb_formuladores',	'tb_fq_incremental',	'tb_fq',
                                          'tb_updown_incremental',	'tb_updown',	'tb_dl50oral_incremental',
                                          'tb_dl50oral',	'tb_dl50cutanea_incremental',	'tb_dl50cutanea',
                                          'tb_cl50_incremental',	'tb_cl50',	'tb_irritacao_ocular_incremental',
                                          'tb_irritacao_ocular_ma',	'tb_irritacao_ocular',
                                          'tb_irritacao_cutanea_incremental',	'tb_irritacao_cutanea_ma',
                                          'tb_irritacao_cutanea',	'tb_llna_incremental',	'tb_LLNA_preliminar',
                                          'tb_LLNA_definitivo_individuos_grupos',
                                          'tb_LLNA_definitivo_individuos_resultados','tb_LLNA_definitivo_grupos',
                                          'tb_sensibilizacao_incremental','tb_sensibilizacao_preliminar',
                                          'tb_ames_incremental','tb_ames_testes','tb_triplicatas_TA97',
                                          'tb_triplicatas_TA97a',	'tb_triplicatas_TA98','tb_triplicatas_TA100',
                                          'tb_triplicatas_TA102','tb_triplicatas_TA1535','tb_triplicatas_TA1537',
                                          'tb_triplicatas_TA1538','tb_triplicatas_WP2_uvrA',
                                          'tb_triplicatas_WP2_uvrA_pKM101',	'tb_micronucleo_incremental',
                                          'tb_micronucleo_historico',	'tb_micronucleo_preliminar',
                                          'tb_micronucleo_proporcao_ep',	'tb_micronucleo_proporcao_epmn',
                                          'tb_micronucleo_resultados',	'tb_micronucleo_doses',
                                          'tb_aditamentos_incremental',	'tb_aditamentos_discussao_incremental',
                                          'tb_culturas_incremental',	'tb_classificao_estudo_anvisa_incremental',
                                          'tb_classificao_estudo_empresa_incremental',
                                          'tb_classificao_desfecho_incremental','tb_perguntas_nc_incremental',
                                          'tb_comunicacao_perigo_incremental',	'tb_desvios','tb_alertas_incremental']
                 }




tabelas_lista_1 = ['tb_incremental',
                   'tb_pt',
                   'tb_certificados_incremental',
                   'tb_certificados',
                   'tb_laudos_incremental',
                   'tb_laudos',
                   'tb_formuladores_incremental',
                   'tb_formuladores',
                   'tb_composicao_incremental',
                   'tb_composicao',
                   'tb_fq_incremental',
                   'tb_fq',
                   'tb_updown_incremental',
                   'tb_updown',
                   'tb_dl50oral_incremental',
                   'tb_dl50oral',
                   'tb_dl50cutanea_incremental',
                   'tb_dl50cutanea',
                   'tb_cl50_incremental',
                   'tb_cl50',
                   'tb_irritacao_ocular_incremental',
                   'tb_irritacao_ocular_ma',
                   'tb_irritacao_ocular',
                   'tb_irritacao_cutanea_incremental',
                   'tb_irritacao_cutanea_ma',
                   'tb_irritacao_cutanea',
                   'tb_llna_incremental',
                   'tb_sensibilizacao_incremental',
                   'tb_ames_incremental',
                   'tb_micronucleo_incremental',
                   'tb_aditamentos_incremental',
                   'tb_aditamentos_discussao_incremental',
                   'tb_culturas_incremental',
                   'tb_classificao_estudo_anvisa_incremental',
                   'tb_classificao_estudo_empresa_incremental',
                   'tb_classificao_desfecho_incremental',
                   'tb_perguntas_nc_incremental',
                   'tb_comunicacao_perigo_incremental',
                   'tb_desvios',
                   'tb_alertas_incremental']

tabelas_lista_2 = ['tb_updown_incremental',
                   'tb_updown',
                   'tb_dl50oral_incremental',
                   'tb_dl50oral',
                   'tb_dl50cutanea_incremental',
                   'tb_dl50cutanea',
                   'tb_irritacao_cutanea_ma',
                   'tb_irritacao_cutanea',
                   'tb_cl50_incremental',
                   'tb_cl50',
                   'tb_irritacao_ocular_incremental',
                   'tb_irritacao_ocular_ma',
                   'tb_irritacao_ocular',
                   'tb_irritacao_cutanea_incremental',
                   'tb_llna_incremental',
                   'tb_sensibilizacao_incremental',
                   'tb_ames_incremental',
                   'tb_micronucleo_incremental',
                   'tb_desvios',
                   'tb_alertas_incremental']

# planilha = pd.read_excel("C:/Users/rodun/Documents/Anvisa_PC/Flora_python/Evolutiva/pre_banco/teste.xlsx", sheet_name="modelo_banco1")
# planilha = planilha.loc[planilha['indice'] != 'branco']



def extrai_dados_de_tabelas_prepara_dataframe(tabelas_lista):
    dict_tabelas = {}
    for tabela in tabelas_lista:

        print(f'formata: {tabela}')
        tb = planilha.loc[planilha['indice'] == tabela] #Procura as linhas da coluna A que tem o nome da tabela
        tb = tb[tb.iloc[:, 1] != 0] # Remove as linhas iguais a 0 da na coluna "Excluir"
        total_colunas = tb.iloc[0].count() # Conta o total de campos não NaN na primeira linha
        tb = tb.iloc[1:, 2:total_colunas] #Remove a primeira linha (labels na tabela do excel) e as duas primeiras colunas (nome da tabela e Excluir)
        tb = tb.replace('\n', '. ', regex=True)

        if (tb.empty):
            print(f'{tabela} está vazia')

        else:
            print(f'Nomeia : {tabela}')
            for nome in nomes_colunas.keys():
                if (tabela == nome):
                    nome_colunas = nomes_colunas[nome]
                    tb.columns = nome_colunas

            dict_tabelas[str(tabela)] = tb
    print("Arquivo Formatado corretamente\n")
    return dict_tabelas

def cria_os_dataframes(tabelas_lista):
    tb_incremental = extrai_dados_de_tabelas_prepara_dataframe(tabelas_lista)
    return tb_incremental

if __name__ == '__main__':

#Abre os arquivos
    os.chdir("C:/Users/rodun/Documents/Anvisa_PC/Flora_python/Evolutiva/5. Pre banco")
    total_de_arquivos = len(os.listdir("C:/Users/rodun/Documents/Anvisa_PC/Flora_python/Evolutiva/5. Pre banco"))
    i = 1
    for arquivo in os.listdir():
        tabelas_salvas = {}

# Formulários (1)
        print(f'\n{"-="*10} NOVO ARQUIVO{"-="*10}')
        print(f'{arquivo}----------------Formulários (1)----{i}/{total_de_arquivos}')
        planilha0 = pd.read_excel(arquivo, sheet_name="modelo_banco(1)_4.0")
        planilha = planilha0.loc[planilha0['indice'] != 'branco']

        tb_incremental = cria_os_dataframes(tabelas_lista_1)
        for dataframe in tb_incremental:
            tb_incremental[dataframe].to_sql(name=dataframe, con=my_conn, schema='flora', if_exists='append')
            tabelas_salvas[dataframe] = tb_incremental[dataframe].iloc[0, 0]
            print(f'Dados persistidos: {dataframe}.')

# Tabela de total de campos preenchidos
        print(f'\n{arquivo}----------------Tabela de total de campos preenchidos----{i}/{total_de_arquivos}')
        planilha0 = pd.read_excel(arquivo, sheet_name="campos_preenchidos(1)") #Abrir arquivo
        planilha = planilha0.iloc[1:, 1:] #Formatar dataframe
        planilha.columns = nomes_colunas['tb_campos_preenchidos'] #Nomear colunas
        planilha.to_sql(name='tb_campos_preenchidos', con=my_conn, schema='flora', if_exists='append') #persistir no BD

# Formulários (2)
        print(f'\n{arquivo}----------------Formulários (2)----{i}/{total_de_arquivos}')
        planilha0 = pd.read_excel(arquivo, sheet_name="modelo_banco(2)_4.0")
        planilha = planilha0.loc[planilha0['indice'] != 'branco']

        tb_incremental = cria_os_dataframes(tabelas_lista_2)
        for dataframe in tb_incremental:
            tb_incremental[dataframe].to_sql(name=dataframe, con=my_conn, schema='flora', if_exists='append')
            tabelas_salvas[dataframe] = tb_incremental[dataframe].iloc[0, 0]
            print(f'Dados persistidos: {dataframe}.')
        caminhoCompleto_antigo = (f"C:/Users/rodun/Documents/Anvisa_PC/Flora_python/Evolutiva/5. Pre banco/{arquivo}")
        caminhoCompleto_novo = (f"C:/Users/rodun/Documents/Anvisa_PC/Flora_python/Evolutiva/6. Concluidos/{arquivo}")
        shutil.move(caminhoCompleto_antigo, caminhoCompleto_novo)
        print('Arquivo movido para pasta de Concluídos')
        i += 1
        print(f'\n{"-=" * 10} FIM DO PROCESSAMENTO{"-=" * 10}')
