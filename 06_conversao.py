#entrada de dados
nome = input("informe o nome:" )
idade = input("informe sua idade:")
altura=input("altura:").replace(',','.')

#conversao de tipo
idade = int(idade)
altura = float(altura)

print(f"Nome: {nome} TIPO: {type(nome)}")
print(f"idade:{idade}> Tipo {type(idade)}")
print(f"altura: {altura}. Tipo : {type(idade)}")
