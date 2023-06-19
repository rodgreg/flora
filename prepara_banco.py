import MySQLdb

conn = MySQLdb.connect(user='root', passwd='<senha>', host='127.0.0.1', port='<port>')
cursor = conn.cursor()

# tb_incremental
cria_tb_incremental = ("""
CREATE DATABASE IF NOT EXISTS `flora` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
    USE `flora`;
CREATE TABLE IF NOT EXISTS  `tb_incremental` (
  `index` int,
  `file_name` varchar(100) NOT NULL,
  `data_bd` date NOT NULL,
  `PK` varchar(200) NOT NULL,
  `nome_completo` varchar(100) DEFAULT NULL,
  `empresa_usuario` varchar(100) DEFAULT NULL,
  `data_inicio` date DEFAULT NULL,
  `nu_processo` varchar(25) DEFAULT NULL,
  `nu_expediente`varchar(15) DEFAULT NULL,
  `data_entrada` date DEFAULT NULL,
  `marca_comercial` varchar(100) DEFAULT NULL,
  `empresa` varchar(100) DEFAULT NULL,
  `cnpj` varchar(25) DEFAULT NULL,
  `tipo_formulacao` varchar(100) DEFAULT NULL,
  `sg_formulacao` varchar(4) DEFAULT NULL,
  `finalidade_producao` varchar(10) DEFAULT NULL,
  `finalidade_importacao` varchar(10) DEFAULT NULL,
  `finalidade_exportacao` varchar(10) DEFAULT NULL,
  `finalidade_manipulacao` varchar(10) DEFAULT NULL,
  `finalidade_comercializacao` varchar(10) DEFAULT NULL,
  `finalidade_utilizacao` varchar(10) DEFAULT NULL,
  `finalidade_formulacao` varchar(10) DEFAULT NULL,
  `finalidade_outras` varchar(50) DEFAULT NULL,
  `classe_herbicida` varchar(10) DEFAULT NULL,
  `classe_inseticida` varchar(10) DEFAULT NULL,
  `classe_fungicida` varchar(10) DEFAULT NULL,
  `classe_outras` varchar(50) DEFAULT NULL,
  `pt_nao_aplicavel` varchar(10) DEFAULT NULL,
  `assunto` varchar(200) DEFAULT NULL,
  `co_codigo` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`PK`));
""")

# tb_pt, tb_composicao_incremental, tb_composicao, tb_certificados_incremental, tb_certificados,
# tb_laudos_incremental, tb_laudos, tb_formuladores_incremental, tb_formuladores, tb_fq_incremental, tb_fq
cria_tabelas_iniciais = ("""
        CREATE DATABASE IF NOT EXISTS `flora` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
    USE `flora`;
CREATE TABLE IF NOT EXISTS  `tb_pt` (
  `id` int NOT NULL AUTO_INCREMENT,
  `index` int,
  `FK` varchar(100) DEFAULT NULL,
  `ordem` int DEFAULT NULL,
  `nome_ia` varchar(100) DEFAULT NULL,
  `indice_ia` varchar(10) DEFAULT NULL,
  `n_cas` varchar(15) DEFAULT NULL,
  `marca_comercial_pt` varchar(100) DEFAULT NULL,
  `nu_processo` varchar(150) DEFAULT NULL,
  `nu_registro` varchar(50) DEFAULT NULL,
  `pureza` DECIMAL(7,2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (FK) references tb_incremental(PK));
  
  
CREATE TABLE IF NOT EXISTS  `tb_composicao_incremental` (
  `id` int NOT NULL AUTO_INCREMENT,
  `index` int,
  `FK` varchar(100) DEFAULT NULL,
  `un_medida` varchar(5) DEFAULT NULL,
  `utilizou_corretor_ph` varchar(5) DEFAULT NULL,
  `corretores_ph` LONGTEXT DEFAULT NULL,
  `ph_min` varchar(5) DEFAULT NULL,
  `ph_max` varchar(5) DEFAULT NULL,
  `observação` LONGTEXT DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (FK) references tb_incremental(PK));
    
        
CREATE TABLE IF NOT EXISTS  `tb_composicao` (
  `id` int NOT NULL AUTO_INCREMENT,
  `index` int,
  `FK` varchar(100) DEFAULT NULL,
  `ordem` int DEFAULT NULL,
  `segredo_industrial` varchar(100) DEFAULT NULL,
  `nu_protocolo` varchar(25) DEFAULT NULL,
  `n_cas` varchar(15) DEFAULT NULL,
  `componente` LONGTEXT DEFAULT NULL,
  `funcao` varchar(30) DEFAULT NULL,
  `c_nominal` DECIMAL(7,2) DEFAULT NULL,
  `c_minima` DECIMAL(7,2) DEFAULT NULL,
  `c_maxima` DECIMAL(7,2) DEFAULT NULL,
  `protocolo_componente` varchar(25) DEFAULT NULL,
  `componente_tox_relevante` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (FK) references tb_incremental(PK));
    
    
CREATE TABLE IF NOT EXISTS  `tb_certificados_incremental` (
  `id` int NOT NULL AUTO_INCREMENT,
  `index` int,
  `FK` varchar(100) DEFAULT NULL,
  `observação` LONGTEXT DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (FK) references tb_incremental(PK));
    
    
CREATE TABLE IF NOT EXISTS  `tb_certificados` (
  `id` int NOT NULL AUTO_INCREMENT,
  `index` int,
  `FK` varchar(100) DEFAULT NULL,
  `ordem` int DEFAULT NULL,
  `ingrediente_ativo` varchar(100) DEFAULT NULL,
  `codigo` varchar(150) DEFAULT NULL,
  `lote` varchar(100) DEFAULT NULL,
  `fabricacao` varchar(100) DEFAULT NULL,
  `validade` varchar(30) DEFAULT NULL,
  `analise` varchar(30) DEFAULT NULL,
  `c_analisada` DECIMAL(7,2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (FK) references tb_incremental(PK));
    
    
    
CREATE TABLE IF NOT EXISTS  `tb_laudos_incremental` (
  `id` int NOT NULL AUTO_INCREMENT,
  `index` int,
  `FK` varchar(100) DEFAULT NULL,
  `observação` LONGTEXT DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (FK) references tb_incremental(PK));
    
    
CREATE TABLE IF NOT EXISTS  `tb_laudos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `index` int,
  `FK` varchar(100) DEFAULT NULL,
  `ordem` int DEFAULT NULL,
  `ingrediente_ativo` varchar(100) DEFAULT NULL,
  `codigo` varchar(150) DEFAULT NULL,
  `lote` varchar(100) DEFAULT NULL,
  `fabricacao` varchar(100) DEFAULT NULL,
  `validade` varchar(30) DEFAULT NULL,
  `analise` varchar(30) DEFAULT NULL,
  `c_analisada` DECIMAL(7,2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (FK) references tb_incremental(PK));
    
CREATE TABLE IF NOT EXISTS  `tb_formuladores_incremental` (
  `id` int NOT NULL AUTO_INCREMENT,
  `index` int,
  `FK` varchar(100) DEFAULT NULL,
  `observação` LONGTEXT DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (FK) references tb_incremental(PK));
  
    
CREATE TABLE IF NOT EXISTS  `tb_formuladores` (
  `id` int NOT NULL AUTO_INCREMENT,
  `index` int,
  `FK` varchar(100) DEFAULT NULL,
  `ordem` int DEFAULT NULL,
  `tipo` varchar(100) DEFAULT NULL,
  `razao_social` longtext DEFAULT NULL,
  `cnpj` varchar(50) DEFAULT NULL,
  `endereco` LONGTEXT DEFAULT NULL,
  `laudo` varchar(150) DEFAULT NULL,
  `declaracao` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (FK) references tb_incremental(PK));

    
CREATE TABLE IF NOT EXISTS  `tb_fq_incremental` (
  `id` int NOT NULL AUTO_INCREMENT,
  `index` int,
  `FK` varchar(100) DEFAULT NULL,
  `observação` LONGTEXT DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (FK) references tb_incremental(PK));
  
  
CREATE TABLE IF NOT EXISTS  `tb_fq` (
  `id` int NOT NULL AUTO_INCREMENT,
  `index` int,
  `FK` varchar(100) DEFAULT NULL,
  `ordem` int DEFAULT NULL,
  `estudo` varchar(100) DEFAULT NULL,
  `laboratorio` LONGTEXT DEFAULT NULL,
  `BPL` varchar(50) DEFAULT NULL,
  `cod_estudo` varchar(100) DEFAULT NULL,
  `dt_conclusao` varchar(25) DEFAULT NULL,
  `certificado` varchar(100) DEFAULT NULL,
  `conclusao` LONGTEXT DEFAULT NULL,
  `desvios` varchar(50) DEFAULT NULL,
  `desvios_descricao` LONGTEXT DEFAULT NULL,
  `desvios_argumentacao` LONGTEXT DEFAULT NULL,
  `desvios_impacto` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (FK) references tb_incremental(PK));
  
        """)

