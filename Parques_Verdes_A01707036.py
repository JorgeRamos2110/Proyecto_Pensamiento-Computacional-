import statistics


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
    
Val_manzana = 6988.96

num_areas_persona = 9

media_ancho_calle = 6

metros_region = Kilometros_region*1000000

lado_manzana = Val_manzana**(1/2)

lado_region = metros_region**(1/2)

numero_manzanas_lado = (lado_region)//(media_ancho_calle+lado_manzana)

numero_manzanas_region = numero_manzanas_lado**2

desviación_estandar_habitantes = statistics.stdev(Lista_num_habitantes)
media_habitantes = (sum(Lista_num_habitantes))/10

aproximacion_habitantes = desviación_estandar_habitantes+media_habitantes

desviación_estandar_vivienda = statistics.stdev(Lista_m_vivienda)
media_vivienda = (sum(Lista_num_habitantes))/10

aproximacion_vivienda = desviación_estandar_vivienda+media_vivienda

densidad_poblacional_relativa = aproximacion_habitantes/aproximacion_vivienda

cantidad_viviendas_region = numero_manzanas_region*num_viviendas_manzana

densidad_poblacional_total = densidad_poblacional_relativa*cantidad_viviendas_region

densidad_poblacional_total_km = densidad_poblacional_total/(1*10**(-6))

cantidad_habitantes= densidad_poblacional_total_km*Kilometros_region

areas_verdes_m = cantidad_habitantes*num_areas_persona

areas_verdes_km= areas_verdes_m/1000000

print("Cantidad de kilometros cuadrados de áreas verdes:",areas_verdes_km)

