def changeme(lista):
    lista = [2, 3, 4]
    print("Wewnątrz funkcji: ", lista)
    return


lista = [10, 20, 30]
changeme(lista)
## Wewnątrz funkcji:  [2, 3, 4]
print("Poza funkcją: ", lista)
## Poza funkcją:  [10, 20, 30]
