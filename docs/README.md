# Sistema Inteligente de Monitoramento Espacial - Aurora Siger - Global Solution 2026

## Nome da Equipe e RM dos Integrantes

**Equipe:** ChronoCodex

```
Nome: Renato Lima do Nascimento     - RM:570266
Nome: Renato Levy do Valle          - RM:572352 
Nome: Alexandre Martins Niewelt     - RM:570614
```

--- 

## Resumo do Problema e Cenário Analisado

Esse projeto tem como objetivo desenvolver um sistema inteligente de monitoramento para uma missão espacial experimental chamada **Aurora Siger**.

A proposta simula uma central de controle capaz de receber, organizar, interpretar e exibir dados de telemetria relacionados à operação espacial. O sistema analisa informações sobre energia, comunicação, suporte à vida, habitat, temperatura, radiação, sensores e eventos críticos.

O problema analisado envolve a necessidade de tomar decisões em ambientes extremos, como missões espaciais, onde a comunicação pode ser limitada e os dados dos sensores se tornam a principal fonte de informação para manter a segurança da operação.

O sistema foi desenvolvido para funcionar no terminal, permitindo que o usuário escolah entre **10 cenários simulados**: 

1. Cenário Normal;
2. Cenário de Energia Baixa;
3. Cenário de Falha na Comunicação;
4. Cenário de Radiação Elevada;
5. Cenário Crítico Geral;
6. Cenário de Falha no Suporte à Vida;
7. Cenário de Superaquecimento Interno;
8. Cenário de Baixa Geração Solar por Tempestade de Poeira;
9. Cenário de Inconsistência nos Sensores;
10. Cenário de Modo Economia Preventivo.

Cada cenário possui dados de telemetria armazenados em um arquivo CSV, permitindo que o sistema leia dados externos, interprete a situação da missão e gere diagnósticos automáticos.

--- 

## Estruturas de Dados

O projeto utiliza diferentes estruturas de dados estudadas ao longo das fases do curso.

### Listas 

As listas foram usadas para armazenar valores históricos da missão, como: 

* histórico de reserva energética;
* histórico de consumo;
* histórico de temperatura;
* log de eventos;
* alertas pendentes;
* eventos críticos.

As listas são importantes porque permitem armazenar vários valores em sequência e analisar a evolução dos dados ao longo do tempo.

Exemplo de uso: 

```python
historico_reserva = [52, 47, 43, 39, 36, 34]
```

--- 

### Dicionários 

Os dicionários foram usados para organizar informações com chave e valor, facilitando o acesso aos dados pelo nome.

Eles aparecem em estruturas como: 

* dados do cenário;
* módulos críticos;
* dados de energia;
* dados ambientais;
* limites de segurança.

Exemplo:

```python
energia = {
    "reserva_percentual": 34, 
    "consumo_kwh": 82, 
    "geracao_solar_kwh": 31, 
    "geracao_auxiliar_kwh": 8
}
```

O uso de dicionários se aproxima do conceito de tabela hash, pois permite acessar rapidamente uma informação por meio de uma chave.

--- 

### Matriz

A matriz foi representada por uma lista de listas. Ela organiza as leituras de telemetria por horário e variável.

Exemplo de uso: 

```python
leituras = [
    ["00h", 42, 65, 52, 24, 85],
    ["04h", 38, 70, 47, 24, 83], 
    ["08h", 35, 74, 43, 25, 82]
]
```

Cada linha representa um horário de leitura. Cada coluna representa uma variável, como geração, consumo, reserva, temperatura e comunicação.

--- 

### Fila

A fila foi usada para representar alertas pendentes.

O conceito de fila segue o princípio **FIFO**

> First In, First Out - o primeiro item que entra é o primeiro a sair.

Esse conceito é útil para visualizar os eventos críticos mais recentes da missão.

--- 

### Hierarquia 

A hierarquia foi usada para representar sistemas e subsistemas da missão, como energia, habitat e segurança.

Exemplo:

```python 
hierarquia_missao = {
    "energia": {
        "solar": "gera energia renovável",
        "baterias": "armazenam energia reserva",
        "consumo": "mede o gasto energético da missão"
    }, 
    "habitat": {
        "oxigenio": "mantém condições de sobrevivência",
        "temperatura": "controla o ambiente interno", 
        "comunicacao": "mantém contato com a base"
    }
}
```

