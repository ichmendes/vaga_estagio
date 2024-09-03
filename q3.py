import json

# Exemplo de dados em JSON (substitua por dados reais)
dados = '''[
    {"dia": 1, "faturamento": 1000.0},
    {"dia": 2, "faturamento": 2000.0},
    {"dia": 3, "faturamento": 1500.0},
    {"dia": 4, "faturamento": 0.0},
    {"dia": 5, "faturamento": 3000.0}
]'''

faturamento = json.loads(dados)
valores = [dia['faturamento'] for dia in faturamento if dia['faturamento'] > 0]
media_mensal = sum(valores) / len(valores)

menor = min(valores)
maior = max(valores)
dias_acima_media = sum(1 for valor in valores if valor > media_mensal)

print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")
print(f"Dias acima da média: {dias_acima_media}")
