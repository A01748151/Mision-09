#Alberto Contreras Torres


def extraerPares(lista):
    nueva = []
    copia = list(lista)
    print(copia)
    if copia == []:
        return nueva
    else:
        for k in copia:
            if k % 2 == 0:
                nueva.append(k)

        return nueva


def extraerMayoresPrevio(lista):
    nueva= []
    copia= lista[:]
    for k in range(len(copia)):
        if k+1 < len(copia):
            if copia[k+1]>copia[k]:
                nueva.append(copia[k+1])

    return nueva




def intercambiarParejas(lista):
    nueva= []
    copia= lista[:]
    for k in range (len(copia)):
        if k % 2 == 0:
            pares = k

            nueva.append(pares)
            if k != pares:
                impares = k

                nueva.append(impares)



    return nueva


def intercambiarMM(lista):
    minimo = min(lista)
    maximo = max(lista)
    posicion = lista.index(minimo)
    posicion2 = lista.index(maximo)
    lista.insert(posicion2, minimo)
    lista.insert(posicion, maximo)
    datoEliminar = lista[posicion+1]
    datoEliminar2 = lista[posicion2+1]
    lista.remove(datoEliminar)
    lista.remove(datoEliminar2)
    return lista




def promediarCentro(lista):
    copia = lista[:]
    maximo = max(copia)
    minimo = min(copia)
    copia.remove(maximo)
    copia.remove(minimo)
    promedio = sum(copia)//len(copia)
    for k in copia:
        copia.remove(k)

    copia.append(promedio)
    return copia


def calcularEstadistica(lista):
    if lista == []:
        return (0,0)
    else:
        mean = sum(lista)/len(lista)
        deviation = (lista[1]-mean)*.5/len(lista)-1

        return mean, deviation


def calcularSuma(lista):

    lista.index(13)
    for k in lista:
        if k == 13:
            posicion = lista.index(13)
            lista.remove(lista[posicion])
            lista.remove(lista[posicion-1])
            lista.remove(lista[posicion+1])
    suma = sum(lista)

    return suma





def main():
    lista= [1,2,3,2,4,60,5,8,3,22,44,55]
    #lista = []
    a= extraerPares(lista)
    print(a)

    print("----------------------------------------------")
    lista = [1,2,3,2,4,60,5,8,3,22,44,55]
    b = extraerMayoresPrevio(lista)
    print(b)

    print("----------------------------------------------")
    lista =  [1,2,3,2,4,60,5,8,3,22,44,55]
    c = intercambiarParejas(lista)
    print(c)

    print("----------------------------------------------")

    lista =[5,9,3,22,19,31,10,7]
    d = intercambiarMM(lista)
    print(d)

    print("----------------------------------------------")

    lista = [95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85]
    e = promediarCentro(lista)
    print(e)

    print("----------------------------------------------")

    lista = [1,2,3,4,5,6]
    f = calcularEstadistica(lista)
    print(f)

    print("----------------------------------------------")

    lista = [5, 2, 13, 4, 1, 6, 1, 8, 4, 1, 5]
    g = calcularSuma(lista)
    print(g)

main()