Essa organização se aproxima de uma árvore, pois existe uma estrutura principal dividida em partes menores.

## Regras Lógiccas Principais do Diagnóstico

O sistema utiliza regras lógicas para classificar a missão como:

* **NORMAL**
* **ALERTA**
* **CRÍTICO**

As regras foram construídas com `if`, `elif`, `else` e operadores lógicos como `and`, `or` e `not`. 

Algumas condições avaliadas pelo sistema são: 

```python 
energia_baixa = reserva < 40
energia_critica = reserva <= 25
consumo_maior_que_geracao = consumo > geracao_total 
comunicacao_baixa = qualidade_comunicacao < 50
radiacao_alta = radiacao == "alta"
temperatura_critica = temperatura >= 34
falha_suporte_vida = not suporte_vida_funcionamento
```

A expressão booleana principal do diagnóstico crítico é:

```text
CRÍTICO = 
falha_suporte_vida OR energia_critica OR temperatura_critica OR
(energia_baixa AND consumo_maior_que_geracao) OR
(comunicacao_falha AND radiacao_alta) OR
duas_ou_mais_falhas_essenciais
```

Essa regra indica que a missão entra em estado crítico quando há falha no suporte à vida, energia em nível crítico, temperatura extrema ou combinação perigosa de falhas.

A classificação segue a seguinte ordem: 

```python 
if critico:
    status = "CRÍTICO"
elif alerta: 
    status = "ALERTA"
else:
    status = "NORMAL"
```

Essa ordem é importante porque o sistema precisa priorizar situações graves antes de classificar a missão como alerta ou normal.

--- 

## Técnica de Previsão Utilizada e Resultado

A técnica de previsão utilizada foi **regressão linear simples manual**, sem uso de bibliotecas avançadas como Pandas, NumPy ou Scikit-Learn. 

Essa variável escolhida para previsão foi a **reserva energética**, pois a energia é essencial para manter suporte à vida, comunicação, habitat, sensores e controle térmico. 

A regressão linear usa a equação:

```text 
y = a * x + b 
```

No projeto:

* `x` representa o ciclo de leitura;
* `y` representa a reserva energética;
* `a` representa a inclinação da reta;
* `b` representa o intercepto.

Exemplo de histórico usado: 

```python 
historico_reserva = [52, 47, 43, 39, 36, 34]
```

O sistema usa esse histórico para prever a reserva energética do próximo ciclo.

Além disso, a previsão gera uma recomendação automática: 

* se a previsão for menor ou igual a 25%, o sistema indica risco crítico;
* se a previsão for menor que 40%, o sistema recomenda modo economia;
* se a previsão estiver segura, mas em queda, o sistema recomenda monitoramento preventivo;
* se estiver estável, recomenda manter operação normal.

Dessa forma, o sistema deixa de ser apenas reativo e passa a ter comportamento preditivo.

--- 

## Como Executar o Software
Para executar o projeto, matenha a seguinte estrutura de pastas:

```text 
projeto_missao_espacial 
│
│
├─────src/
│      └─────sistema.py
│
├─────data/
│      └─────dados.csv
│
├─────docs/
│      └─────relatorio.pdf
│      └─────link_video.txt
│
└─────README.md
```

No terminal, execute: 
```bash 
python src/sistema.py
```

Observação: caso o arquivo Python esteja salvo como `sistemas.py`, renomeie para `sistema.py` ou ajuste o comando de execução conforme o nome usado no projeto.

--- 

## Exemplo de Entrada e Saída do Sistema 

Ao executar o programa, o sistema exibe um menu no terminal: 

```text 
Sistema Inteligente de Monitoramento Espacial - Aurora Siger 
============================================================
Escolha um Cenário para Análise:
1  - Cenário Normal
2  - Cenário de Energia Baixa
3  - Cenário de Falha na Comunicação
4  - Cenário de Radiação Elevada 
5  - Cenário Crítico Geral 
6  - Cenário de Falha de Suporte à Vida
7  - Cenário de Superaquecimento Interno
8  - Cenário de Baixa Geração Solar por Tempestade de Poeira 
9  - Cenário de Inconsistência nos Sensores 
10 - Cenário de Modo Economia Preventivo
```
Exemplo de Entrada:

