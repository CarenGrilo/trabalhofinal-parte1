import sqlite3
import extract
import notification

def criar_connection(): 
    return sqlite3.connect("banco.db")

def criar_cursor_e_tabelas():
    connection = criar_connection()
    cursor = connection.cursor()
    #cursor.execute("DROP TABLE IF EXISTS cidades")
    #cursor.execute("DROP TABLE IF EXISTS previsao")
    #cursor.execute("DROP TABLE IF EXISTS ondas")
    cursor.execute("CREATE TABLE IF NOT EXISTS cidades (id INTEGER, nome TEXT, estado TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS previsao (cidade TEXT, data TEXT, min INTEGER, max INTEGER)")
    cursor.execute("CREATE TABLE IF NOT EXISTS ondas (cidade TEXT, data TEXT, vento TEXT, direcao_vento TEXT)")
    connection.commit()
    return cursor

def popular():
    connection = criar_connection()
    cursor = connection.cursor()
    cidades = extract.extract_cities()

    for cidade in cidades:
        cursor.execute(f"INSERT INTO cidades VALUES ('{cidade['id']}', '{cidade['nome']}', '{cidade['estado']}')")
        previsao = extract.forecast_weather(cidade['id'])
        cursor.execute(f"INSERT INTO previsao VALUES ('{previsao['cidade']}', '{previsao['clima'][0]['data']}', '{previsao['clima'][0]['min']}', '{previsao['clima'][0]['max']}')")
        ondas = extract.forecast_waves(cidade['id'])
        if 'name' in ondas:
            print(f"Erro ao buscar previsão de ondas para a cidade {cidade['nome']}")
            #notification.notify("Erro ao buscar previsão de ondas", f"Cidade {cidade['nome']} não encontrada")
        else:
            cursor.execute(f"INSERT INTO ondas VALUES ('{ondas['cidade']}', '{ondas['ondas'][0]['data']}', '{ondas['ondas'][0]['dados_ondas'][0]['vento']}', '{ondas['ondas'][0]['dados_ondas'][0]['direcao_vento']}')")

    connection.commit()

def checar_banco():
    connection = criar_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT count(*) FROM cidades")
    num_cidades = cursor.fetchone()
    cursor.execute("SELECT count(*) FROM previsao")
    num_previsao = cursor.fetchone()
    cursor.execute("SELECT count(*) FROM ondas")
    num_ondas = cursor.fetchone()
    print(f"{num_cidades} cidades cadastradas")
    print(f"{num_previsao} previsões de tempo cadastradas")
    print(f"{num_ondas} previsões de ondas cadastradas")
    connection.close()
