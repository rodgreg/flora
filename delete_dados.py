



DELETE FROM tb_pt WHERE tb_pt.FK = '[Shodan (conferido).xlsx]modelo_banco(2)_4.044608';
DELETE FROM tb_certificados_incremental WHERE tb_certificados_incremental.FK = '[Shodan (conferido).xlsx]modelo_banco(2)_4.044608';
DELETE FROM tb_certificados WHERE tb_certificados.FK = '[Shodan (conferido).xlsx]modelo_banco(2)_4.044608';
DELETE FROM tb_laudos_incremental WHERE tb_laudos_incremental.FK = '[Shodan (conferido).xlsx]modelo_banco(2)_4.044608';
DELETE FROM tb_laudos WHERE tb_laudos.FK = '[Shodan (conferido).xlsx]modelo_banco(2)_4.044608';
DELETE FROM tb_formuladores_incremental WHERE tb_formuladores_incremental.FK = '[Shodan (conferido).xlsx]modelo_banco(2)_4.044608';
DELETE FROM tb_formuladores WHERE tb_formuladores.FK = '[Shodan (conferido).xlsx]modelo_banco(2)_4.044608';
DELETE FROM tb_composicao_incremental WHERE tb_composicao_incremental.FK = '[Shodan (conferido).xlsx]modelo_banco(2)_4.044608';
DELETE FROM tb_composicao WHERE tb_composicao.FK = '[Shodan (conferido).xlsx]modelo_banco(2)_4.044608';
DELETE FROM tb_fq_incremental WHERE tb_fq_incremental.FK = '[Shodan (conferido).xlsx]modelo_banco(2)_4.044608';
DELETE FROM tb_fq WHERE tb_fq.FK = '[Shodan (conferido).xlsx]modelo_banco(2)_4.044608';
DELETE FROM tb_dl50oral_incremental WHERE tb_dl50oral_incremental.FK = '[Shodan (conferido).xlsx]modelo_banco(2)_4.044608';
DELETE FROM tb_dl50cutanea_incremental WHERE tb_dl50cutanea_incremental.FK = '[Shodan (conferido).xlsx]modelo_banco(2)_4.044608';
DELETE FROM tb_cl50_incremental WHERE tb_cl50_incremental.FK = '[Shodan (conferido).xlsx]modelo_banco(2)_4.044608';
DELETE FROM tb_irritacao_ocular_incremental WHERE tb_irritacao_ocular_incremental.FK = '[Shodan (conferido).xlsx]modelo_banco(2)_4.044608';
DELETE FROM tb_irritacao_cutanea_incremental WHERE tb_irritacao_cutanea_incremental.FK = '[Shodan (conferido).xlsx]modelo_banco(2)_4.044608';
DELETE FROM tb_llna_incremental WHERE tb_llna_incremental.FK = '[Shodan (conferido).xlsx]modelo_banco(2)_4.044608';
DELETE FROM tb_ames_incremental WHERE tb_ames_incremental.FK = '[Shodan (conferido).xlsx]modelo_banco(2)_4.044608';
DELETE FROM tb_micronucleo_incremental WHERE tb_micronucleo_incremental.FK = '[Shodan (conferido).xlsx]modelo_banco(2)_4.044608';
DELETE FROM tb_aditamentos_incremental WHERE tb_aditamentos_incremental.FK = '[Shodan (conferido).xlsx]modelo_banco(2)_4.044608';
DELETE FROM tb_irritacao_cutanea_incremental WHERE tb_irritacao_cutanea_incremental.FK = '[Shodan (conferido).xlsx]modelo_banco(2)_4.044608';
DELETE FROM tb_classificao_estudo_anvisa_incremental WHERE tb_classificao_estudo_anvisa_incremental.FK = '[Shodan (conferido).xlsx]modelo_banco(2)_4.044608';
DELETE FROM tb_classificao_estudo_empresa_incremental WHERE tb_classificao_estudo_empresa_incremental.FK = '[Shodan (conferido).xlsx]modelo_banco(2)_4.044608';
DELETE FROM tb_classificao_desfecho_incremental WHERE tb_classificao_desfecho_incremental.FK = '[Shodan (conferido).xlsx]modelo_banco(2)_4.044608';
DELETE FROM tb_perguntas_nc_incremental WHERE tb_perguntas_nc_incremental.FK = '[Shodan (conferido).xlsx]modelo_banco(2)_4.044608';
DELETE FROM tb_comunicacao_perigo_incremental WHERE tb_comunicacao_perigo_incremental.FK = '[Shodan (conferido).xlsx]modelo_banco(2)_4.044608';
DELETE FROM tb_desvios WHERE tb_desvios.FK = '[Shodan (conferido).xlsx]modelo_banco(2)_4.044608';
DELETE FROM tb_alertas_incremental WHERE tb_alertas_incremental.FK = '[Shodan (conferido).xlsx]modelo_banco(2)_4.044608';
DELETE FROM tb_irritacao_cutanea_incremental WHERE tb_irritacao_cutanea_incremental.FK = '[Shodan (conferido).xlsx]modelo_banco(2)_4.044608';

DELETE FROM tb_incremental WHERE tb_incremental.PK = '[Shodan (conferido).xlsx]modelo_banco(2)_4.044608';






for tabela in tabelas_salvas.keys():
    cursor.execute(f"Use flora; DELETE FROM {tabela} WHERE {tabela}.FK = '{tabelas_salvas[tabela]}';")