# tb_updown_incremental,tb_updown
cria_tabelas_updown = ("""
        CREATE DATABASE IF NOT EXISTS `flora` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
    USE `flora`;

CREATE TABLE IF NOT EXISTS  `tb_updown_incremental` (
  `id` int NOT NULL AUTO_INCREMENT,
  `index` int,
  `FK` varchar(100) DEFAULT NULL,
  `titulo` LONGTEXT DEFAULT NULL,
  `codigo` varchar(100) DEFAULT NULL,
  `laboratorio` LONGTEXT DEFAULT NULL,
  `bpl` varchar(10) DEFAULT NULL,
  `protocolo` varchar(100) DEFAULT NULL,
  `protocolo_outros` LONGTEXT DEFAULT NULL,
  `dt_inicio` varchar(20) DEFAULT NULL,
  `dt_conclusao` varchar(20) DEFAULT NULL,
  `certificado` LONGTEXT DEFAULT NULL,
  `especie` varchar(100) DEFAULT NULL,
  `linhagem` varchar(100) DEFAULT NULL,
  `teste_limite` varchar(10) DEFAULT NULL,
  `sinais_relevantes` varchar(12) DEFAULT NULL,
  `justificativa_apenas_machos` LONGTEXT DEFAULT NULL,
  `criterio_parada` LONGTEXT DEFAULT NULL,
  `criterio_parada_justificativa` LONGTEXT DEFAULT NULL,
  `discussao_adicional` varchar(10) DEFAULT NULL,
  `observacoes` LONGTEXT DEFAULT NULL,
  `maior_que` varchar(10) DEFAULT NULL,
  `dl50_oral` DECIMAL(7,2) DEFAULT NULL,
  `lt_minimo` DECIMAL(7,2) DEFAULT NULL,
  `lt_maximo` DECIMAL(7,2) DEFAULT NULL,
  `conclusao` LONGTEXT DEFAULT NULL,  
  PRIMARY KEY (`id`),
  FOREIGN KEY (FK) references tb_incremental(PK));

CREATE TABLE IF NOT EXISTS  `tb_updown` (
  `id` int NOT NULL AUTO_INCREMENT,
  `index` int,
  `FK` varchar(100) DEFAULT NULL,
  `codigo` varchar(100) DEFAULT NULL,
  `sequencia` int DEFAULT NULL,
  `dose` DECIMAL(7,2) DEFAULT NULL,
  `sexo` varchar(10) DEFAULT NULL,
  `resposta` varchar(5) DEFAULT NULL,
  `sinais_clinicos` LONGTEXT DEFAULT NULL,
  `necropsia` LONGTEXT DEFAULT NULL, 
  PRIMARY KEY (`id`),
  FOREIGN KEY (FK) references tb_incremental(PK));
        """)

# tb_dl50oral_incremental, tb_dl50oral
cria_tabelas_dloral = ("""
        CREATE DATABASE IF NOT EXISTS `flora` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
    USE `flora`;

  CREATE TABLE IF NOT EXISTS  `tb_dl50oral_incremental` (
  `id` int NOT NULL AUTO_INCREMENT,
  `index` int,
  `FK` varchar(100) DEFAULT NULL,
  `titulo` LONGTEXT DEFAULT NULL,
  `codigo` varchar(100) DEFAULT NULL,
  `laboratorio` LONGTEXT DEFAULT NULL,
  `bpl` varchar(10) DEFAULT NULL,
  `protocolo` varchar(100) DEFAULT NULL,
  `protocolo_outros` LONGTEXT DEFAULT NULL,
  `dt_inicio` varchar(20) DEFAULT NULL,
  `dt_conclusao` varchar(20) DEFAULT NULL,
  `certificado` LONGTEXT DEFAULT NULL,
  `especie` varchar(100) DEFAULT NULL,
  `linhagem` varchar(100) DEFAULT NULL,
  `sinais_relevantes` varchar(12) DEFAULT NULL,
  `discussao_adicional` varchar(10) DEFAULT NULL,
  `observacoes` LONGTEXT DEFAULT NULL,
  `maior_que` varchar(12) DEFAULT NULL,
  `dl50_oral` DECIMAL(7,2) DEFAULT NULL,
  `lt_minimo` DECIMAL(7,2) DEFAULT NULL,
  `lt_maximo` DECIMAL(7,2) DEFAULT NULL,
  `conclusao` LONGTEXT DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (FK) references tb_incremental(PK)); 
  
  CREATE TABLE IF NOT EXISTS  `tb_dl50oral` (
  `id` int NOT NULL AUTO_INCREMENT,
  `index` int,
  `FK` varchar(100) DEFAULT NULL,
  `codigo` varchar(100) DEFAULT NULL,
  `etapa` int,
  `dose` DECIMAL(7,2) DEFAULT NULL,
  `no_machos` int,
  `no_mortes_machos` int,
  `no_femeas` int,
  `no_mortes_femeas` int,
  `sinais_clinicos` LONGTEXT DEFAULT NULL,
  `necropsia` LONGTEXT DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (FK) references tb_incremental(PK));
        """)

