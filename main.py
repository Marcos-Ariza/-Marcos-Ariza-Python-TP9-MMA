def busqueda_lineal(lista, elemento):
    
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

def busqueda_binaria(lista, elemento):
    
    izquierda = 0
    derecha = len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == elemento:
            return medio
        elif lista[medio] < elemento:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

lista = [1, 3, 5, 7, 9]
elemento = 5

indice = busqueda_lineal(lista, elemento)
print(f"El elemento {elemento} se encuentra en el índice {indice} (búsqueda lineal)")

indice = busqueda_binaria(lista, elemento)
print(f"El elemento {elemento} se encuentra en el índice {indice} (búsqueda binaria)")