# GS2-CTFE

Simulação de monitoramento ambiental de uma sala de aula. O programa lê temperatura, luminosidade e ruído, compara cada valor com limites de referência e gera um relatório de conforto.

## Como executar

Requer Python 3.

```bash
python Untitled-1.py
```

O programa pede quantas leituras serão feitas e, para cada uma, os três valores. Aceita vírgula ou ponto como separador decimal. Ao final, pergunta se deve iniciar uma nova sequência (`s` ou `n`).

## Limites adotados

| Parâmetro | Faixa | Referência |
| --- | --- | --- |
| Temperatura | 18 a 25 °C | NR-17 (2021), item 17.8.4.2 |
| Luminosidade | 300 a 500 lux | NBR ISO 8995-1:2013 (mínimo de 300 lux); teto de 500 lux definido pelo grupo |
| Ruído | máximo 35 dB | NBR 10152:2017, Tabela 3 |

Um valor fora da faixa gera um alerta na hora e conta como ocorrência crítica daquele parâmetro. Uma leitura é crítica se pelo menos um parâmetro estiver fora da faixa.

## Relatório

Depois de cada sequência, o programa mostra e grava `relatorio_ambiental.txt` com:

- ambiente e quantidade de leituras
- limites usados
- média, maior e menor valor de cada parâmetro
- ocorrências críticas por parâmetro
- percentual de leituras críticas
- classificação geral

A média de ruído é a média aritmética simples dos valores em dB. Ela não representa o nível sonoro equivalente.

Se mais de 30% das leituras forem críticas, o estado geral é de atenção. Caso contrário, a frequência fica dentro do critério da simulação.

O resultado é uma simulação com os critérios acima. Não certifica acessibilidade e não substitui avaliação técnica do espaço.
