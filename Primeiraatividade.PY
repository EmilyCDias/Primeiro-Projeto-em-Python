# Entradas do usuário
fumo = int(input("Tempo como fumante (em anos)....: "))
Valor = float(input("Valor do maço.....: "))
Quantidade = int(input("Quantidade de maços por dia....: "))

# Cálculo dos gastos
gasto_diario = Valor * Quantidade
gasto_anual = gasto_diario * 365
resultado = gasto_anual * fumo

# Definindo faixas para comparações
FAIXA_1 = 20000
FAIXA_2 = 50000

# Verificando as faixas de valores de maneira mais explícita
if resultado < FAIXA_1:
    print(f"Com o valor R$ {resultado:.2f}, você poderia ter dado entrada em um carro.")

elif FAIXA_1 <= resultado < FAIXA_2:
    print(f"Com o valor R$ {resultado:.2f}, você poderia ter dado entrada em um carro.")

else:
    print(f"Com o valor R$ {resultado:.2f}, você poderia ter dado entrada em um carro.")
