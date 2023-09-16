dias_semana=("Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo")

"""
print(dias_semana[0])
print(dias_semana[1])
print(dias_semana[2])
print(dias_semana[3])
print(dias_semana[4])
print(dias_semana[5])
print(dias_semana[6])

print(dias_semana[:7])
print(dias_semana[2:4])
print(dias_semana[-1:])
print(dias_semana[:-1])

"""
# Para recorrer tuplas se usa for

for i in range(len(dias_semana)):
    print(dias_semana[i])
    
# Para cambiar algun valor de la tupla o añadir debemos primero convertir a lista

dias_semana_lista = list(dias_semana)

print(type(dias_semana_lista))

dias_semana_lista.append("Festivo") #Anadir en la ultima posicion

print(dias_semana_lista[:8])

dias_semana_lista.pop()

print(dias_semana_lista[:8])

dias_semana_lista = tuple(dias_semana)

print(type(dias_semana))