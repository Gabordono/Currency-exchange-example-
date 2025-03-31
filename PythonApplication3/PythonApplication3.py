peso = float(input("How many pesos are left?"))
sol = float(input("How many sol are left?"))
reais = float(input("How many reais are left?"))

usd = (peso * 0.050) + (sol * 0.28) + (reais * 0.17)
print(usd)
