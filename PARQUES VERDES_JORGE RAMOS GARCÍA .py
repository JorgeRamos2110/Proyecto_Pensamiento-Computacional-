import statistics
#Esta biblioteca extra me permite calcular la desviación estandar y otras funciones relacionadas a la estadística

VAL_MANZANA = 6988.96
#Medición urbanistica básica
NUM_AREAS_PERSONA = 9
#Numero de metros cuadrados recomendados por la OMS
MEDIA_ANCHO_CALLE = 6
#Medida media de calle
AREA_IDEAL_PARQUE_KM =4.5
#Medición urbanistica recomendada

num_viviendas_manzana = int(input
                        ("Ingrese el número de viviendas en una manzana:"))
#Nos da mediante in input el número de viviendas en una manzana
kilometros_region= int(input("Ingrese los kilometros que se buscan analizar:"))
#Los kilómetros totales a analizar
lista_num_habitantes = []
while len(lista_num_habitantes)<10:
    num_habitantes=int(input("Ingrese el número de habitantes por casa:"))
    lista_num_habitantes.append(num_habitantes)
#Valores del número de habitantes ordenados en listas
lista_m_vivienda = []
while len(lista_m_vivienda)<10:
    m_vivienda=int(input("Ingrese los m**2 de la vivienda:"))
    lista_m_vivienda.append(m_vivienda)
#Valores del tamaño de viviendas ordenados en listas
metros_region = kilometros_region*1000000

def numero_manzanas_region(metros_region, VAL_MANZANA, MEDIA_ANCHO_CALLE):
    lado_manzana = VAL_MANZANA**(1/2)
    lado_region = metros_region**(1/2)
    numero_manzanas_lado = (lado_region)/(MEDIA_ANCHO_CALLE+lado_manzana)
    numero_manzanas_region = numero_manzanas_lado**2
    return numero_manzanas_region
#Esta función sirve para calcular el numero_manzanas_region del área que se estudia 
numero_manzanas_region = numero_manzanas_region(metros_region, VAL_MANZANA,
                                                MEDIA_ANCHO_CALLE)

def aproximaciones (opcion, lista_num_habitantes, lista_m_vivienda):
    if (opcion==1):
        desviación_estandar_habitantes = statistics.stdev(lista_num_habitantes)
        media_habitantes = (sum(lista_num_habitantes))/10
        aproximacion_habitantes = desviación_estandar_habitantes+media_habitantes
        if (aproximacion_habitantes < 5):
            aproximacion_habitantes=aproximacion_habitantes+1
            return aproximacion_habitantes
        elif aproximacion_habitantes > 5:
            aproximacion_habitantes=aproximacion_habitantes-1
            return aproximacion_habitantes
    if (opcion==2):
        desviación_estandar_vivienda = statistics.stdev(lista_m_vivienda)
        media_vivienda = (sum(lista_num_habitantes))/10
        aproximacion_vivienda = desviación_estandar_vivienda+media_vivienda
        return aproximacion_vivienda
#Esta función se utiliza para calcular las aproximaciones de los habitantes y de las viviendas usando las listas

aproximacion_vivienda = aproximaciones(2, lista_num_habitantes, lista_m_vivienda)
aproximacion_habitantes = aproximaciones(1,lista_num_habitantes, lista_m_vivienda)
#Asignamos variables a los resultados de nuestras funciones

def areas_verdes_km(aproximacion_habitantes, aproximacion_vivienda,
                    metros_region, NUM_AREAS_PERSONA):
    densidad_poblacional_relativa = aproximacion_habitantes/aproximacion_vivienda
    cantidad_habitantes= densidad_poblacional_relativa*metros_region
    areas_verdes_m = cantidad_habitantes*NUM_AREAS_PERSONA
    return areas_verdes_m/1000000

areas_verdes_km = areas_verdes_km(aproximacion_habitantes, aproximacion_vivienda,
                    metros_region, NUM_AREAS_PERSONA)
#Asignamos una variable al resultado de la función 

def cantidad_parques(AREA_IDEAL_PARQUE_KM,areas_verdes_km):
    return (areas_verdes_km/AREA_IDEAL_PARQUE_KM)
#Esta función calcula la cantidad de parques tomando el area ideal y los km de área
cantidad_parques = cantidad_parques(AREA_IDEAL_PARQUE_KM,areas_verdes_km)
n = input("Hay niños en la región: si o no:")

def juegos_parques(n):
    if n=="si":
        return "Habra juegos"
    return "No habra juegos"
#Esta función nos dice si habra juegos o no 
def parques_manzana(areas_verdes_km, numero_manzanas_region):
    return (areas_verdes_km/numero_manzanas_region)
#Esta función da una alternativa al acomodo de los km de áreas verdes ahora en relacion a las manzanas 
parques_manzana = parques_manzana(areas_verdes_km, numero_manzanas_region)

print("Cantidad de kilómetros cuadrados de áreas verdes:",areas_verdes_km,",",
      "Cantidad de parques:",cantidad_parques,",",
      "Especificaciones:",juegos_parques(n),",", "Km de áreas verdes por manzana:",
      parques_manzana)
#Imprimimos los km de áreas verdes, la cantidad de parques y las especificaciones


