# Importando bibliotecas nativas do Python para não utilizar Pandas
import csv # usada para ler os dados em CSV
import os # usada para colocar o path do arquivo

# Nome do Sistema 
nome_sistema = "Sistema Inteligente de Monitoramento Espacial - Aurora Siger"

# Try e Except para poder achar e rodar o arquivo .csv tanto em arquivos .py como em .ipynb 

try:
    # Caminho base do projeto 
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # caso esteja rodando em terminal
except NameError:
    base_dir = os.getcwd() # caso esteja rodando em notebook (jupyter)

    if os.path.basename(base_dir) == "src": 
        base_dir = os.path.dirname(base_dir)
        
# Caminho do arquivo CSV dos dados 
caminho_telemetria = os.path.join(base_dir, "data", "dados.csv")

print("Caminho do CSV:", caminho_telemetria) # Caminho do arquivo 
print("Arquivo existe?", os.path.exists(caminho_telemetria)) #True or False 

# Módulos Críticos da Missão 

modulos_criticos = [
    "suporte_vida", 
    "energia", 
    "comunicacao", 
    "habitat", 
    "laboratorio", 
    "armazenamento", 
    "navegacao", 
    "propulsao_auxiliar"
]

# Limites de Segurança da Missão

limites_seguranca = {
    "energia_minima_alerta": 40, 
    "energia_minima_critica": 25, 
    "temperatura_interna_minima": 18, 
    "temperatura_interna_maxima": 28, 
    "temperatura_interna_critica": 34, 
    "qualidade_comunicacao_minima": 50, 
    "consumo_alto": 75
}

# Hierarquia da missão

hierarquia_missao = {
    "energia": {
        "solar": "gera energia renovável", 
        "baterias": "armazena energia reserva", 
        "consumo": "mede o gasto energético da missão"
    }, 
    "habitat": {
        "oxigenio": "mantém condições de sobrevivência",
        "temperatura": "controla o ambiente interno", 
        "comunicacao": "mantém contato com a base"
    }, 
    "seguranca": {
        "radiacao": "monitora exposição perigosa", 
        "sensores": "validam leituras da missão", 
        "alertas": "registram situações anormais"
    }
}

# Função para criar um cenário

def criar_cenario(
    nome,
    descricao,
    classificacao_esperada,
    modulos, 
    energia, 
    ambiente,
    historico_reserva, 
    historico_consumo, 
    historico_temperatura, 
    leituras, 
    log_eventos, 
    alertas_pendentes, 
    eventos_criticos, 
    inconsistencia_proposital, 
    recomendacao_inicial
): 
    cenario = {
        "nome": nome,
        "descricao": descricao,
        "classificacao_esperada": classificacao_esperada, 
        "modulos": modulos, 
        "energia": energia, 
        "ambiente": ambiente, 
        "historico_reserva": historico_reserva, 
        "historico_consumo": historico_consumo, 
        "historico_temperatura": historico_temperatura, 
        "leituras": leituras, 
        "log_eventos": log_eventos, 
        "alertas_pendentes": alertas_pendentes, 
        "eventos_criticos": eventos_criticos, 
        "inconsistencia_proposital": inconsistencia_proposital, 
        "recomendacao_inicial": recomendacao_inicial
    }

    return cenario

# Leitura de arquivo csv de telemetria
def converter_linha_csv(linha): 
    campos_inteiros = [
        "cenario_id", 
        "suporte_vida", 
        "energia", 
        "comunicacao", 
        "habitat", 
        "laboratorio", 
        "armazenamento", 
        "navegacao", 
        "propulsao_auxiliar", 
        "reserva_percentual", 
        "consumo_kwh", 
        "geracao_solar_kwh", 
        "geracao_auxiliar_kwh", 
        "temperatura_interna", 
        "temperatura_externa", 
        "qualidade_comunicacao", 
        "velocidade_vento", 
        "integridade_sensores"
    ]

    for campo in campos_inteiros:
        linha[campo] = int(linha[campo])

    return linha

# Ler a telemetria do arquivo dados.csv
def ler_telemetria_csv(caminho_arquivo):
    dados = [] 

    with open(caminho_arquivo, mode="r", encoding="utf-8-sig") as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor: 
            linha_convertida = converter_linha_csv(linha)
            dados.append(linha_convertida)

        return dados 
    
    # Filtrando telemetria por cenário
def filtrar_telemetria_por_cenario(dados_telemetria, cenario_id): 
    linhas_do_cenario = []

    for linha in dados_telemetria:
        if linha["cenario_id"] == int(cenario_id):
            linhas_do_cenario.append(linha)

    return linhas_do_cenario

