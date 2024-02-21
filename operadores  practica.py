nombre= (input("Ingresa tu Nombre:"))
monto = float (input("Introduce el ingreso anual"))
cobro= 85,528
impuesto=0.18
descuento=556.2
pagoImpuesto=0

a ='1'
b= "2"
print(a + b)

if monto==cobro:
    pagoImpuesto=monto*impuesto-descuento
    print(nombre,"debe pagar",pagoImpuesto)
if monto >= cobro:
    pagoImpuesto=monto*impuesto-descuento
    print(nombre,"debe pagar",pagoImpuesto)
    
    
    
    