# tb_dl50cutanea_incremental, tb_dl50cutanea
cria_tabelas_dlcutanea = ("""
        CREATE DATABASE IF NOT EXISTS `flora` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
    USE `flora`;

  CREATE TABLE IF NOT EXISTS  `tb_dl50cutanea_incremental` (
  `id` int NOT NULL AUTO_INCREMENT,
  `index` int,
  `FK` varchar(100) DEFAULT NULL,
  `dispensa` varchar(100) DEFAULT NULL,
  `titulo` LONGTEXT DEFAULT NULL,
  `codigo` varchar(100) DEFAULT NULL,
  `laboratorio` LONGTEXT DEFAULT NULL,
  `bpl` varchar(12) DEFAULT NULL,
  `protocolo` varchar(100) DEFAULT NULL,
  `protocolo_outros` longtext DEFAULT NULL,
  `dt_inicio` varchar(20) DEFAULT NULL,
  `dt_conclusao` varchar(20) DEFAULT NULL,
  `certificado` varchar(100) DEFAULT NULL,
  `especie` varchar(100) DEFAULT NULL,
  `linhagem` varchar(100) DEFAULT NULL,
  `sinais_relevantes` varchar(12) DEFAULT NULL,
  `discussao_adicional` varchar(12) DEFAULT NULL,
  `observacoes` LONGTEXT DEFAULT NULL,
  `maior_que` varchar(12) DEFAULT NULL,
  `dl50_cutanea` DECIMAL(7,2) DEFAULT NULL,
  `lt_minimo` DECIMAL(7,2) DEFAULT NULL,
  `lt_maximo` DECIMAL(7,2)  DEFAULT NULL,
  `conclusao` LONGTEXT DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (FK) references tb_incremental(PK)); 
  
    CREATE TABLE IF NOT EXISTS  `tb_dl50cutanea` (
  `id` int NOT NULL AUTO_INCREMENT,
  `index` int,
  `FK` varchar(100) DEFAULT NULL,
  `codigo` varchar(100) DEFAULT NULL,
  `etapa` int,
  `dose` DECIMAL(7,2) DEFAULT NULL,
  `no_machos` int,
  `no_mortes_machos` int,
  `no_femeas` int,
  `no_mortes_femeas` int,
  `sinais_clinicos` LONGTEXT DEFAULT NULL,
  `necropsia` LONGTEXT DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (FK) references tb_incremental(PK));   
        """)

# tb_cl50_incremental, tb_cl50
cria_tabelas_clinalatoria = ("""
        CREATE DATABASE IF NOT EXISTS `flora` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
    USE `flora`;

  CREATE TABLE IF NOT EXISTS  `tb_cl50_incremental` (
  `id` int NOT NULL AUTO_INCREMENT,
  `index` int,
  `FK` varchar(100) DEFAULT NULL,
  `dispensa` varchar(100) DEFAULT NULL,
  `dispensa_1` varchar(100) DEFAULT NULL,
  `dispensa_outra` varchar(100) DEFAULT NULL,
  `dispensa_justificativa` LONGTEXT DEFAULT NULL,
  `titulo` LONGTEXT DEFAULT NULL,
  `codigo` varchar(100) DEFAULT NULL,
  `laboratorio` LONGTEXT DEFAULT NULL,
  `bpl` varchar(12) DEFAULT NULL,
  `protocolo` varchar(100) DEFAULT NULL,
  `protocolo_outros` longtext DEFAULT NULL,
  `dt_inicio` varchar(20) DEFAULT NULL,
  `dt_conclusao` varchar(20) DEFAULT NULL,
  `certificado` varchar(100) DEFAULT NULL,
  `especie` varchar(100) DEFAULT NULL,
  `linhagem` varchar(100) DEFAULT NULL,
  `exposicao_4h` varchar(10) DEFAULT NULL,
  `sinais_relevantes` varchar(12) DEFAULT NULL,
  `discussao_adicional` varchar(12) DEFAULT NULL,
  `observacoes` LONGTEXT DEFAULT NULL,
  `maior_que` varchar(12) DEFAULT NULL,
  `cl50` DECIMAL(7,2) DEFAULT NULL,
  `lt_minimo` DECIMAL(7,2) DEFAULT NULL,
  `lt_maximo` DECIMAL(7,2)  DEFAULT NULL,
  `conclusao` LONGTEXT DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (FK) references tb_incremental(PK));
  
   CREATE TABLE IF NOT EXISTS  `tb_cl50` (
  `id` int NOT NULL AUTO_INCREMENT,
  `index` int,
  `FK` varchar(100) DEFAULT NULL,
  `codigo` varchar(100) DEFAULT NULL,
  `ordem` int DEFAULT NULL,
  `c_efetiva` DECIMAL(7,2) DEFAULT NULL,
  `no_machos` INT DEFAULT NULL,
  `no_mortes_machos` INT DEFAULT NULL,
  `no_femeas` INT DEFAULT NULL,
  `no_mortes_femeas` INT DEFAULT NULL,
  `MMAD` DECIMAL(7,2) DEFAULT NULL,
  `GSD` DECIMAL(7,2) DEFAULT NULL,
  `sinais_clinicos` longtext DEFAULT NULL,
  `necropsia` longtext DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (FK) references tb_incremental(PK));
        """)