def montar_cenario_a_partir_csv(linhas_cenario):
    if len(linhas_cenario) == 0: 
        raise ValueError("Nenhuma telemetria encontrada para esse cenário.")
    
    primeira_linha = linhas_cenario[0]
    ultima_linha = linhas_cenario[-1]
    
    modulos = {
        "suporte_vida": ultima_linha["suporte_vida"], 
        "energia": ultima_linha["energia"], 
        "comunicacao": ultima_linha["comunicacao"],
        "habitat": ultima_linha["habitat"], 
        "laboratorio": ultima_linha["laboratorio"], 
        "armazenamento": ultima_linha["armazenamento"],
        "navegacao": ultima_linha["navegacao"],
        "propulsao_auxiliar": ultima_linha["propulsao_auxiliar"]
    }
    
    energia = {
        "reserva_percentual": ultima_linha["reserva_percentual"],
        "consumo_kwh": ultima_linha["consumo_kwh"], 
        "geracao_solar_kwh": ultima_linha["geracao_solar_kwh"], 
        "geracao_auxiliar_kwh": ultima_linha["geracao_auxiliar_kwh"]
    }
    
    ambiente = {
        "temperatura_interna": ultima_linha["temperatura_interna"], 
        "temperatura_externa": ultima_linha["temperatura_externa"], 
        "radiacao": ultima_linha["radiacao"], 
        "qualidade_comunicacao": ultima_linha["qualidade_comunicacao"], 
        "velocidade_vento": ultima_linha["velocidade_vento"], 
        "integridade_sensores": ultima_linha["integridade_sensores"]
    }

    historico_reserva = []
    historico_consumo = []
    historico_temperatura = [] 
    leituras = []
    log_eventos = []
    alertas_pendentes = [] 
    eventos_criticos = []

    for linha in linhas_cenario:
        historico_reserva.append(linha["reserva_percentual"])
        historico_consumo.append(linha["consumo_kwh"])
        historico_temperatura.append(linha["temperatura_interna"])

        leitura = [
            linha["horario"], 
            linha["geracao_solar_kwh"], 
            linha["consumo_kwh"], 
            linha["reserva_percentual"],
            linha["temperatura_interna"],
            linha["qualidade_comunicacao"]
        ]

        leituras.append(leitura) 

        if linha["evento_log"] != "": 
            log_eventos.append(linha["evento_log"])

        if linha["alerta_pendente"] != "":
            alertas_pendentes.append(linha["alerta_pendente"])

        if linha["evento_critico"] != "":
            eventos_criticos.append(linha["evento_critico"])

    cenario = {
        "nome": primeira_linha["cenario_nome"], 
        "descricao": primeira_linha["cenario_descricao"], 
        "classificacao_esperada": primeira_linha["classificacao_esperada"], 
        "modulos": modulos,
        "energia": energia,
        "ambiente": ambiente,
        "historico_reserva": historico_reserva, 
        "historico_consumo": historico_consumo, 
        "historico_temperatura": historico_temperatura, 
        "leituras": leituras,
        "log_eventos": log_eventos,
        "alertas_pendentes": alertas_pendentes, 
        "eventos_criticos": eventos_criticos, 
        "inconsistencia_proposital": primeira_linha["inconsistencia_proposital"] == "sim", 
        "recomendacao_inicial": primeira_linha["recomendacao_inicial"]
    }

    return cenario

# Função para exibir o menu principal 
def exibir_menu():

    print("\n" + "=" * 60)
    print(nome_sistema)
    print("=" * 60)
    print("Escolha um Cenário para Análise:")
    print("1   - Cenário Normal")
    print("2   - Cenário de Energia Baixa")
    print("3   - Cenário de Falha na Comunicação")
    print("4   - Cenário de Radiação Elevada")
    print("5   - Cenário Crítico Geral")
    print("6   - Cenário de Falha no Suporte à Vida")
    print("7   - Cenário de Superaquecimento Interno")
    print("8   - Cenário de Baixa Geração Solar por Tempestade de Poeira")
    print("9   - Cenário de Inconsistência nos Sensores")
    print("10  - Cenário de Modo Economia Preventiva")
    print('sair - Encerrar Sistema')
    print("=" * 60) 

# Função para exibir status dos módulos 
def exibir_modulos(modulos):
    print("\nSTATUS DOS MÓDULOS CRÍTICOS")
    print("-" * 60)
    
    for nome_modulo, status in modulos.items():
        if status == 1:
            texto_status = "NORMAL"
        else:
            texto_status = "FALHA"
    
        print(f"{nome_modulo:22} -> {status} ({texto_status})")

# Função para exibir dados de energia 
def exibir_energia(energia):
    print("\nDADOS DE ENERGIA")
    print("-" * 60)
    print(f"Reserva Energética:..........{energia['reserva_percentual']}%")
    print(f"Consumo Atual:...............{energia['consumo_kwh']} kWh")
    print(f"Geração Solar:...............{energia['geracao_solar_kwh']} kWh")
    print(f"Geração Auxliar:.............{energia['geracao_auxiliar_kwh']} kWh")

# Função para exibir dados ambientais
def exibir_ambiente(ambiente):
    print("\nDADOS AMBIENTAIS")
    print("-" * 60)
    print(f"Temperatura Interna:.........{ambiente['temperatura_interna']} °C")
    print(f"Temperatura Externa:.........{ambiente['temperatura_externa']} °C")
    print(f"Radiação:....................{ambiente['radiacao']}")
    print(f"Qualidade de Comunicação:....{ambiente['qualidade_comunicacao']}%")
    print(f"Velocidade do Vento:.........{ambiente['velocidade_vento']} km/h")
    print(f"Integridade dos Sensores:....{ambiente['integridade_sensores']}%")

# Função para exibir histórico em listas 
def exibir_historico(cenario): 
    print("\nHISTÓRICO")
    print("-" * 60)
    print(f"Histórico de Reserva:.........{cenario['historico_reserva']}")
    print(f"Histórico de Consumo:.........{cenario['historico_consumo']}")
    print(f"Histórico de Temperatura:.....{cenario['historico_temperatura']}")

# Função para exibir matriz de leituras 
def exibir_matriz_leituras(leituras):
    print("\nMATRIZ DE LEITURAS POR HORÁRIO")
    print("-" * 60)
    print(f"{'Horário':8} {'Geração':10} {'Consumo':10} {'Reserva':10} {'Temperatura':8} {'Comunicação':8}")

    for linha in leituras: 
        horario = linha[0]
        geracao = linha[1]
        consumo = linha[2]
        reserva = linha[3]
        temperatura = linha[4]
        comunicacao = linha[5]

        print(f"{horario:8} {geracao:<10} {consumo:<10} {reserva:<10} {temperatura:<8} {comunicacao:<8}")

# Função para exibir log de eventos 
def exibir_log_eventos(log_eventos):
    print("\nLOG DE EVENTOS")
    print("-" * 60)
    
    for indice, evento in enumerate(log_eventos, start=1):
        print(f"{indice}. {evento}")

