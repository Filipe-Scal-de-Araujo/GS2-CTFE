# ---------------------------------------------------------------------------
# Integrantes: (nome completo e RM de cada um)
# Ambiente: Sala de aula (leitura, escrita, uso de quadro)
#
# LIMITES DE REFERÊNCIA
# Temperatura (18 a 25 °C): NR-17 (2021), item 17.8.4.2, temperatura do ar
#   para ambientes climatizados com atividade intelectual constante.
# Luminosidade (300 a 500 lux): NBR ISO 8995-1:2013 indica 300 lux no plano de
#   trabalho em salas de aula. O máximo de 500 lux se apoia na faixa citada
#   pela IESNA (2000) e é decisão do grupo, para evitar ofuscamento.
# Ruído (máx. 35 dB): NBR 10152:2017, Tabela 3, valor de referência de
#   35 dB(A) para salas de aula.
# ---------------------------------------------------------------------------

AMBIENTE = "Sala de Aula"
LIMITES_PERCENTUAL = 30
NOME_ARQUIVO = "relatorio_ambiental.txt"

LIMITES = {
    "temperatura": {
        "nome": "Temperatura",
        "unidade": "°C",
        "min": 18,
        "max": 25,
        "mensagem": "A temperatura está fora dos limites recomendados."
    },

    "luminosidade": {
        "nome": "Luminosidade",
        "unidade": "Lux",
        "min": 300,
        "max": 500,
        "mensagem": "A luminosidade está fora dos limites recomendados."
    },
    
    "ruido": {
        "nome": "Ruido",
        "unidade": "dB",
        "min": None,
        "max": 35,
        "mensagem": "O ruído está fora dos limites recomendados."
    },
}

def ler_quantidade():
    while True:
        texto = input("Qauntas leituras você deseja fazer? ").strip()
        if texto.isdigit() and int(texto) > 0:
            return int(texto)
        print("Por favor, digite um número inteiro positivo.")

def ler_numero(mensagem):
    while True:
        try:
            return float(input(mensagem).strip().replace(",", "."))
        except ValueError:
            print("Por favor, digite um número válido.")

# Função Estatística

def calcular_estatisticas(valores):
    media = sum(valores) / len(valores)
    return media, max(valores), min(valores)

# Verificação de Alerta

def verificar_leitura(leitura, ocorrencias):
    alertas = []
    for paremetro, valor in leitura.items():
        lim = LIMITES[paremetro]
        abaixo = lim["min"] is not None and valor < lim["min"]
        acima = valor > lim["max"]
        if abaixo or acima:
            alertas.append(lim["mensagem"])
            ocorrencias[paremetro] += 1
    return alertas

def classifiucar(porcentual):
    if porcentual > LIMITES_PERCENTUAL:
        return ("Estado geral: condições ambientais de atenção, com "
                "frequência de ocorências acima do critério estabelecido.")
    return ("Estado geral: frequêncai de ocorrencia dentro do critério " 
            "estabelecido para a simulação.")

def formatar_faixa(lim):
    if lim["min"] is None:
        return f"máximo {lim['max']} {lim['unidade']}"
    return f"entre {lim['min']} e {lim['max']} {lim['unidade']}"

#Relatorio

def montar_relatorio(leituras, stats, ocorrencias, total_criticas,
                     percentual, classificacao):
    linhas = []
    linhas.append("=" * 60)
    linhas.append("Relatorio de Monitoramento Ambiental (Simulação)")
    linhas.append("=" * 60)
    linhas.append(f"Ambiente: {AMBIENTE}")
    linhas.append(f"Quantidade de leituras: {len(leituras)}")
    linhas.append("")
    linhas.append("Limites de Referencia Adotados")
    for lim in LIMITES.values():
        linhas.append(f"   {lim['nome']}: {formatar_faixa(lim)}")
    linhas.append("")
    linhas.append("Estatisticas")
    for parametro, lin in LIMITES.items():
        media, maior, menor = stats[parametro]
        u = lin["unidade"]
        linhas.append(f"   {lin['nome']}: média = {media:.2f} {u} | "
                      f"maior = {maior:.2f} {u} | menor = {menor:.2f} {u}")
    linhas.append("  (A media de ruido é a media aritmética simples dos "
                  "valores em dB,")
    linhas.append("    estatisticas descritiva simplificada: não represneta "
                  "nivel sonoro equivalente.)")
    linhas.append("")
    linhas.append("Ocorrencias Críticas por Parametro")
    for parametro, lim in LIMITES.items():
        linhas.append(f"   {lim['nome']}: {ocorrencias[parametro]}")
    linhas.append("")
    linhas.append(f"Leituras com pelo menos uma condição crítica: "
                  f"{total_criticas} de {len(leituras)}")
    linhas.append(f"Percentual de leituras criticas: {percentual:.2f}%")
    linhas.append("")
    linhas.append(classificacao)
    linhas.append("")
    linhas.append("OBSERVAÇÃO: este resultado se refere a uma simulação "
                  "baseado nos")
    linhas.append("criterios adotados; não é certificação de acessibilidade "
                  "nem substitui")
    linhas.append("avaliação técnica do espaço.")
    linhas.append("=" * 60)
    return "\n".join(linhas)

def salvar_relatorio(texto):
    with open(NOME_ARQUIVO, "w", encoding="utf-8") as arquivo:
        arquivo.write(texto +"\n")
    print(f"\nRelatorio salvo no arquivo: {NOME_ARQUIVO}")

# Uma Sequencia Completa de Analise

def executar_analise():
    leituras = []
    ocorrencias = {"temperatura": 0, "luminosidade": 0, "ruido": 0}
    total_criticas = 0

    quantidade = ler_quantidade()

    for i in range(1, quantidade + 1):
        print(f"\n--- Leitura {i} de {quantidade} ---")
        leitura = {
            "temperatura": ler_numero(f"Leitura {i} - Temperatura (°C): "),
            "luminosidade": ler_numero(f"Leitura {i} - Luminosidade (lux): "),
            "ruido": ler_numero(f"Leitura {i} - Ruido (dB): ")
        }
        leituras.append(leitura)

        alertas = verificar_leitura(leitura, ocorrencias)
        if alertas:
            for alerta in alertas:
                print("Alerta:", alerta)
            total_criticas += 1
        else:
            print("Leituras dentro dos limites de referência estabelicidas.")
        
    stats = {}
    for parametros in LIMITES:
        valores = [l[parametros] for l in leituras]
        stats[parametros] = calcular_estatisticas(valores)

    percentual = (total_criticas / len(leituras)) * 100
    classifiucacao = classifiucar(percentual)

    relatorio = montar_relatorio(leituras, stats, ocorrencias,
                                 total_criticas, percentual, classifiucacao)
    
    print("\n" + relatorio)
    salvar_relatorio(relatorio)

# Progrma Princimpal

def main():
    print("Monitoramento Ambiental - Conforto e Acessibilidade")
    print(f"Ambiente de referencia: {AMBIENTE}\n")
    print("Limites adotados:")
    for lim in LIMITES.values():
        print(f"  {lim['nome']}: {formatar_faixa(lim)}")
    print()

    while True:
        executar_analise()

        resposta = input("\nDeseja realizar uma nova sequencia? (s/n): ")
        resposta = resposta.strip().lower()
        while resposta not in ("s", "n"):
            resposta = input("Resposta invalido. Digite s ou n: ")
            resposta = resposta.strip().lower()

        if resposta == "n":
            print("Programa encerrado. Obrigado por utilizar!")
            break
        print()
main()