# Búsqueda Lineal y Búsqueda Binaria en Python

Este repositorio contiene implementaciones de dos algoritmos de búsqueda en Python: la búsqueda lineal y la búsqueda binaria. Estos algoritmos permiten encontrar la posición de un elemento específico dentro de una lista.

## Tabla de Contenidos

- [Introducción](#introducción)
- [Algoritmos de Búsqueda](#algoritmos-de-búsqueda)
  - [Búsqueda Lineal](#búsqueda-lineal)
  - [Búsqueda Binaria](#búsqueda-binaria)
- [Requisitos](#requisitos)
- [Ejemplo de Uso](#ejemplo-de-uso)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## Introducción

La búsqueda lineal y la búsqueda binaria son dos algoritmos fundamentales utilizados para encontrar elementos dentro de estructuras de datos. La búsqueda lineal es adecuada para listas no ordenadas, mientras que la búsqueda binaria requiere que la lista esté ordenada de antemano. 

## Algoritmos de Búsqueda

### Búsqueda Lineal

La búsqueda lineal recorre cada elemento de la lista desde el principio hasta el final hasta encontrar el elemento deseado o hasta verificar que el elemento no está en la lista.

#### Implementación:

```python
def busqueda_lineal(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1
```

### Búsqueda Binaria

La búsqueda binaria es un algoritmo más eficiente que divide la lista ordenada en mitades para encontrar el elemento buscado. Es necesario que la lista esté previamente ordenada.

#### Implementación:

```python
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
```

## Requisitos

- Python 3.x

No se requieren bibliotecas adicionales para ejecutar estos algoritmos.

## Ejemplo de Uso

```python
# Lista de ejemplo
lista = [1, 3, 5, 7, 9]
# Elemento a buscar
elemento = 5

# Búsqueda Lineal
indice = busqueda_lineal(lista, elemento)
print(f"El elemento {elemento} se encuentra en el índice {indice} (búsqueda lineal)")

# Búsqueda Binaria
indice = busqueda_binaria(lista, elemento)
print(f"El elemento {elemento} se encuentra en el índice {indice} (búsqueda binaria)")
```

### Salida Esperada

```
El elemento 5 se encuentra en el índice 2 (búsqueda lineal)
El elemento 5 se encuentra en el índice 2 (búsqueda binaria)
```

## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas mejorar este proyecto, siéntete libre de abrir un issue o enviar un pull request.
