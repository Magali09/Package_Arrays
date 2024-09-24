def pedir_numero()->list:
    #A_Pedir el ingreso de 10 números enteros entre -1000 y 1000. 
    #E_Listar todos los números ingresados.
    """Pide numero

    Args:
        numero (int): ingresa numero

    Returns:
        int:retorna numero
    
    """
    lista_numeros = []
    respuesta = "si"
    while respuesta == "si" and len(lista_numeros) < 3:
        numero = int(input("Ingrese un numero: "))
        while numero < -1000 or numero >1000:
            numero = int(input("Reingrese un numero entre -1000 y 1000: "))
        lista_numeros.append(numero)
        
        if len(lista_numeros) < 3:
            respuesta = input("Quiere ingresar otro numero: si/no?").lower()
        else:
            respuesta = input("Su lista esta completa!!!!")
    return lista_numeros    
