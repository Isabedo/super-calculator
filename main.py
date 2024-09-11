while True:
    print("oprime 1 para sumar")
    print("oprime 2 para restar")
    print("oprime 3 para multiplicar")
    print("oprime 4 para dividir")
    print("oprime 5 para salir")

    opcion = int(input("ingrese la opcion que desea realizar: "))
    if not opcion:
        print("ingrese una opcion valida")
    elif opcion==5:
     break
    else:
     num1 = int(input("ingrese el primer numero: "))
     num2 = int(input("ingrese el segundo numero: "))
    if opcion==1:
        suma=num1+num2
        print("la suma es: ", suma)
    elif opcion ==2:
        resta=num1-num2
        print("la resta es: ", resta)
    elif opcion == 3:
        multi=num1*num2
        print("la multiplicacion es: ", multi)
    elif opcion == 4:
        divi=num1/num2
        print("la division es: ", divi)