# Função para exibir fila de alertas 
def exibir_fila_alertas(alertas):
    print("\nFILA DE ALERTAS PENDENTES")
    print("-" * 60)

    if len(alertas) == 0: 
        print("Não há alertas pendentes.")
    else:
        for indice, alerta in enumerate(alertas, start=1):
            print(f"{indice}. {alerta}")

# Função para exibir pilha de eventos críticos
def exibir_pilha_eventos_criticos(eventos_criticos): 
    print("\nPILHA DE EVENTOS CRÍTICOS")
    print("-" * 60)

    if len(eventos_criticos) == 0: 
        print("Nenhum evento crítico registrado.")
    else:
        print("Topo da pilha aparece por último na lista.")
        for indice, evento in enumerate(eventos_criticos, start=1):
            print(f"{indice}. {evento}")

# Criando tabela status modulos

def criar_tabela_status_modulos(modulos):
    tabela = []

    for nome_modulo, valor_binario in modulos.items():
        if valor_binario == 1: 
            status = "NORMAL"
            criticidade = "BAIXA"
            explicacao = "Módulo funcionando corretamente."
        else:
            status = "FALHA"

            if nome_modulo in ["suporte_vida", "energia", "comunicacao", "habitat"]:
                criticidade = "ALTA"
                explicacao = "Módulo essencial comprometido."
            else:
                criticidade = "MÉDIA"
                explicacao = "Módulo importante apresenta falha."
        linha = {
            "modulo": nome_modulo,
            "valor_binario": valor_binario, 
            "status": status,
            "criticidade": criticidade,
            "explicacao": explicacao
        }

        tabela.append(linha)

    return tabela

# Exibir tabela de status dos módulos 
def exibir_tabela_status_modulos(modulos):
    tabela = criar_tabela_status_modulos(modulos)

    print("\nTABELA DE STATUS DOS MÓDULOS")
    print("-" * 90)
    print(f"{'Módulo':22} {'Valor':8} {'Status':12} {'Criticidade':14} {'Explicação'} ")
    print("-" * 90) 

    for linha in tabela: 
        print(
            f"{linha['modulo']:22} "
            f"{linha['valor_binario']:<8} "
            f"{linha['status']:12} "
            f"{linha['criticidade']:14} "
            f"{linha['explicacao']} "
        )

def exibir_busca_modulos_essenciais(modulos):
    modulos_essenciais = ["suporte_vida", "energia", "comunicacao", "habitat"]

    print("\nBUSCA RÁPIDA EM DICIONÁRIO - MÓDULOS ESSENCIAIS")
    print("-" * 70)

    for modulo in modulos_essenciais:
        valor = modulos.get(modulo)

        if valor == 1:
            status = "NORMAL"
        elif valor == 0:
            status = "FALHA"
        else:
            status = "NÃO ENCONTRADO"

        print(f"{modulo:20} -> {status}")

# Criar vetor de energia 
def criar_vetor_energia(energia):
    vetor_energia = [
        energia["reserva_percentual"], 
        energia["consumo_kwh"], 
        energia["geracao_solar_kwh"], 
        energia["geracao_auxiliar_kwh"]
    ]

    return vetor_energia

# Exibir vetor de energia 
def exibir_vetor_energia(energia):
    vetor = criar_vetor_energia(energia)

    print("\nVETOR DE ENERGIA")
    print("-" * 60)
    print("Posição 0 - Reserva Energética: ", vetor[0], "%")
    print("Posição 1 - Consumo Atual: ", vetor[1], "kWh")
    print("Posição 2 - Geração Solar: ", vetor[2], "kWh")
    print("Posição 3 - Geração Auxiliar: ", vetor[3], "kWh")

# Analisar tendência simples de uma lista 
def analisar_tendencia_lista(lista_valores):
    if len(lista_valores) == 0:
        return "sem dados"

    primeiro = lista_valores[0]
    ultimo = lista_valores[-1]

    if ultimo > primeiro: 
        return "aumento"
    elif ultimo < primeiro:
        return "queda"
    else:
        return "estabilidade"
    
# Exibir resumo das listas históricas 
def exibir_resumo_listas(cenario): 
    historico_reserva = cenario["historico_reserva"]
    historico_consumo = cenario["historico_consumo"]
    historico_temperatura = cenario["historico_temperatura"]

    print("\nRESUMO DAS LISTAS HISTÓRICAS")
    print("-" * 70)

    print("Reserva Energética:")
    print(f"   Valores Registrados: {historico_reserva}")
    print(f"   Quantidade de Registros: {len(historico_reserva)}")
    print(f"   Tendência Simples: {analisar_tendencia_lista(historico_reserva)}")

    print("\nConsumo Energético:")
    print(f"   Valores Registrados: {historico_consumo}")
    print(f"   Quantidade de Registros: {len(historico_consumo)}")
    print(f"   Tendência Simples: {analisar_tendencia_lista(historico_consumo)}")    

# Exibir resumo da matriz de leituras 
def exibir_resumo_matriz(leituras):
    quantidade_linhas = len(leituras)

    if quantidade_linhas > 0:
        quantidade_colunas = len(leituras[0])
    else:
        quantidade_colunas = 0

    print("\nRESUMO DA MATRIZ")
    print("-" * 60)
    print(f"Quantidade de Linhas:  {quantidade_linhas}")
    print(f"Quantidade de Colunas: {quantidade_colunas}")
    print("Cada linha representa um horário de leitura da missão.")
    print("Cada coluna representa uma variável monitorada.")

