import urllib.parse
import requests
import simplejson
import json
from time import time, ctime

current_DateTime = time()

print('\n BIENVENIDO, HOY ES: ',ctime(current_DateTime))


main_api = "https://www.mapquestapi.com/directions/v2/route?"
#origin = "Bogota"
#dest = "Cali"
key = "SiWmyszv8znGG67FYHjXdjO9yTs14b7E"
#url = main_api + urllib.parse.urlencode({"key": key,"from":origin, "to":dest })
#json_data = requests.get(url).json()
#print(json_data) probar si funciona el formato json

#print("URL: "+(url))

#json_data = requests.get(url).json()
#json_status = json_data["info"]["statuscode"]

#if json_status == 0:
    #print("API Status: " + str(json_status) + " = A successfull router call .\n" )
    
while True:
    orig = input("LOCACION EMPIEZA EN: ")
    if orig == "quitar" or orig == "q":
        break
    dest = input("DESTINO: ")
    if dest == "quitar" or dest == "q":
        break
    url = main_api + urllib.parse.urlencode({"key": key,"from":orig, "to":dest })
    print("URL: "+ (url))
    
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    
    if json_status == 0:
        print("Estado API: " + str(json_status) + " = LLAMADA DE ROUTER EXITOSA .\n" )
        print("=============================================")
        print("Direcciones de" + (orig) + " hacia" + (dest))
        print("Duracion del viaje en h/m/s:	" + (json_data["route"]["formattedTime"])) 
        print("Millas:	" + str(json_data["route"]["distance"]))
        #print("Fuel Used (Gal): " + str(json_data["route"]["fuelUsed"])) 
        print("=============================================")
        print("Kilometros:	" + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        #print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)")) 
        print("=============================================\n")
        print ("SALIDA DEL PROGRAMA B")
    elif json_status == 402: 
        print("**********************************************")
        print("Estado de codigo: " + str(json_status) + "; Usuario ingresado invlaido por una o dos locaciones.")
        print("**********************************************\n") 
    else:
        print("************************************************************************") 
        print("Estado de codigo: " + str(json_status) + "; Refer to:") 
        print("https://developer.mapquest.com/documentation/directions-api/status-codes") 
        print("************************************************************************\n")

        print ("SALIDA DEL PROGRAMA B")