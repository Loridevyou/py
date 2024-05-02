#questo algoritmo genera un numero primo di Mersenne


p = int(input("Inserisci un numero primo: "))
count = 0

for i in range(2 ,round(p**0.5)+1):
    if p % i == 0 and p != i:
        count += 1
if count > 0:
    print("Il numero inserito non è primo")
else:
    m = 2**p - 1
    print("Il numero di Mersenne di", p, "è:", m)