# Classificar prioridade textual de alerta
def classificar_prioridade_alerta(alerta):
    alerta_minusculo = alerta.lower()

    palavras_criticas = [
        "suporte à vida", 
        "emergência", 
        "desligar", 
        "redirecionar", 
        "radiação", 
        "crítico"
    ]

    palavras_alerta = [
        "reduzir", 
        "verificar", 
        "validar", 
        "economia", 
        "acompanhar", 
        "reiniciar"
    ]

    for palavra in palavras_criticas:
        if palavra in alerta_minusculo: 
            return "ALTA"

    for palavra in palavras_alerta: 
        if palavra in alerta_minusculo:
            return "MÉDIA"

    return "BAIXA"

# Organizar fila de alertas 
def organizar_fila_alertas(alertas): 
    fila_estruturada = [] 

    for indice, alerta in enumerate(alertas, start=1): 
        item_fila = {
            "ordem_chegada": indice,
            "mensagem": alerta,
            "prioridade": classificar_prioridade_alerta(alerta)
        }

        fila_estruturada.append(item_fila) 

    return fila_estruturada

# Exibir fila de alertas estruturada
def exibir_fila_alertas_estruturada(alertas):
    fila = organizar_fila_alertas(alertas) 

    print("\nFILA DE ALERTAS ESTRUTURADA")
    print("-" * 80)

    if len(fila) == 0:
        print("Não há alertas pendentes.")
        return 

    print(f"{'Ordem':8} {'Prioridade':12} {'Mensagem':}")
    print("-" * 80)

    for alerta in fila:
        print(
            f"{alerta['ordem_chegada']:<8} "
            f"{alerta['prioridade']:12} "
            f"{alerta['mensagem']}"
        )

# Criar pilha de eventos críticos
def criar_pilha_eventos_criticos(eventos_criticos):
    pilha = []

    for evento in eventos_criticos:
        pilha.append(evento)

    return pilha 

# Exibir pilha de eventos críticos estruturado 
def exibir_pilha_eventos_criticos_estruturada(eventos_criticos):
    pilha = criar_pilha_eventos_criticos(eventos_criticos)

    print("\nPILHA DE EVENTOS CRÍTICOS ESTRUTURADA")
    print("-" * 80) 

    if len(pilha) == 0:
        print("Nenhum evento crítico registrado.")
        return 

    print("Exibindo do topo da pilha para a base:")
    print("-" * 80)

    posicao = 1

    while len(pilha) > 0:
        evento_topo = pilha.pop() 
        print(f"{posicao}. {evento_topo}")
        posicao += 1

# Exibir hierarquia da missão 
def exibir_hierarquia_missao(hierarquia):
    print("\nHIERARQUIA DA MISSÃO")
    print("-" * 70)

    for sistema, subsistemas in hierarquia.items():
        print(f"{sistema.upper()}")

        for subsistema, descricao in subsistemas.items(): 
            print(f"  |__{subsistema}: {descricao}")

# Exibir resumo das estruturas de dados usadas 
def exibir_resumo_estruturas(cenario):
    print("\nRESUMO DAS ESTRUTURAS DE DADOS USADAS")
    print("-" * 80)

    print("1 - Lista:") 
    print("    Usada em hist[oricos de reserva, consumo, temperatura, logs, alertas.")

    print("\n2 - Dicionário:")
    print("    Usado para organizar cen[ario, módulos, energia, ambiente, limites.")

    print("\n3 - Matriz:")
    print("   Usada em leituras por horário, representada como lista de listas.")

    print("\n4 - Fila:")
    print("    Usada para organizar alertas pendentes por ordem de chegada.")

    print("\n5 - Pilha:")
    print("    Usada para registrar eventos críticos recentes.")

    print("\n6 - Vetor:")
    print("    Usado para organizar valores principais de energia em sequência.")

    print("\n7 - Hierarquia:")
    print("    Usada para representar sistemas e subsistemas da missão.")

    print("\n8 - Tabela de Status:")
    print("    Usada para transformar valores binários 0/1 em informação legível.")

    print("\nRESUMO DO CENÁRIO ATUAL")
    print(f"   Nome do Cenário: {cenario['nome']}")
    print(f"   Quantidade de Módulos Monitorados: {len(cenario['modulos'])}")
    print(f"   Quantidade de Leituras na Matriz: {len(cenario['leituras'])}") 
    print(f"   Quantidade de Eventos no Log: {len(cenario['log_eventos'])}") 
    print(f"   Quantidade de Alertas Pendentes: {len(cenario['alertas_pendentes'])}")
    print(f"   Quantidade de Eventos Críticos: {len(cenario['eventos_criticos'])}") 

