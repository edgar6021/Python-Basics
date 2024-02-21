#Edgar De la rosa como saber si un año es bisieto o comun#

year = int (input ("Introduce un año"))

if year < 1582:
    print ("No esta dentro del periodo del calendario Gregoriano")
else:
    if year % 4 !=0:
        print("año comun") 
    elif year % 100 != 0:
        print ("año Bisieto")
    elif year % 400 != 0:
        print("año comun")
    else:
        print("año bisieto")               
    