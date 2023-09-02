#reciban por consola el valor de una compra 
# ingresar el numero de cuotas
# Calcular el valor de la cuota
# usando while - muestre el plan de pago
# cupo liberado con cada pago ejemplo cuota 1 --- valor resta ----

totalCompra = int(input("Ingrese el valor de la compra: "))
cuotas = int(input("Ingrese el numero de cuotas: "))

cuota = totalCompra / cuotas
cuota_num = 1

while totalCompra > 0:
    print("Cuota", cuota_num, "a pagar:", cuota)
    totalCompra -= cuota
    cuota_num += 1
    print("Restante por pagar:", totalCompra)

print("¡El crédito ha sido cancelado!")