# Avaliando condições lógicas do cenário
def avaliar_condicoes_logicas(cenario): 
    modulos = cenario["modulos"]
    energia = cenario["energia"]
    ambiente = cenario["ambiente"]

    # Dados principais de energia 
    reserva = energia["reserva_percentual"]
    consumo = energia["consumo_kwh"]
    geracao_solar = energia["geracao_solar_kwh"]
    geracao_auxiliar = energia["geracao_auxiliar_kwh"]
    geracao_total = geracao_solar + geracao_auxiliar

    # Dados Principais do Ambiente 
    temperatura = ambiente["temperatura_interna"]
    radiacao = ambiente["radiacao"]
    qualidade_comunicacao = ambiente["qualidade_comunicacao"]
    integridade_sensores = ambiente["integridade_sensores"]

    # Dados Essenciais dos Módulos 
    suporte_vida_funcionando = modulos.get("suporte_vida", 0) == 1
    energia_funcionando = modulos.get("energia", 0) == 1
    comunicacao_funcionando = modulos.get("comunicacao", 0) == 1
    habitat_funcionando = modulos.get("habitat", 0) == 1

    # Utilizando operador "not", se o suporte_vida for False, então falha_suporte_vida será True.
    falha_suporte_vida = not suporte_vida_funcionando
    falha_energia = not energia_funcionando
    falha_comunicacao_modulo = not comunicacao_funcionando
    falha_habitat = not habitat_funcionando

    # Verificando módulos essenciais 
    modulos_essenciais = ["suporte_vida", "energia", "comunicacao", "habitat"]
    falhas_essenciais = []

    for modulo in modulos_essenciais:
        if modulos.get(modulo, 0) == 0:
            falhas_essenciais.append(modulo)

    falha_modulo_essencial = len(falhas_essenciais) > 0
    duas_ou_mais_falhas_essenciais = len(falhas_essenciais) >= 2

    # Criando regras de nergia
    energia_baixa = reserva < limites_seguranca["energia_minima_alerta"]
    energia_critica = reserva <= limites_seguranca["energia_minima_critica"]

    consumo_maior_que_geracao = consumo > geracao_total
    consumo_alto = consumo >= limites_seguranca["consumo_alto"]

    # Criando regras de comunicação
    comunicacao_baixa = qualidade_comunicacao < limites_seguranca["qualidade_comunicacao_minima"]

    # Utilizando operador or para saber se a comunicação foi comprometida com a falha do módulo ou se
    # a qualidade do sinal está baixa. 
    comunicacao_comprometida = falha_comunicacao_modulo or comunicacao_baixa

    # Criando regras ambientais 
    radiacao_alta = radiacao == "alta"

    temperatura_abaixo_limite = temperatura < limites_seguranca["temperatura_interna_minima"]
    temperatura_acima_limite = temperatura > limites_seguranca["temperatura_interna_maxima"]
    temperatura_fora_faixa = temperatura_abaixo_limite or temperatura_acima_limite

    temperatura_critica = temperatura >= limites_seguranca["temperatura_interna_critica"]

    # Criando regras de sensores e inconsistência
    sensores_instaveis = integridade_sensores < 60 
    inconsistencia_marcada = cenario.get("inconsistencia_proposital", False) 

    inconsistencia_energia = (
        energia_funcionando
        and geracao_total == 0
        and reserva < limites_seguranca["energia_minima_alerta"]
    )

    dados_inconsistentes = inconsistencia_marcada or inconsistencia_energia or sensores_instaveis

    # Verificação de estabilidade geral da nave - utilizando o operar not para verificar se a missão 
    # está estável. A missão só será considerada estável se NÃO houver: 
    missao_estavel = not (
        energia_baixa
        or comunicacao_comprometida
        or radiacao_alta
        or temperatura_fora_faixa
        or sensores_instaveis
        or falha_modulo_essencial
    )

    condicoes = {
        "reserva": reserva,
        "consumo": consumo, 
        "geracao_total": geracao_total,
        "temperatura": temperatura, 
        "radiacao": radiacao,
        "qualidade_comunicacao": qualidade_comunicacao, 
        "integridade_sensores": integridade_sensores,
        "energia_baixa": energia_baixa, 
        "energia_critica": energia_critica, 
        "consumo_maior_que_geracao": consumo_maior_que_geracao, 
        "consumo_alto": consumo_alto, 
        "falha_suporte_vida": falha_suporte_vida, 
        "falha_energia": falha_energia, 
        "falha_comunicacao_modulo": falha_comunicacao_modulo, 
        "falha_habitat": falha_habitat, 
        "falha_modulo_essencial": falha_modulo_essencial, 
        "falhas_essenciais": falhas_essenciais, 
        "duas_ou_mais_falhas_essenciais": duas_ou_mais_falhas_essenciais,
        "comunicacao_baixa": comunicacao_baixa, 
        "comunicacao_comprometida": comunicacao_comprometida, 
        "radiacao_alta": radiacao_alta, 
        "temperatura_fora_faixa": temperatura_fora_faixa, 
        "temperatura_critica": temperatura_critica, 
        "sensores_instaveis": sensores_instaveis, 
        "dados_inconsistentes": dados_inconsistentes, 
        "missao_estavel": missao_estavel
    }
    
    return condicoes

# Gerando motivos do diagnóstico
def gerar_motivos_diagnostico(condicoes):
    motivos = [] 

    if condicoes["falha_suporte_vida"]:
        motivos.append("Falha no suporte à vida detectado.")

    if condicoes["energia_critica"]:
        motivos.append("Reserva energética em nível crítico.")
    elif condicoes["energia_baixa"]:
        motivos.append("Reserva energética abaixo do limite de alerta.")

    if condicoes["consumo_maior_que_geracao"]:
        motivos.append("Consumo maior que a geração total de energia.")

    if condicoes["consumo_alto"]:
        motivos.append("Consumo energético elevado.")

    if condicoes["falha_comunicacao_modulo"]:
        motivos.append("Módulo de comunicação apresenta falha.")
    elif condicoes["comunicacao_baixa"]:
        motivos.append("Qualidade da comunicação abaixo do limite seguro.")
        
    if condicoes["radiacao_alta"]: 
        motivos.append("Radiação elevada detectada.")

    if condicoes["temperatura_critica"]:
        motivos.append("Temperatura interna fora da faixa segura.")
    elif condicoes["temperatura_fora_faixa"]:
        motivos.append("Temperatura interna fora da faixa segura.")

    if condicoes["falha_habitat"]:
        motivos.append("Módulo de habitat apresenta falha.")

    if condicoes["duas_ou_mais_falhas_essenciais"]:
        motivos.append("Duas ou mais falhas em módulos essenciais.")

    if condicoes["sensores_instaveis"]: 
        motivos.append("Integridade dos sensores abaixo do limite confiável.")

    if condicoes["dados_inconsistentes"]:
        motivos.append("Dados inconsistentes ou conflitantes foram identificados.")

    if condicoes["missao_estavel"]: 
        motivos.append("Todos os principais parâmetros estão dentro da faixa segura.")

    return motivos

# Gerando recomendação com base no diagnóstico

