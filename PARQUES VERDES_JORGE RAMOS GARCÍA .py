"""
Este proyecto nos da una aproximación
al número de km de áreas verdes recomendadas
por la OMS, tomando como parámetros
10 encuestas realizadas a personas de
la región.
"""
#Biblioteca
import statistics
"""
Esta biblioteca extra me permite calcular
la desviación estándar y
otras funciones relacionadas a la estadística.
"""
#Funciones
def numero_manzanas_region(metros_region, VAL_MANZANA, MEDIA_ANCHO_CALLE):
    """
    (Operadores, funciones)
    Recibe: el valor de metros_region y las constantes VAL_MANZANA y
    MEDIA_ANCHO_CALLE
    Calcula lado_manzana sacando la raíz cuadrada de la constante VAL_MANZANA
    Calcula el lado_region sacando la raíz cuadrada de metros_region
    Calcula el numero_manzanas_lado al dividir el lado_region entre la
    sumatoria de MEDIA_ANCHO_CALLE y el lado_manzana
    Sacamos el numero_manzanas_region al elevar al cuadrado el valor
    de numero_manzanas_region
    Devuelve: el numero_manzanas_region
    """
    lado_manzana = VAL_MANZANA**(1/2)
    lado_region = metros_region**(1/2)
    numero_manzanas_lado = (lado_region)/(MEDIA_ANCHO_CALLE+lado_manzana)
    numero_manzanas_region = numero_manzanas_lado**2
    return numero_manzanas_region


def aproximaciones(opcion, lista_num_habitantes, lista_m_vivienda):
    """
    (Operadores, funciones, condicionales, condicionales anidados,
    uso de biblioteca, listas)
    Recibe: el valor de la opcion, las listas lista_num_habitantes y
    lista_m_vivienda
    Mediante un condicional determina usando el valor de opcion si entra
    en el primer segmento o en el segundo; si entra a la primera parte
    toma la lista lista_num_habitantes y utilizando la biblioteca extra
    calcula la desviación estándar de la lista, obtiene la media_habitantes
    al sumar los valores de la lista y dividirlo entre 10, posteriormente
    calcula  la aproximacion_habitantes al sumar los dos valores calculados
    previamente, ingresa nuevamente a un condicional de acuerdo 
    al valor de la aproximación_habitantes en donde si esta es mayor 
    a 5 le resta una unidad y si es menor a 5 le suma una unidad;
    ahora cuando entra al segundo segmento calcula la desviación
    estándar de la lista_m_vivienda con la biblioteca extra, calcula 
    la media_vivienda al sumar los valores de la lista_m_habitantes y
    dividirlo entre 10 y finalmente calcular la aproximacion_vivienda al
    sumar los dos valores obtenidos anteriormente.
    Devuelve: aproximacion_habitantes y aproximacion_vivienda
    """
    if (opcion==1):
        desviacion_estandar_habitantes = statistics.stdev(lista_num_habitantes)
        media_habitantes = (sum(lista_num_habitantes))/10
        aproximacion_habitantes = (desviacion_estandar_habitantes+
                                   media_habitantes)
        if (aproximacion_habitantes < 5):
            aproximacion_habitantes=aproximacion_habitantes+1
            return aproximacion_habitantes
        elif aproximacion_habitantes > 5:
            aproximacion_habitantes=aproximacion_habitantes-1
            return aproximacion_habitantes
    if (opcion==2):
        desviacion_estandar_vivienda = statistics.stdev(lista_m_vivienda)
        media_vivienda = (sum(lista_num_habitantes))/10
        aproximacion_vivienda = desviacion_estandar_vivienda+media_vivienda
        return aproximacion_vivienda


def areas_verdes_km(aproximacion_habitantes, aproximacion_vivienda,
                    metros_region, NUM_AREAS_PERSONA):
    """
    (operadores, funciones)
    Recibe: valor de aproximacion_habitantes, aproximacion_vivienda,
    metros_region y la constante NUM_AREAS_PERSONAS
    Calcula areas_verdes_m al dividir la aproximacion_habitantes entre
    la aproximacion_vivienda, se multiplica el valor de esa división
    por los metros_region
    Devuelve: el valor de areas_verdes entre 1000000
    """
    densidad_poblacional_relativa = (aproximacion_habitantes/
                                     aproximacion_vivienda)
    cantidad_habitantes= densidad_poblacional_relativa*metros_region
    areas_verdes_m = cantidad_habitantes*NUM_AREAS_PERSONA
    return areas_verdes_m/1000000


