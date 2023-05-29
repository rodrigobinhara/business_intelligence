import pandas as pd

df = pd.read_excel('Saída.xlsx', sheet_name=0) # Carrega a planilha

# Dicionário com as palavras que você deseja substituir e suas correções
word_mapping = {
    'AcrelÃ¢ndia': 'Acrelândia',
    'BrasilÃ©ia': 'Brasilândia',
    'EpitaciolÃ¢ndia': 'Epitaciolândia',
    'FeijÃ³': 'Feijó',
    'JordÃ£o': 'Jordão',
    'MÃ¢ncio Lima': 'Mâncio Lima',
    'MaceiÃ³': 'Maceió',
    'PlÃ¡cido de Castro': 'Plácido de Castro',
    'Porto Real do ColÃ©gio': 'Porto Real do Colégio',
    'TarauacÃ¡': 'Tarauacá'
    }

# Substituir as palavras na coluna 'city'
df['city'] = df['city'].replace(word_mapping)

df['City Code Prefix'] = df['city_ibge_code'].apply(lambda x: str(x)[:2]) # Cria a coluna 'City Code Prefix' com os dois primeiros caracteres de 'City Ibge Code'

df['Prev City Code Prefix'] = df['City Code Prefix'].shift() # Cria coluna 'Prev City Code Prefix' com o valor de 'City Code Prefix' da linha anterior

df['Prev City'] = df['city'].shift() # Cria coluna 'Prev City' com o valor de 'City' da linha anterior

mask = df['city'].isnull() & (df['City Code Prefix'] == df['Prev City Code Prefix']) # Se 'City' é nulo e 'City Code Prefix' é igual a 'Prev City Code Prefix', substituir 'City' por 'Prev City'
df.loc[mask, 'city'] = df.loc[mask, 'Prev City']

df = df.drop(columns=['City Code Prefix', 'Prev City Code Prefix', 'Prev City']) # Remove as colunas auxiliares

df['city/Estado'] = df['city'] + '/' + df['Estado'] # Criação da colunna Cidade/Estado

df.to_excel('multas (teste_dados)_DADOS_COVID_v2.xlsx', index=False) # Salva o DataFrame modificado de volta para um novo arquivo Excel