def gerar_recomendacoes_diagnostico(condicoes, status): 
    recomendacoes = [] 

    if status == "NORMAL": 
        recomendacoes.append("Manter operação normal e continuar monitoramento periódico.")

    if condicoes["falha_suporte_vida"]: 
        recomendacoes.append("Ativar imediatamente o sistema auxiliar de suporte à vida.")

    if condicoes["energia_critica"]: 
        recomendacoes.append("Reduzir consumo até que geração volte a superar o gasto energético.")
    elif condicoes["energia_baixa"]: 
        recomendacoes.append("Ativar modo economia e reduzir consumo do laboratório.")

    if condicoes["consumo_maior_que_geracao"]: 
        recomendacoes.append("Reduzir consumo até que a geração volte a superar o gasto energético.")

    if condicoes["falha_comunicacao_modulo"] or condicoes["comunicacao_baixa"]: 
        recomendacoes.append("Ativar canal de comunicação de emergência e reiniciar antena principal.")

    if condicoes["radiacao_alta"]: 
        recomendacoes.append("Suspender atividades externas e reforçar proteção dos equipamentos sensíveis.")

    if condicoes["temperatura_critica"]: 
        recomendacoes.append("Adicionar protocolo térmico de emergência e reduzir atividades que geram calor.")
    elif condicoes["temperatura_fora_faixa"]: 
        recomendacoes.append("Verificar sistema de controle térmico do habitat.")

    if condicoes["sensores_instaveis"] or condicoes["dados_inconsistentes"]: 
        recomendacoes.append("Validar leituras dos sensores antes de tomar decisões definitivas.")

    if condicoes["duas_ou_mais_falhas_essenciais"]: 
        recomendacoes.append("Priorizar recuperação dos módulos essenciais antes de retomar operações secundárias.")

    # Evita recomendações repetitdas
    recomendacoes_sem_repeticao = [] 

    for recomendacao in recomendacoes:
        if recomendacao not in recomendacoes_sem_repeticao:
            recomendacoes_sem_repeticao.append(recomendacao)

    return recomendacoes_sem_repeticao

# Diagnosticar missão 
def diagnosticar_missao(cenario):
    condicoes = avaliar_condicoes_logicas(cenario)

    # Expressão booleana principal para o diagnóstico da condição 
    critico = (
        condicoes["falha_suporte_vida"]
        or condicoes["energia_critica"]
        or condicoes["temperatura_critica"]
        or (condicoes["energia_baixa"] and condicoes["consumo_maior_que_geracao"])
        or (condicoes["falha_comunicacao_modulo"] and condicoes["radiacao_alta"])
        or condicoes["duas_ou_mais_falhas_essenciais"]
    )

    # Expressão booleana para alertas quando existe algum risco relevante 
    alerta = (
        condicoes["energia_baixa"]
        or condicoes["consumo_maior_que_geracao"]
        or condicoes["consumo_alto"]
        or condicoes["comunicacao_comprometida"]
        or condicoes["radiacao_alta"]
        or condicoes["temperatura_fora_faixa"]
        or condicoes["sensores_instaveis"]
        or condicoes["dados_inconsistentes"]
        or condicoes["falha_modulo_essencial"]
    )

    if critico:
        status = "CRÍTICO"
        nivel = 3
    elif alerta:
        status = "ALERTA"
        nivel = 2
    else:
        status = "NORMAL"
        nivel = 1

    motivos = gerar_motivos_diagnostico(condicoes)
    recomendacoes = gerar_recomendacoes_diagnostico(condicoes, status)

    diagnostico = {
        "status": status,
        "nivel": nivel,
        "condicoes": condicoes, 
        "motivos": motivos,
        "recomendacoes": recomendacoes
    }
    
    return diagnostico

# Exibindo condições lógicas usadas no diagnóstico 
def exibir_condicoes_logicas(condicoes): 
    print("\nCONDIÇÕES LÓGICAS AVALIADAS")
    print("-" * 80)

    print(f"Energia Baixa:                     {condicoes["energia_baixa"]}")
    print(f"Energia Crítica                    {condicoes["energia_critica"]}")
    print(f"Consumo Maior que Geração:         {condicoes["consumo_maior_que_geracao"]}") 
    print(f"Falha no Suporte à Vida:           {condicoes["falha_suporte_vida"]}") 
    print(f"Comunicação Comprometida:          {condicoes["comunicacao_comprometida"]}") 
    print(f"Radiação Alta:                     {condicoes["radiacao_alta"]}") 
    print(f"Temperatura Fora da Faixa:         {condicoes["temperatura_fora_faixa"]}") 
    print(f"Temperatura Crítica:               {condicoes["temperatura_critica"]}") 
    print(f"Sensores Instáveis:                {condicoes["sensores_instaveis"]}") 
    print(f"Dados Inconsistentes:              {condicoes["dados_inconsistentes"]}")
    print(f"Missão Estável:                    {condicoes["missao_estavel"]}")

    print("\nVALORES PRINCIPAIS USADOS:")
    print(f"Reserva Energética:                {condicoes["reserva"]}%") 
    print(f"Consumo:                           {condicoes["consumo"]} kWh") 
    print(f"Geração Total:                     {condicoes["geracao_total"]} kWh") 
    print(f"Temperatura Interna:               {condicoes["temperatura"]} °C") 
    print(f"Qualidade da Comunicação:          {condicoes["qualidade_comunicacao"]}%") 
    print(f"Integridade dos Sensores:          {condicoes["integridade_sensores"]}%") 

# Exibindo função booleana principal
def exibir_expressao_booleana_principal():
    print("\nEXPRESSÃO BOOLEANA PRINCIPAL DO DIAGNÓSTICO")
    print("CRÍTICO =")
    print("falha_suporte_vida OR energia_critica OR temperatura_critica OR")
    print("(energia_baixa AND consumo_maior_que_geracao) OR")
    print("(comunicacao_falha and radiacao_alta) OR")
    print("duas_ou_mais_falhas_essenciais")

