#B_Mostrar la cantidad de números positivos y negativos.
def mostrar_positivo_negativos(lista: list)->int:
    """
    Muestra la cantidad de números positivos y negativos en una lista.

    Args:
        lista_numeros (list): Lista de números enteros.

    Returns:
        tuple: Cantidad de números positivos y negativos.
    """
    contador_positivos = 0
    contador_negativos = 0
    
   
    for i in lista:
        if i >= 0:
            contador_positivos += 1
        else:
            contador_negativos += 1
    
    return contador_positivos, contador_negativos


#C_Mostrar la sumatoria de los números pares.
def sumar_pares(lista:list)->int:
    """suma pares

    Args:
        lista (list): paso lista

    Returns:
        int: devuelve suma
    """
    sumar = 0
    
    for i in lista:
        if i % 2 == 0:
            sumar += i
            
    return sumar