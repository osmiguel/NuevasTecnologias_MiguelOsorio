# Los conjuntos son inmutables
# Son desordenados, quiere decir que cuando se llama no se tiene certeza el orden que los mostrara
# no son indexados
# no permite duplicados

vocales = {"a", "e", "i", "o", "u"}

print(len(vocales))

print(type(vocales))

# Para recorrer usar in

print("Cunjunto 1")

for i in vocales:
    print(vocales)
    
vocales.add("@")

for i in vocales:
    print(vocales)
    
vocales.pop()

for i in vocales:
    print(vocales)
    