def exibir_diagnostico(diagnostico):
    print("\n" + "=" * 80)
    print("DIAGNÓSTICO AUTOMÁTICO DA MISSÃO")
    print("=" * 80)

    print(f"Status calculado pelo sistema: {diagnostico['status']}")
    print(f"Nível numérico de serveridade: {diagnostico['nivel']}")

    print("\nMOTIVOS DO DISGNÓSTICO")
    print("-" * 80)

    for indice, motivo in enumerate(diagnostico['motivos'], start=1):
        print(f"{indice}. {motivo}")

    print("\nRECOMENDAÇÕES GERADAS PELO SISTEMA")
    print("-" * 80)

    for indice, recomendacao in enumerate(diagnostico['recomendacoes'], start=1):
        print(f"{indice}. {recomendacao}")

    exibir_condicoes_logicas(diagnostico['condicoes'])
    exibir_expressao_booleana_principal()

# Calculando a média de uma lista 
def calcular_media(lista_valores): 
    if len(lista_valores) == 0: 
        raise ValueError("Não é possível calcular média de uma lista vazia.")

    soma = 0

    for valor in lista_valores: 
        soma += valor 

    media = soma / len(lista_valores)

    return media 

def calcular_regressao_linear_simples(historico_reserva): 
    if len(historico_reserva) < 2: 
        raise ValueError("É necessário ter pelo menos 2 valores para fazer previsão.")

    # Criando um ciclo automaticamente 
    # Se existir 6 leituras, os ciclos serão [1, 2, 3, 4, 5, 6]
    ciclos = []

    for i in range(1, len(historico_reserva) + 1): 
        ciclos.append(i)

    x = ciclos
    y = historico_reserva

    media_x = calcular_media(x)
    media_y = calcular_media(y)

    numerador = 0
    denominador = 0

    for i in range(len(x)):
        diferenca_x = x[i] - media_x 
        diferenca_y = y[i] - media_y

        numerador += diferenca_x * diferenca_y
        denominador += diferenca_x ** 2

    if denominador == 0: 
        raise ValueError("Não foi possível calcular a regressão linear.")

    inclinacao = numerador / denominador
    intercepto = media_y - inclinacao * media_x

    proximo_ciclo = len(historico_reserva) + 1

    previsao_bruta = inclinacao * proximo_ciclo + intercepto

    # A previsão não deve ficar abaixo de 0 e nem acima de 100 por estarmos trabalhando com energia
    if previsao_bruta < 0: 
        previsao_ajustada = 0
    elif previsao_bruta > 100: 
        previsao_ajustada = 100
    else:
        previsao_ajustada = previsao_bruta

    resultado = {
        "ciclos": ciclos, 
        "historico_reserva": historico_reserva, 
        "media_x": media_x, 
        "media_y": media_y, 
        "inclinacao": inclinacao, 
        "intercepto": intercepto, 
        "proximo_ciclo": proximo_ciclo,
        "previsao_bruta": previsao_bruta, 
        "previsao_ajustada": previsao_ajustada
    }

    return resultado

def interpretar_tendencia(inclinacao): 
    if inclinacao < -0.1: 
        return "queda"
    elif inclinacao > 0.1: 
        return "aumento"
    else: 
        return "estabilidade"
    
# Gerando recomendação preditiva 
def gerar_recomendacao_preditiva(previsao, tendencia):
    limite_critico = limites_seguranca["energia_minima_critica"]
    limite_alerta = limites_seguranca["energia_minima_alerta"]

    if previsao <= limite_critico: 
        status_previsao = "RISCO CRÍTICO"
        recomendacao = (
            "A previsão indica que a reserva pode atingir nível crítico. "
            "Ativar modo de emergência, desligar sistemas não essenciais "
            "e preservar energia de suporte à vida e habitat."
        )
    elif previsao < limite_alerta: 
        status_previsao = "RISCO DE ALERTA"
        recomendacao = (
            "A previsão indica reserva abaixo do limite de alerta. "
            "Ativar modo economia e reduzir consumo do laboratório, "
            "navegação secundária e sistemas não essenciais."
        )
    elif tendencia == "queda": 
        status_previsao = "ATENÇÃO PREVENTIVA"
        recomendacao = (
            "A reserva prevista ainda está segura, mas apresenta tendência de queda. "
            "Manter monitoramento e preparar economia preventiva."
        )
    else: 
        status_previsao = "PREVISÃO NORMAL"
        recomendacao = (
            "A previsão indica reserva energética dentro da faixa segura. "
            "Manter operação normal e continuar monitoramento."
        )

    resultado = {
        "status_previsao": status_previsao, 
        "recomendacao": recomendacao
    }

    return resultado

# Prevendo reserva energética do próximo ciclo 
def prever_reserva_energia(cenario): 
    historico_reserva = cenario["historico_reserva"]

    resultado_regressao = calcular_regressao_linear_simples(historico_reserva)

    tendencia = interpretar_tendencia(resultado_regressao["inclinacao"])

    recomendacao_preditiva = gerar_recomendacao_preditiva(
        resultado_regressao["previsao_ajustada"],
        tendencia
    )

    resultado_previsao = {
        "historico_reserva": historico_reserva,
        "ciclos": resultado_regressao["ciclos"], 
        "media_x": resultado_regressao["media_x"], 
        "media_y": resultado_regressao["media_y"], 
        "inclinacao": resultado_regressao["inclinacao"], 
        "intercepto": resultado_regressao["intercepto"], 
        "proximo_ciclo": resultado_regressao["proximo_ciclo"], 
        "previsao_bruta": resultado_regressao["previsao_bruta"], 
        "previsao_ajustada": resultado_regressao["previsao_ajustada"], 
        "tendencia": tendencia, 
        "status_previsao": recomendacao_preditiva["status_previsao"],
        "recomendacao": recomendacao_preditiva["recomendacao"]
    }

    return resultado_previsao

