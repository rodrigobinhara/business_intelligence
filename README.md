# business_intelligence
Projetos de business intelligence, entre outros.

PASSOS PARA EXECUÇÃO DO DESAFIO

Os pasoss com as telas podem ser encontrados no arquivo "Passos para a Execução do Desafio - Rodrigo Binhara.pdf"

Prezados senhores,

Desde já gostaria de agradecer o desafio enviado e gostaria de descrever aqui os passos da realização.

Ao entender o que o desafio solicitou, busquei construir os entregáveis buscando o diferencial de fazer o ETL fora do Power BI, usando para tal a ferramenta Tableau, mas posteriormente tive que usar o Python para completar a fase de transformação dos dados e por fim, utilizar como front-end o Power BI.

EXTRAÇÃO TABLEAU (arquivo: ETL_MongoDB_mySQL_v2.twb)
De início, ao utilizar o Tableau Prep Builder, não encontrei nativamente um conector para o MongoDB, tentei instalar vários drivers trial ODBC e JDBC, mas infelizmente não funcionaram com a credenciais enviadas, não devido às credenciais (que foram liberadas pela T.I.), mas pelas formas de conexão que realmente não darem certo.
Em seguida lembrei que a ferramenta Tableau (visualizador) também faz conexões e que alguns drivers nesta ferramenta funcionam mais que o Prep Builder (não sei por qual motivo). Feito isso, consegui baixar um driver trial genérico do ODBC MongoDB que permitiu fazer a conexão com os dados (este driver não funcionou no Prep Builder).
Para dar continuidade ao Desafio, já que o Tableau (Visualizador) não fornece amplas possibilidades de transformação de dados, exportei a tabela Multas como .csv para então utilizá-lo no Prep Builder:
O conector nativo do MySQL funcionou tranquilamente no Prep Builder + a importação do arquivo .csv para seguir com a Transformação dos dados. 

TRANSFORMAÇÃO 01 TABLEAU (arquivo: ETL_MongoDB_mySQL.tfl)
Realizada a concatenação das fatos, o primeiro ponto que não realizado dentro do Prep Builder foi o enriquecimento de dados na tabela de COVID da coluna “city” devido ao fato do Tableau trabalhar com linhas não buscando referência em outras e segundo, a correção dos nomes das Cidades nesta coluna. Por consequência, não realizei dentro desta ferramenta também a criação da coluna Cidade/Estado. 
Desta forma, configurei uma saída em arquivo .xlsx para salvar a tabelas fato concatenada em um arquivo só: (arquivo:Saída.xlsx).
 
TRANSFORMAÇÃO 02 PYTHON: (arquivo: multas_teste_dados_dados_covid_v2_tranf_phyton.py)
A partir disso utilizei o Python para executar o que faltava transformar na coluna “city”.
Aqui gerei um arquivo .xlsx com o campo “city” totalmente preenchido, as palavras com caracteres especiais corrigidos e a criação da coluna Cidade/Estado na tabela COVID: (arquivo: multas (teste_dados)_DADOS_COVID_v2.xlsx)
 

FRONT-END POWER BI: (arquivo: Desafio - Rodrigo Binhara.pbix)
No Power BI, optei por modelar uma tabela de Calendário aqui pois eu já tinha um outro arquivo com a tabela pronta, assim foi tranquilo linkar os dados.
Como o Desafio pede apenas 01 dashboard, procurei montar um tema estililizado da Builders e aninhar todos os objetos em um aba só.
 


