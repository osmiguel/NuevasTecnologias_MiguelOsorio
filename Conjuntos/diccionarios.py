usuario = {
    "nombre":"Miguel",
    "apellido":"Osorio",
    "edad":"20"
}

print(usuario)

print(usuario.keys())

print(usuario.values())

# Buscar item especifico
print(usuario.get("nombre"))

# Agregar datos
usuario["correo"]= "correo@correo.com"

print(usuario.keys())
print(usuario.get("correo"))

# Actualizar

usuario.update({"correo":"miguel@correo.com"})

print(usuario)

# Remover
"""
usuario.pop("nombre")
print(usuario.keys())
usuario.popitem()
print(usuario.keys())
"""
#recorrer diccionario
# con for

for x,y in usuario.items():
    print(x + ": ",y)
    
# Recorrer claves

for x in usuario.keys():
    print(x)

for y in usuario.values():
    print(y)
