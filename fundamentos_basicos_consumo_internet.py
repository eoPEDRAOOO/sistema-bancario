10
def recomendar_plano(consumo_mensal):
    if consumo_mensal <= 10.0:
        return "Plano Essencial Fibra - 50Mbps"
    elif consumo_mensal > 10.0 and consumo_mensal <= 20.0:
        return "Plano Prata Fibra - 100Mbps"
    elif consumo_mensal > 20.0:
        return "Plano Premium Fibra - 300Mbps"
    else:
        pass


consumo_mensal = float(input())
print(recomendar_plano(consumo_mensal))