# tb_irritacao_ocular_incremental, tb_irritacao_ocular_MA, tb_irritacao_ocular
cria_tabelas_irritacao_ocular = ("""
        CREATE DATABASE IF NOT EXISTS `flora` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
    USE `flora`;

  CREATE TABLE IF NOT EXISTS  `tb_irritacao_ocular_incremental` (
  `id` int NOT NULL AUTO_INCREMENT,
  `index` int,
  `FK` varchar(100) DEFAULT NULL,
  `MA_estudos` varchar(100) DEFAULT NULL,
  `MA_observacoes` LONGTEXT DEFAULT NULL,
  `dispensa` varchar(12) DEFAULT NULL,
  `dispensa_1` varchar(12) DEFAULT NULL,
  `dispensa_2` varchar(12) DEFAULT NULL,
  `dispensa_outra` varchar(12) DEFAULT NULL,
  `dispensa_justificativa` LONGTEXT DEFAULT NULL,
  `titulo` LONGTEXT DEFAULT NULL,
  `codigo` varchar(100) DEFAULT NULL,
  `laboratorio` LONGTEXT DEFAULT NULL,
  `bpl` varchar(12) DEFAULT NULL,
  `protocolo` varchar(100) DEFAULT NULL,
  `protocolo_outros` longtext DEFAULT NULL,
  `dt_inicio` varchar(20) DEFAULT NULL,
  `dt_conclusao` varchar(20) DEFAULT NULL,
  `certificado` varchar(100) DEFAULT NULL,
  `especie` varchar(100) DEFAULT NULL,
  `linhagem` varchar(100) DEFAULT NULL,
  `dose` varchar(100) DEFAULT NULL,
  `um_dose` varchar(100) DEFAULT NULL,
  `lavagem_do_olho` varchar(100) DEFAULT NULL,
  `horas_pos_aplicacao` varchar(100) DEFAULT NULL,
  `tempo_total` varchar(12) DEFAULT NULL,
  `corrosao` varchar(12) DEFAULT NULL,
  `sexo_1` varchar(12) DEFAULT NULL,
  `sexo_2` varchar(12) DEFAULT NULL,
  `sexo_3` varchar(12) DEFAULT NULL,
  `lesoes_1` varchar(12) DEFAULT NULL,
  `lesoes_2` varchar(12) DEFAULT NULL,
  `lesoes_3` varchar(12) DEFAULT NULL,
  `lesoes_4` varchar(12) DEFAULT NULL,
  `detalhamento_alteracoes` LONGTEXT DEFAULT NULL,
  `descricao_bula` LONGTEXT DEFAULT NULL,
  `discussao_adicional` varchar(12) DEFAULT NULL,
  `observacoes` LONGTEXT DEFAULT NULL,
  `conclusao` LONGTEXT DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (FK) references tb_incremental(PK));
  
  CREATE TABLE IF NOT EXISTS  `tb_irritacao_ocular_MA` (
  `id` int NOT NULL AUTO_INCREMENT,
  `index` int,
  `FK` varchar(100) DEFAULT NULL,
  `codigo` varchar(100) DEFAULT NULL,
  `protocolo` LONGTEXT DEFAULT NULL,
  `resultados` LONGTEXT DEFAULT NULL,
  `classificacao` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (FK) references tb_incremental(PK));
  
    CREATE TABLE IF NOT EXISTS  `tb_irritacao_ocular` (
  `id` int NOT NULL AUTO_INCREMENT,
  `index` int,
  `FK` varchar(100) DEFAULT NULL,
  `codigo` varchar(100) DEFAULT NULL,
  `ordem` LONGTEXT DEFAULT NULL,
  `alteracao` LONGTEXT DEFAULT NULL,
  `24_1` VARCHAR(5) DEFAULT NULL,
  `48_1` VARCHAR(5) DEFAULT NULL,
  `72_1` VARCHAR(5) DEFAULT NULL,
  `21_1` VARCHAR(5) DEFAULT NULL,
  `24_2` VARCHAR(5) DEFAULT NULL,
  `48_2` VARCHAR(5) DEFAULT NULL,
  `72_2` VARCHAR(5) DEFAULT NULL,
  `21_2` VARCHAR(5) DEFAULT NULL,
  `24_3` VARCHAR(5) DEFAULT NULL,
  `48_3` VARCHAR(5) DEFAULT NULL,
  `72_3` VARCHAR(5) DEFAULT NULL,
  `21_3` VARCHAR(5) DEFAULT NULL,
  `media_1` DECIMAL(7,2) DEFAULT NULL,
  `media_2` DECIMAL(7,2) DEFAULT NULL,
  `media_3` DECIMAL(7,2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (FK) references tb_incremental(PK));
        """)

# tb_irritacao_cutanea_incremental, tb_irritacao_cutanea_MA, tb_irritacao_cutanea
cria_tabelas_irritacao_cutanea = ("""
        CREATE DATABASE IF NOT EXISTS `flora` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
    USE `flora`;

  CREATE TABLE IF NOT EXISTS  `tb_irritacao_cutanea_incremental` (
  `id` int NOT NULL AUTO_INCREMENT,
  `index` int,
  `FK` varchar(100) DEFAULT NULL,
  `MA_estudos` varchar(100) DEFAULT NULL,
  `MA_observacoes` LONGTEXT DEFAULT NULL,
  `dispensa` varchar(100) DEFAULT NULL,
  `dispensa_1` varchar(100) DEFAULT NULL,
  `dispensa_2` varchar(100) DEFAULT NULL,
  `dispensa_outra` varchar(100) DEFAULT NULL,
  `dispensa_justificativa` LONGTEXT DEFAULT NULL,
  `titulo` LONGTEXT DEFAULT NULL,
  `codigo` varchar(100) DEFAULT NULL,
  `laboratorio` LONGTEXT DEFAULT NULL,
  `bpl` varchar(12) DEFAULT NULL,
  `protocolo` varchar(100) DEFAULT NULL,
  `protocolo_outros` longtext DEFAULT NULL,
  `dt_inicio` varchar(20) DEFAULT NULL,
  `dt_conclusao` varchar(20) DEFAULT NULL,
  `certificado` varchar(100) DEFAULT NULL,
  `especie` varchar(100) DEFAULT NULL,
  `linhagem` varchar(100) DEFAULT NULL,
  `dose` varchar(100) DEFAULT NULL,
  `diluicao` varchar(100) DEFAULT NULL,
  `diluente` varchar(100) DEFAULT NULL,
  `lavagem` varchar(100) DEFAULT NULL,
  `tempo_apos_aplicacao` varchar(100) DEFAULT NULL,
  `tempo_total` varchar(12) DEFAULT NULL,
  `lesoes_1` varchar(12) DEFAULT NULL,
  `lesoes_2` varchar(12) DEFAULT NULL,
  `lesoes_3` varchar(12) DEFAULT NULL,
  `lesoes_4` varchar(12) DEFAULT NULL,
  `lesoes_5` varchar(12) DEFAULT NULL,
  `lesoes_6` varchar(12) DEFAULT NULL,
  `detalhamento_alteracoes` LONGTEXT DEFAULT NULL,
  `descricao_bula` LONGTEXT DEFAULT NULL,
  `discussao_adicional` varchar(12) DEFAULT NULL,
  `observacoes` LONGTEXT DEFAULT NULL,
  `conclusao` LONGTEXT DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (FK) references tb_incremental(PK));
  
  CREATE TABLE IF NOT EXISTS  `tb_irritacao_cutanea_MA` (
  `id` int NOT NULL AUTO_INCREMENT,
  `index` int,
  `FK` varchar(100) DEFAULT NULL,
  `codigo` varchar(100) DEFAULT NULL,
  `protocolo` LONGTEXT DEFAULT NULL,
  `resultados` LONGTEXT DEFAULT NULL,
  `classificacao` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (FK) references tb_incremental(PK));
  
    CREATE TABLE IF NOT EXISTS  `tb_irritacao_cutanea` (
  `id` int NOT NULL AUTO_INCREMENT,
  `index` int,
  `FK` varchar(100) DEFAULT NULL,
  `codigo` varchar(100) DEFAULT NULL,
  `ordem` INT DEFAULT NULL,
  `sexo` varchar(30) DEFAULT NULL,
  `eritema_1` DECIMAL(7,2) DEFAULT NULL,
  `edema_1` DECIMAL(7,2) DEFAULT NULL,
  `eritema_24` DECIMAL(7,2) DEFAULT NULL,
  `edema_24` DECIMAL(7,2) DEFAULT NULL,
  `eritema_48` DECIMAL(7,2) DEFAULT NULL,
  `edema_48` DECIMAL(7,2) DEFAULT NULL,
  `eritema_72` DECIMAL(7,2) DEFAULT NULL,
  `edema_72` DECIMAL(7,2) DEFAULT NULL,
  `eritema_media_24_48_72` DECIMAL(7,2) DEFAULT NULL,
  `edema_media_24_48_72` DECIMAL(7,2) DEFAULT NULL,
  
  PRIMARY KEY (`id`),
  FOREIGN KEY (FK) references tb_incremental(PK));
  
        """)