def cantidad_parques(AREA_IDEAL_PARQUE_KM,areas_verdes_km):
    """
    (Operadores, funciones)
    Recibe: el valor de areas_verdes_km y la constante AREA_IDEAL_PARQUES_KM
    Calcula la cantidad de parques usando los dos valores dados
    Devuelve: la división entre areas_verdes_km y AREA_IDEAL_PARQUE_KM
    """
    return (areas_verdes_km/AREA_IDEAL_PARQUE_KM)


def juegos_parques(n):
    """
    (Funciones, condicionales)
    Recibe: el valor string de n
    Usando condicionales determina si habrá juegos o no
    de acuerdo al valor de n
    Devuelve: "Habrá juegos" o "No habrá juegos"
    """
    if n=="si":
        return "Habrá juegos"
    return "No habrá juegos"


def parques_manzana(areas_verdes_km, numero_manzanas_region):
    """
    (Operadores, funciones)
    Recibe: el valor de areas_verdes_km y el numero_manzanas_region
    Calcula la cantidad de parques en relación con los dos valores dados
    Devuelve: la división entre areas_verdes_km y numero_manzanas_region
    """
    return (areas_verdes_km/numero_manzanas_region)
"""
Esta función da una alternativa al acomodo
de los km de áreas verdes ahora en relación a las manzanas,
tomando los km de áreas verdes y
el número de manzanas de la región.
"""

#Constantes
VAL_MANZANA = 6988.96
#Medición urbanística básica
NUM_AREAS_PERSONA = 9
#Numero de metros cuadrados recomendados por la OMS
MEDIA_ANCHO_CALLE = 6
#Medida media de calle
AREA_IDEAL_PARQUE_KM =4.5
#Medición urbanística recomendada

#Inputs
num_viviendas_manzana = int(input("Número de viviendas en una manzana:"))

kilometros_region= int(input("Kilómetros que se buscan analizar:"))

n = input("Hay niños en la región: si o no:")


#Encuestas en forma de listas
lista_num_habitantes = []
while len(lista_num_habitantes)<10:
    num_habitantes=int(input("Ingrese el número de habitantes por casa:"))
    lista_num_habitantes.append(num_habitantes)
"""
El usuario nos da la información de 10
encuestas sobre el número de habitantes,
los cuales colocamos en listas para su mejor manejo.
"""
lista_m_vivienda = []
while len(lista_m_vivienda)<10:
    m_vivienda=int(input("Ingrese los m**2 de la vivienda:"))
    lista_m_vivienda.append(m_vivienda)
"""
El usuario nos da la información de 10
encuestas sobre el tamaño de las viviendas,
los cuales colocamos en listas para su mejor manejo.
"""

#Conversión
metros_region = kilometros_region*1000000


#Damos variables al resultado de funciones
numero_manzanas_region = numero_manzanas_region(metros_region, VAL_MANZANA,
                                                MEDIA_ANCHO_CALLE)

aproximacion_vivienda = aproximaciones(2, lista_num_habitantes,
                                       lista_m_vivienda)
aproximacion_habitantes = aproximaciones(1, lista_num_habitantes,
                                         lista_m_vivienda)

areas_verdes_km = areas_verdes_km(aproximacion_habitantes,
                                  aproximacion_vivienda,
                                  metros_region, NUM_AREAS_PERSONA)

cantidad_parques = cantidad_parques(AREA_IDEAL_PARQUE_KM, areas_verdes_km)

parques_manzana = parques_manzana(areas_verdes_km,
                                  numero_manzanas_region)


print("Cantidad de kilómetros cuadrados de áreas verdes:",
      areas_verdes_km,",", "Cantidad de parques:",
      cantidad_parques,",","Especificaciones:",
      juegos_parques(n),",", "Km de áreas verdes por manzana:",
      parques_manzana)
"""
Finalmente imprimimos los km de áreas verdes,
la cantidad de parques con la medida urbanística recomendada,
las especificaciones y
la cantidad de parques por manzanas.
"""