# Exibindo previsão de dados
def exibir_previsao_dados(cenario): 
    print("\n" + "=" * 80)
    print("PREVISÃO DE DADOS - RESERVA ENERGÉTICA")
    print("=" * 80)

    try: 
        previsao = prever_reserva_energia(cenario) 

        print(f"Dados Usados na Previsão:          {previsao['historico_reserva']}")
        print(f"Ciclos Analisados:                 {previsao['ciclos']}")
        print(f"Média dos Ciclos:                  {previsao['media_x']:.2f}")
        print(f"Média da Reserva Energética:       {previsao['media_y']:.2f}%")

        print("\nREGRESSÃO LINEAR SIMPLES")
        print("-" * 80) 
        print(f"Inclinação da Reta:                {previsao['inclinacao']:.2f}")
        print(f"Intercepto:                        {previsao['intercepto']:.2f}")

        print(
            "Equação Estimada:              "
            f"reserva = {previsao['inclinacao']:.2f} * ciclo + {previsao['intercepto']:.2f}"            
        )

        print("\nRESULTADO DA PREVISÃO")
        print("-" * 80) 
        print(f"Próximo Ciclo Previsto:            {previsao['proximo_ciclo']}")
        print(f"Previsão Bruta:                    {previsao['previsao_bruta']:.2f}%")
        print(f"Previsão Ajustada:                 {previsao['previsao_ajustada']:.2f}%")
        print(f"Tendência Identificada:            {previsao['tendencia']}")
        print(f"Status da Previsão:                {previsao['status_previsao']}")

        print("\nRECOMENDAÇÃO PREDITIVA")
        print("-" * 80) 
        print(previsao["recomendacao"])

    except ValueError as erro:
        print("Não foi possível realizar a previsão.")
        print(f"Motivo: {erro}")

    except Exception as erro:
        print("Ocorreu um erro inesperado na previsão.")
        print(f"Detalhes técnicos: {erro}")

# Função principal para exibir um cenário completo - 2
def exibir_cenario(cenario):
    print("\n" + "#" * 80)
    print(f"CENÁRIO SELECIONADO: {cenario['nome']}")
    print("#" * 80) 

    print(f"\nDescrição: {cenario['descricao']}")
    print(f"Classificação Esperada: {cenario['classificacao_esperada']}")

    if cenario["inconsistencia_proposital"]:
        print("\nObservação: este cenário possui inconsistência proposital nos dados.")

    # Tabela de status usando valores binários 0/1
    exibir_tabela_status_modulos(cenario["modulos"])

    # Busca rápida em dicionário
    exibir_busca_modulos_essenciais(cenario["modulos"])

    # Dados energéticos 
    exibir_energia(cenario["energia"])

    # Vetor de energia 
    exibir_vetor_energia(cenario["energia"])

    # Dados ambientais 
    exibir_ambiente(cenario["ambiente"])

    # Listas Históricas 
    exibir_historico(cenario)
    exibir_resumo_listas(cenario) 

    # Matriz de Leituras 
    exibir_matriz_leituras(cenario["leituras"])
    exibir_resumo_matriz(cenario["leituras"])

    # Log de Eventos 
    exibir_log_eventos(cenario["log_eventos"])

    # Fila de alertas estruturada 
    exibir_fila_alertas_estruturada(cenario["alertas_pendentes"])

    # Pilha de eventos críticos estruturada 
    exibir_pilha_eventos_criticos_estruturada(cenario["eventos_criticos"])

    # Hierarquia da Missão
    exibir_hierarquia_missao(hierarquia_missao)

    # Resumo final das Estruturas de Dados 
    #exibir_resumo_estruturas(cenario)

    print("\nRECOMENDAÇÃO INICIAL")
    print("-" * 80) 
    print(cenario["recomendacao_inicial"])

    # Inclusão do diagnóstico lógico 
    diagnostico = diagnosticar_missao(cenario) 
    exibir_diagnostico(diagnostico)

    # Exibindo a previsão de dados 
    exibir_previsao_dados(cenario)

# Função principal do sistema
def main():
    try:
        dados_telemetria = ler_telemetria_csv(caminho_telemetria)
    
    except FileNotFoundError:
        print("\nErro: arquivo telemtria.csv não encontrado.")
        print("Verifique se o arquivo está dentro da pasta data/")
        return 
    
    except Exception as erro:
        print("\nErro ao ler o arquivo de telemetria.")
        print(f"Detalhes técnicos: {erro}")
        return

    while True:
        exibir_menu()

        escolha = input("Digite o número do cenário desejado: ").strip().lower()

        if escolha == "sair":
            print("\nSistema encerrado com segurança.")
            break

        try:
            if escolha not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
                raise ValueError("Opção inválida. Escolha um número de 1 a 10 ou digite 'sair'.")

            linhas_cenario = filtrar_telemetria_por_cenario(dados_telemetria, escolha)
            cenario_escolhido = montar_cenario_a_partir_csv(linhas_cenario)

            exibir_cenario(cenario_escolhido)

            input("\nPressione ENTER para voltar ao menu...")

        except ValueError as erro:
            print(f"\nErro: {erro}")

        except Exception as erro:
            print("\nOcorreu um erro inesperado no sistema.")
            print(f"Detalhes técnicos: {erro}")

## Função execução do programa 
# Essa condição verifica se o arquivo sistema.py está sendo executado diretamente.
# Se estiver, o Python chama a função main(), que inicia o menu do sistema.
# Isso evita que o programa rode automaticamente caso este arquivo seja importado por outro arquivo.

if __name__ == "__main__":
    main()