# CONTINUAR DAQUI=======================================

# tb_llna_incremental, tb_LLNA_preliminar, tb_LLNA_definitivo_individuos_grupos,
# tb_LLNA_definitivo_individuos_resultados, tb_LLNA_definitivo_grupos
cria_tabelas_llna = ("""
        CREATE DATABASE IF NOT EXISTS `flora` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
    USE `flora`;

  CREATE TABLE IF NOT EXISTS  `tb_llna_incremental` (
  `id` int NOT NULL AUTO_INCREMENT,
  `index` int,
  `FK` varchar(100) DEFAULT NULL,
  `titulo` LONGTEXT DEFAULT NULL,
  `codigo` varchar(100) DEFAULT NULL,
  `laboratorio` LONGTEXT DEFAULT NULL,
  `bpl` varchar(12) DEFAULT NULL,
  `protocolo` varchar(100) DEFAULT NULL,
  `protocolo_outros` longtext DEFAULT NULL,
  `dt_inicio` varchar(20) DEFAULT NULL,
  `dt_conclusao` varchar(20) DEFAULT NULL,
  `certificado` varchar(100) DEFAULT NULL,
  `especie` varchar(100) DEFAULT NULL,
  `linhagem` varchar(100) DEFAULT NULL,
  `tipo_estudo` varchar(100) DEFAULT NULL,
  `possui_controle_positivo` varchar(100) DEFAULT NULL,
  `possui_teste_confiabilidade` varchar(100) DEFAULT NULL,
  `dt_conclusao_confiabilidade` varchar(100) DEFAULT NULL,
  `justificativa_confiabilidade` LONGTEXT DEFAULT NULL,
  `preliminar_teste` varchar(100) DEFAULT NULL,
  `preliminar_solubilidade` varchar(100) DEFAULT NULL,
  `preliminar_espessura_orelha` varchar(100) DEFAULT NULL,
  `preliminar_eritema_superior_3` varchar(100) DEFAULT NULL,
  `preliminar_resultados` LONGTEXT DEFAULT NULL,
  `definitivo_abordagem` varchar(100) DEFAULT NULL,
  `definitivo_sexo` varchar(100) DEFAULT NULL,
  `definitivo_no_animais` varchar(100) DEFAULT NULL,
  `definitivo_resultados` LONGTEXT DEFAULT NULL,
  `discussao_adicional` varchar(12) DEFAULT NULL,
  `observacoes` LONGTEXT DEFAULT NULL,
  `conclusao` LONGTEXT DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (FK) references tb_incremental(PK));
        """)

# tb_sensibilizacao_incremental,tb_sensibilizacao_preliminar
cria_tabelas_sensibilizacao = ("""
        CREATE DATABASE IF NOT EXISTS `flora` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
    USE `flora`;

  CREATE TABLE IF NOT EXISTS  `tb_sensibilizacao_incremental` (
  `id` int NOT NULL AUTO_INCREMENT,
  `index` int,
  `FK` varchar(100) DEFAULT NULL,
  `titulo` LONGTEXT DEFAULT NULL,
  `codigo` varchar(100) DEFAULT NULL,
  `laboratorio` LONGTEXT DEFAULT NULL,
  `bpl` varchar(12) DEFAULT NULL,
  `protocolo` varchar(100) DEFAULT NULL,
  `protocolo_outros` longtext DEFAULT NULL,
  `dt_inicio` varchar(20) DEFAULT NULL,
  `dt_conclusao` varchar(20) DEFAULT NULL,
  `certificado` varchar(100) DEFAULT NULL,
  `especie` varchar(100) DEFAULT NULL,
  `linhagem` varchar(100) DEFAULT NULL,
  `metodo` varchar(100) DEFAULT NULL,
  `confiabilidade_teste` varchar(100) DEFAULT NULL,
  `confiabilidade_dt_conducao` varchar(100) DEFAULT NULL,
  `confiabilidade_metodo` varchar(100) DEFAULT NULL,
  `confiabilidade_ST` varchar(100) DEFAULT NULL,
  `confiabilidade_dose` varchar(100) DEFAULT NULL,
  `confiabilidade_diluente` varchar(100) DEFAULT NULL,
  `confiabilidade_resultado_24` varchar(100) DEFAULT NULL,
  `confiabilidade_resultado_48` varchar(100) DEFAULT NULL,
  `preliminar_resultados` LONGTEXT DEFAULT NULL,
  `preliminar_inducao_intradermica` varchar(100) DEFAULT NULL,
  `preliminar_inducao_topica` varchar(100) DEFAULT NULL,
  `preliminar_desafio_topica` varchar(100) DEFAULT NULL,
  `definitivo_no_animais_CN` varchar(100) DEFAULT NULL,
  `definitivo_no_animais_testados` varchar(100) DEFAULT NULL,
  `inducao_intradermica_1` varchar(100) DEFAULT NULL,
  `inducao_intradermica_2` varchar(100) DEFAULT NULL,
  `inducao_topica_1` varchar(100) DEFAULT NULL,
  `inducao_topica_2` varchar(100) DEFAULT NULL,
  `inducao_justificar_diferenca_doses` LONGTEXT DEFAULT NULL,
  `inducao_alteracoes_clinicas` LONGTEXT DEFAULT NULL,
  `desafio_dose` varchar(100) DEFAULT NULL,
  `desafio_justificar_diferenca_dose` LONGTEXT DEFAULT NULL,
  `desafio_tempo_inducao_desafio` varchar(100) DEFAULT NULL,
  `desafio_alteracoes_clinicas` LONGTEXT DEFAULT NULL,
  `desafio_resultado_24` varchar(100) DEFAULT NULL,
  `desafio_resultado_48` varchar(100) DEFAULT NULL,
  `redesafio_teste` varchar(100) DEFAULT NULL,
  `redesafio_tempo_desafio_redesafio` varchar(100) DEFAULT NULL,
  `redesafio_dose` varchar(100) DEFAULT NULL,
  `redesafio_alteracoes_clinicas` LONGTEXT DEFAULT NULL,
  `redesafio_resultado_24` varchar(100) DEFAULT NULL,
  `redesafio_resultado_48` varchar(100) DEFAULT NULL,
  `discussao_adicional` varchar(12) DEFAULT NULL,
  `observacoes` LONGTEXT DEFAULT NULL,
  `conclusao` LONGTEXT DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (FK) references tb_incremental(PK));
        """)

