a=float(input('What do you have left in pesos? '))
b=float(input('What do you have left in soles? '))
c=float(input('What do you have left in reals? '))

Peso = float(0.00025)
Sol = float(0.28)
Real = float(0.18)

nPeso = (a* Peso)
nSol = (b * Sol)
nReal = (c * Real)

USD = ((nPeso) + (nSol) + (nReal))

print (USD)