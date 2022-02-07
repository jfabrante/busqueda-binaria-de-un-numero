import random
import time


def busquedaIngenua(lista, objetivo):
    for i in range(len(lista)):
        if(lista[i] == objetivo):
            return i
    return -1


def busquedaBinaria(lista, objetivo, limiteInferior = None, limiteSuperior = None):
    if(limiteInferior is None):
        limiteInferior = 0
    if (limiteSuperior is None):
        limiteSuperior = len(lista)-1

    if (limiteSuperior < limiteInferior):
        return -1

    puntoMedio = (limiteInferior + limiteSuperior) // 2

    if(lista[puntoMedio] == objetivo):
        return puntoMedio
    elif(objetivo < lista[puntoMedio]):
        return busquedaBinaria(lista, objetivo, limiteInferior, puntoMedio -1)
    else: 
        return busquedaBinaria(lista, objetivo, puntoMedio +1, limiteSuperior)


if(__name__=="__main__"):
    
    tamaño = 10000
    conjuntoInicial = set()

    while(len(conjuntoInicial) < tamaño):
        conjuntoInicial.add(random.randint(-3*tamaño, 3*tamaño))

    listaOrdenada = sorted(list(conjuntoInicial))

    # Medir el tiempo de búsqueda ingenua
    inicio = time.time()
    for objetivo in listaOrdenada:
        busquedaIngenua(listaOrdenada, objetivo)
    fin = time.time()
    print(f"Tiempo de búsqueda ingenua: {fin - inicio} segundos.")


    # Medir el tiempo de búsqueda binaria
    inicio = time.time()
    for objetivo in listaOrdenada:
        busquedaBinaria(listaOrdenada, objetivo)
    fin = time.time()
    print(f"Tiempo de búsqueda binaria: {fin - inicio} segundos.")