# tb_ames_incremental, tb_ames_testes,tb_ames_historico, tb_triplicatas_TA97, tb_triplicatas_TA97a,tb_triplicatas_TA98, tb_triplicatas_TA100,
# tb_triplicatas_TA102, tb_triplicatas_TA1535, tb_triplicatas_TA1537, tb_triplicatas_TA1538, tb_triplicatas_WP2_uvrA,
# tb_triplicatas_WP2_uvrA_pKM101
cria_tabelas_ames = ("""
        CREATE DATABASE IF NOT EXISTS `flora` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
    USE `flora`;

  CREATE TABLE IF NOT EXISTS  `tb_ames_incremental` (
  `id` int NOT NULL AUTO_INCREMENT,
  `index` int,
  `FK` varchar(100) DEFAULT NULL,
  `titulo` LONGTEXT DEFAULT NULL,
  `codigo` varchar(100) DEFAULT NULL,
  `laboratorio` LONGTEXT DEFAULT NULL,
  `bpl` varchar(12) DEFAULT NULL,
  `protocolo` varchar(100) DEFAULT NULL,
  `protocolo_outros` longtext DEFAULT NULL,
  `dt_inicio` varchar(20) DEFAULT NULL,
  `dt_conclusao` varchar(20) DEFAULT NULL,
  `certificado` varchar(100) DEFAULT NULL,
  `especies` varchar(100) DEFAULT NULL,
  `unidade_medida` varchar(100) DEFAULT NULL,
  `possui_atv_antimicrobiana` varchar(100) DEFAULT NULL,
  `efetuou_analises_geneticas` varchar(100) DEFAULT NULL,
  `esteve_entre_108_109` varchar(100) DEFAULT NULL,
  `utilizou_2_aminoantraceno` varchar(100) DEFAULT NULL,
  `utilizou_outro_mutageno` varchar(100) DEFAULT NULL,
  `no_outro_mutageno` varchar(100) DEFAULT NULL,
  `comprovante_outro_mutageno` varchar(100) DEFAULT NULL,
  `metodo_ctrl_historico` varchar(100) DEFAULT NULL,
  `discussao_adicional` varchar(12) DEFAULT NULL,
  `observacoes` LONGTEXT DEFAULT NULL,
  `conclusao` LONGTEXT DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (FK) references tb_incremental(PK));

        """)

# tb_micronucleo_incremental, tb_micronucleo_historico,  tb_micronucleo_preliminar, tb_micronucleo_proporcao_ep, tb_micronucleo_proporcao_epmn,
# tb_micronucleo_resultados
cria_tabelas_micronucleo = ("""
        CREATE DATABASE IF NOT EXISTS `flora` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
    USE `flora`;

  CREATE TABLE IF NOT EXISTS  `tb_micronucleo_incremental` (
  `id` int NOT NULL AUTO_INCREMENT,
  `index` int,
  `FK` varchar(100) DEFAULT NULL,
  `titulo` LONGTEXT DEFAULT NULL,
  `codigo` varchar(100) DEFAULT NULL,
  `laboratorio` LONGTEXT DEFAULT NULL,
  `bpl` varchar(12) DEFAULT NULL,
  `protocolo` varchar(100) DEFAULT NULL,
  `protocolo_outros` longtext DEFAULT NULL,
  `dt_inicio` varchar(20) DEFAULT NULL,
  `dt_conclusao` varchar(20) DEFAULT NULL,
  `certificado` varchar(100) DEFAULT NULL,
  `especie` varchar(100) DEFAULT NULL,
  `linhagem` varchar(100) DEFAULT NULL,
  `amostra` varchar(100) DEFAULT NULL,
  `via_administracao` varchar(100) DEFAULT NULL,
  `qt_administracoes` varchar(100) DEFAULT NULL,
  `tempo_coleta` varchar(100) DEFAULT NULL,
  `tempo_coleta_inicio` varchar(100) DEFAULT NULL,
  `tempo_coleta_termino` varchar(100) DEFAULT NULL,
  `tempo_coleta_unico` varchar(100) DEFAULT NULL,
  `st_controle_negativo` varchar(100) DEFAULT NULL,
  `cn_foi_testado_mais_de_uma_vez` varchar(100) DEFAULT NULL,
  `st_controle_positivo` varchar(100) DEFAULT NULL,
  `qt_dose_cp` varchar(100) DEFAULT NULL,
  `metodo` varchar(100) DEFAULT NULL,
  `controle_historico_origem` varchar(100) DEFAULT NULL,
  `controle_historico_periodo_1` varchar(100) DEFAULT NULL,
  `controle_historico_periodo_2` varchar(100) DEFAULT NULL,
  `controle_historico_qt_estudos_machos` varchar(100) DEFAULT NULL,
  `controle_historico_qt_estudos_femeas` varchar(100) DEFAULT NULL,
  `preliminar_teste` varchar(100) DEFAULT NULL,
  `preliminar_houve_diferenca_sexos` varchar(100) DEFAULT NULL,
  `preliminar_estudo_sem_DMT` varchar(100) DEFAULT NULL,
  `preliminar_qt_dmt_machos` varchar(100) DEFAULT NULL,
  `preliminar_qt_dmt_femeas` varchar(100) DEFAULT NULL,
  `preliminar_dmt_utilizou_dl50` varchar(100) DEFAULT NULL,
  `preliminar_justificativa_escolha_da_dmt` Longtext DEFAULT NULL,
  `preliminar_dl50_mesma_especie` varchar(100) DEFAULT NULL,
  `preliminar_dl50_mesmo_sexo` varchar(100) DEFAULT NULL,
  `preliminar_dl50_machos` varchar(100) DEFAULT NULL,
  `preliminar_dl50_femeas` varchar(100) DEFAULT NULL,
  `preliminar_dl50_minima_machos` varchar(100) DEFAULT NULL,
  `preliminar_dl50_inermediaria_machos` varchar(100) DEFAULT NULL,
  `preliminar_dl50_maxima_machos` varchar(100) DEFAULT NULL,
  `preliminar_dl50_minima_femeas` varchar(100) DEFAULT NULL,
  `preliminar_dl50_inermediaria_femeas` varchar(100) DEFAULT NULL,
  `preliminar_dl50_maxima_femeas` varchar(100) DEFAULT NULL,
  `definitivo_sexo` varchar(100) DEFAULT NULL,
  `definitivo_estudo_complementacao` varchar(100) DEFAULT NULL,
  `definitivo_evidencia_atingiu_medula` Longtext DEFAULT NULL,
  `definitivo_resultados_estatisticos` Longtext DEFAULT NULL,
  `definitivo_houve_aumento_epmn` varchar(100) DEFAULT NULL,
  `definitivo_houve_aumento_dose_resposta_epmn` varchar(100) DEFAULT NULL,
  `definitivo_resultados_fora_controle_historico` varchar(100) DEFAULT NULL,
  `definitivo_alteracoes_clinicas` Longtext DEFAULT NULL,
  `discussao_adicional` varchar(12) DEFAULT NULL,
  `observacoes` LONGTEXT DEFAULT NULL,
  `conclusao` LONGTEXT DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (FK) references tb_incremental(PK));
        """)

