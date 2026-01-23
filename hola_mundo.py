# mi_primer_script.py
print("¡Hola, GitHub!")

primos = []

for numero in range(1, 1001):
    if numero > 1:
        es_primo = True

        for i in range(2, numero):
            if numero % i == 0:
                es_primo = False
                break

        if es_primo:
            primos.append(numero)

print("Números primos entre 1 y 1000:")
print(primos)
