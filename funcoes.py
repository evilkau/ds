custo = [500, 180, 305, 450]
ganhos = [3000, 650, 2000]


def somatorio_while(lista):
    contador = 0
    soma = 0
    while contador < len(lista):
        soma = soma+lista[contador]
        contador=contador+ 1
    return soma


diferenca = somatorio_while(ganhos) - somatorio_while(custo)

print(f"Custos: R${somatorio_while(custo)}")
print(f"Ganhos: R${somatorio_while(ganhos)}")
print(f"Diferença: R${diferenca}")