```text 
Digite o número do cenário desejado: 2
```

Exemplo resumido de saída: 
```text 
CENÁRIO SELECIONADO: Cenário de Energia baixa 

Descrição:
A reserva de energia está baixa e o consumo está acima do ideal. 

DADOS DE ENERGIA
Reserva energética: 34% 
Consumo atual: 82 kWh
Geração solar: 31 kWh
Geração auxiliar: 8 kWh

DIAGNÓSTICO AUTOMÁTICO DA MISSÃO
Status calculado pelo sistema: CRÍTICO

MOTIVOS DO DIAGNÓSTICO
1. Reserva energética abaixo do limite de laerta.
2. Consumo maior que a geração total de energia.
3. Consumo energético elevado.

RECOMENDAÇÕES GERADAS PELO SISTEMA
1. Ativar modo economia e reduzir o consumo do laboratório.
2. Reduzir consumo até que a geração volte a superar o gasto energético

PREVISÃO DE DAODS - RESERVA ENERGÉTICA
Dados usados na previsão: [52, 47, 43, 39, 36, 34]
Tendência identificada: queda 
Status da previsão: RISCO DE ALERTA

RECOMENDAÇÃO PREDITIVA
Ativar modo economia e reduzir consumo do laboratório, navegação secundária e sistemas não essenciais.
```

```text 
sair
```

---

## Recomendações Geradas pelo Sistema 

O sistema gera recomendações com base nas condições detectadas.

Exemplos: 

### Energia Baixa ou Crítica 

```text
Ativar modo economia e reduzir consumo do laboratório.
Desligar sistemas não essenciais e preservar energia para suporte à vida e habitat.
```

### Falha no Suporte à Vida 

```text
Ativar imediatamente o sistema auxiliar de suporte à vida.
```

### Comunicação Comprometida 

```text 
Ativar canal de comunicação de emergência e reiniciar antena principal.
```

### Radiação Elevada 

```text 
Suspender atividades externas e reforçar proteção dos equipamentos sensíveis.
```

### Temperatura Fora da Faixa Segura

```text 
Verificar sistema de controle térmico do habitat.
```

### Sensores Instáveis ou Dados Inconsistentes 

```text 
Validar leituras dos sensores antes de tomar deciões definitivas.
```

### Previsão de Queda Energética 

```text 
Ativar modo economia preventiva antes que a reserva energética alcance nível crítico.
```

Essas recomendações fazem com que o sistema não apenas mostre dados, como também apoie a tomada de decisão operacional.

--- 

## Link do Vídeo no YouTube

**Link:** https://youtu.be/bTOoPlSO0zQ

--- 

## Conclusões e Aprendizados 

O projeto da **Global Solution do Sistema Inteligente de Monitoramento Aurora Siger** permitiu desenvolver um sistema de monitoramento espacial aplicando conceitos fundamentais de Ciência da Computação.

Durante esse desenvolvimento, foram utilizados conceitos de programação, estruturas de dados, lógica booleana, leitura de arquivos, análise de dados simples e previsão por regressão linear.

O sistema foi construído de forma progressiva. Primeiro, foram definidos os 10 cenários simulados. Depois, os dados foram organizados em estruturas como listas, dicionários, matriz, fila, pilha e hierarquia. Em seguida, os dados passaram a ser armazenados em um arquivo externo `dados.csv`, tornando o projeto mais próximo de uma aplicação real de telemetria. 

As regras lógicas permitiram classificar a missão como normal, alerta ou crítico. Além disso, a previsão de reserva energética tornou o sistema mais avançado, pois ele passou a antecipar riscos e gerar recomendações preventivas.

O principal aprendizado foi compreender como dados brutos podem ser transformados em informação útil por meio de altoritmos, estrutas de dados, e regras de decisão. O projeto também mostrou a importância da organização dos dados, da clareza nas recomendações e da responsabilidade em sistemas que simulam decisões críticas para segurança humana e operacional.