# tb_aditamentos_incremental, tb_aditamentos_discussao_incremental, tb_culturas_incremental, tb_classificao_estudo_anvisa_incremental,
# tb_classificao_estudo_empresa_incremental, tb_classificao_desfecho_incremental,
# tb_perguntas_nc_incremental, tb_comunicacao_perigo_incremental, tb_desvios,
# tb_alertas_incremental
cria_tabelas_adicionais = ("""
        CREATE DATABASE IF NOT EXISTS `flora` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
    USE `flora`;
    
CREATE TABLE IF NOT EXISTS  `tb_aditamentos_incremental` (
  `id` int NOT NULL AUTO_INCREMENT,
  `index` int,
  `FK` varchar(100) DEFAULT NULL,
  `assunto` longtext DEFAULT NULL,
  `expediente` varchar(100) DEFAULT NULL,
  `data` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (FK) references tb_incremental(PK));

  CREATE TABLE IF NOT EXISTS  `tb_aditamentos_discussao_incremental` (
  `id` int NOT NULL AUTO_INCREMENT,
  `index` int,
  `FK` varchar(100) DEFAULT NULL,
  `discussao` longtext DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (FK) references tb_incremental(PK));


  CREATE TABLE IF NOT EXISTS  `tb_culturas_incremental` (
  `id` int NOT NULL AUTO_INCREMENT,
  `index` int,
  `FK` varchar(100) DEFAULT NULL,
  `ordem` varchar(100) DEFAULT NULL,
  `cultura` varchar(100) DEFAULT NULL,
  `referencia` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (FK) references tb_incremental(PK));

  CREATE TABLE IF NOT EXISTS  `tb_classificao_estudo_anvisa_incremental` (
  `id` int NOT NULL AUTO_INCREMENT,
  `index` int,
  `FK` varchar(100) DEFAULT NULL,
  `desfecho` varchar(100) DEFAULT NULL,
  `estudo` varchar(100) DEFAULT NULL,
  `classificacao` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (FK) references tb_incremental(PK));

  CREATE TABLE IF NOT EXISTS  `tb_classificao_estudo_empresa_incremental` (
  `id` int NOT NULL AUTO_INCREMENT,
  `index` int,
  `FK` varchar(100) DEFAULT NULL,
  `desfecho` varchar(100) DEFAULT NULL,
  `estudo` varchar(100) DEFAULT NULL,
  `classificacao` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (FK) references tb_incremental(PK));


  CREATE TABLE IF NOT EXISTS  `tb_classificao_desfecho_incremental` (
  `id` int NOT NULL AUTO_INCREMENT,
  `index` int,
  `FK` varchar(100) DEFAULT NULL,
  `desfecho` varchar(100) DEFAULT NULL,
  `classificacao` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (FK) references tb_incremental(PK));
  

  CREATE TABLE IF NOT EXISTS  `tb_perguntas_nc_incremental` (
  `id` int NOT NULL AUTO_INCREMENT,
  `index` int,
  `FK` varchar(100) DEFAULT NULL,
  `pergunta_1` varchar(100) DEFAULT NULL,
  `pergunta_2` varchar(100) DEFAULT NULL,
  `pergunta_3` varchar(100) DEFAULT NULL,
  `pergunta_4` varchar(100) DEFAULT NULL,
  `pergunta_5` varchar(100) DEFAULT NULL,
  `pergunta_6` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (FK) references tb_incremental(PK));

  
  CREATE TABLE IF NOT EXISTS  `tb_comunicacao_perigo_incremental` (
  `id` int NOT NULL AUTO_INCREMENT,
  `index` int,
  `FK` varchar(100) DEFAULT NULL,
  `Palavra_advertencia` varchar(100) DEFAULT NULL,
  `frase_oral` longtext DEFAULT NULL,
  `frase_cutanea` longtext DEFAULT NULL,
  `frase_inalatoria` longtext DEFAULT NULL,
  `frase_ocular` longtext DEFAULT NULL,
  `frase_irritacao_cutanea` longtext DEFAULT NULL,
  `frase_sensibilizacao` longtext DEFAULT NULL,
  `frase_mutagenicidade` longtext DEFAULT NULL,
  `frase_1` longtext DEFAULT NULL,
  `frase_2` longtext DEFAULT NULL,
  `frase_3` longtext DEFAULT NULL,
  `frase_4` longtext DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (FK) references tb_incremental(PK));

  CREATE TABLE IF NOT EXISTS  `tb_desvios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `index` int,
  `FK` varchar(100) DEFAULT NULL,
  `estudo` varchar(100) DEFAULT NULL,
  `codigo_estudo` longtext DEFAULT NULL,
  `desvio_descricao` longtext DEFAULT NULL,
  `desvio_argumentacao` longtext DEFAULT NULL,
  `desvio_interferiu_nos_resultados` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (FK) references tb_incremental(PK));


  CREATE TABLE IF NOT EXISTS  `tb_alertas_incremental` (
  `id` int NOT NULL AUTO_INCREMENT,
  `index` int,
  `FK` varchar(100) DEFAULT NULL,
  `estudo` varchar(100) DEFAULT NULL,
  `ds_alerta` longtext DEFAULT NULL,
  `acao_tomada` varchar(30) DEFAULT NULL,
  `alerta_gerado` longtext DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (FK) references tb_incremental(PK));
  
  CREATE TABLE IF NOT EXISTS  `tb_culturas_incremental` (
  `id` int NOT NULL AUTO_INCREMENT,
  `index` int,
  `FK` varchar(100) DEFAULT NULL,
  `ordem` varchar(100) DEFAULT NULL,
  `cultura` varchar(100) DEFAULT NULL,
  `referencia` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (FK) references tb_incremental(PK));
  
    CREATE TABLE IF NOT EXISTS  `tb_campos_preenchidos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `index` int,
  `FK` varchar(100) DEFAULT NULL,
  `tb_incremental` INT DEFAULT NULL,
  `tb_pt` INT DEFAULT NULL,
  `tb_composicao_incremental` INT DEFAULT NULL,
  `tb_composicao` INT DEFAULT NULL,
  `tb_certificados_incremental` INT DEFAULT NULL,
  `tb_certificados` INT DEFAULT NULL,
  `tb_laudos_incremental` INT DEFAULT NULL,
  `tb_laudos` INT DEFAULT NULL,
  `tb_formuladores_incremental` INT DEFAULT NULL,
  `tb_formuladores` INT DEFAULT NULL,
  `tb_fq_incremental` INT DEFAULT NULL,
  `tb_fq` INT DEFAULT NULL,
  `tb_updown_incremental` INT DEFAULT NULL,
  `tb_updown` INT DEFAULT NULL,
  `tb_dl50oral_incremental` INT DEFAULT NULL,
  `tb_dl50oral` INT DEFAULT NULL,
  `tb_dl50cutanea_incremental` INT DEFAULT NULL,
  `tb_dl50cutanea` INT DEFAULT NULL,
  `tb_cl50_incremental` INT DEFAULT NULL,
  `tb_cl50` INT DEFAULT NULL,
  `tb_irritacao_ocular_incremental` INT DEFAULT NULL,
  `tb_irritacao_ocular_ma` INT DEFAULT NULL,
  `tb_irritacao_ocular` INT DEFAULT NULL,
  `tb_irritacao_cutanea_incremental` INT DEFAULT NULL,
  `tb_irritacao_cutanea_ma` INT DEFAULT NULL,
  `tb_irritacao_cutanea` INT DEFAULT NULL,
  `tb_llna_incremental` INT DEFAULT NULL,
  `tb_LLNA_preliminar` INT DEFAULT NULL,
  `tb_LLNA_definitivo_individuos_grupos` INT DEFAULT NULL,
  `tb_LLNA_definitivo_individuos_resultados` INT DEFAULT NULL,
  `tb_LLNA_definitivo_grupos` INT DEFAULT NULL,
  `tb_sensibilizacao_incremental` INT DEFAULT NULL,
  `tb_sensibilizacao_preliminar` INT DEFAULT NULL,
  `tb_ames_incremental` INT DEFAULT NULL,
  `tb_ames_testes` INT DEFAULT NULL,
  `tb_triplicatas_TA97` INT DEFAULT NULL,
  `tb_triplicatas_TA97a` INT DEFAULT NULL,
  `tb_triplicatas_TA98` INT DEFAULT NULL,
  `tb_triplicatas_TA100` INT DEFAULT NULL,
  `tb_triplicatas_TA102` INT DEFAULT NULL,
  `tb_triplicatas_TA1535` INT DEFAULT NULL,
  `tb_triplicatas_TA1537` INT DEFAULT NULL,
  `tb_triplicatas_TA1538` INT DEFAULT NULL,
  `tb_triplicatas_WP2_uvrA` INT DEFAULT NULL,
  `tb_triplicatas_WP2_uvrA_pKM101` INT DEFAULT NULL,
  `tb_micronucleo_incremental` INT DEFAULT NULL,
  `tb_micronucleo_historico` INT DEFAULT NULL,
  `tb_micronucleo_preliminar` INT DEFAULT NULL,
  `tb_micronucleo_proporcao_ep` INT DEFAULT NULL,
  `tb_micronucleo_proporcao_epmn` INT DEFAULT NULL,
  `tb_micronucleo_resultados` INT DEFAULT NULL,
  `tb_micronucleo_doses` INT DEFAULT NULL,
  `tb_aditamentos_incremental` INT DEFAULT NULL,
  `tb_aditamentos_discussao_incremental` INT DEFAULT NULL,
  `tb_culturas_incremental` INT DEFAULT NULL,
  `tb_classificao_estudo_anvisa_incremental` INT DEFAULT NULL,
  `tb_classificao_estudo_empresa_incremental` INT DEFAULT NULL,
  `tb_classificao_desfecho_incremental` INT DEFAULT NULL,
  `tb_perguntas_nc_incremental` INT DEFAULT NULL,
  `tb_comunicacao_perigo_incremental` INT DEFAULT NULL,
  `tb_desvios` INT DEFAULT NULL,
  `tb_alertas_incremental` INT DEFAULT NULL, 
   PRIMARY KEY (`id`),
   FOREIGN KEY (FK) references tb_incremental(PK));
  
        """)

cursor.execute(cria_tb_incremental)
cursor.execute(cria_tabelas_iniciais)
cursor.execute(cria_tabelas_updown)
cursor.execute(cria_tabelas_dloral)
cursor.execute(cria_tabelas_dlcutanea)
cursor.execute(cria_tabelas_clinalatoria)
cursor.execute(cria_tabelas_irritacao_ocular)
cursor.execute(cria_tabelas_irritacao_cutanea)
cursor.execute(cria_tabelas_llna)
cursor.execute(cria_tabelas_sensibilizacao)
cursor.execute(cria_tabelas_ames)
cursor.execute(cria_tabelas_micronucleo)
cursor.execute(cria_tabelas_adicionais)
conn.close()
