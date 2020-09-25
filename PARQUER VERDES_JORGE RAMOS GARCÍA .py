
import statistics
#Esta biblioteca me permite calcular la desviación estandar y otras funciones relacionadas a la estadística


num_viviendas_manzana = int(input("Ingrese el número de viviendas en una manzana:"))

Kilometros_region= int(input("Ingrese los kilometros que se buscan analizar:"))

Lista_num_habitantes = []
while len(Lista_num_habitantes)<10:
    num_habitantes=int(input("Ingrese el número de habitantes por casa:"))
    Lista_num_habitantes.append(num_habitantes)

Lista_m_vivienda = []
while len(Lista_m_vivienda)<10:
    m_vivienda=int(input("Ingrese los m**2 de la vivienda:"))
    Lista_m_vivienda.append(m_vivienda)
 #Coloque dos listas de input para que de los datos requeridos   
Val_manzana = 6988.96
#Medición urbanistica básica
num_areas_persona = 9
#Numero de metros cuadrados recomendados por la OMS
media_ancho_calle = 6
area_ideal_parque_km =4.5

metros_region = Kilometros_region*1000000

lado_manzana = Val_manzana**(1/2)
#calculamos uno de los lados de la manzana
lado_region = metros_region**(1/2)

numero_manzanas_lado = (lado_region)//(media_ancho_calle+lado_manzana)

numero_manzanas_region = numero_manzanas_lado**2
#número de manzanas en toda la región
desviación_estandar_habitantes = statistics.stdev(Lista_num_habitantes)
media_habitantes = (sum(Lista_num_habitantes))/10

aproximacion_habitantes = desviación_estandar_habitantes+media_habitantes
#Con la media y la desviación estandar podemos aproximarnos a un mejor resultado 
desviación_estandar_vivienda = statistics.stdev(Lista_m_vivienda)
media_vivienda = (sum(Lista_num_habitantes))/10

if aproximacion_habitantes < 5:
    aproximacion_habitantes=aproximacion_habitantes+1
elif aproximacion_habitantes > 5:
    aproximacion_habitantes=aproximacion_habitantes-1
    
aproximacion_vivienda = desviación_estandar_vivienda+media_vivienda

densidad_poblacional_relativa = aproximacion_habitantes/aproximacion_vivienda
#esta densidad relativa es por casa
cantidad_viviendas_region = numero_manzanas_region*num_viviendas_manzana
#calculamos la cantidad de casas

cantidad_habitantes= densidad_poblacional_relativa*metros_region 

#calculamos la cantidad de habitantes
areas_verdes_m = cantidad_habitantes*num_areas_persona
#número de metros de áreas verdes necesarias
areas_verdes_km = areas_verdes_m/1000000



def cantidad_parques(area_ideal_parque_km,areas_verdes_km):
    return (areas_verdes_km/area_ideal_parque_km)

n = input("Hay niños en la región: si o no:")

def juegos_parques(n):
    if n=="si":
        return "Habra juegos"
    return "No habra juegos"

    
    
print("Cantidad de kilometros cuadrados de áreas verdes:",areas_verdes_km)

print("Cantidad de parques:",cantidad_parques(area_ideal_parque_km,areas_verdes_km),"Especificaciones:",juegos_parques(n))
