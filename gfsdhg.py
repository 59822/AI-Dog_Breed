'''import time

# Obtener la hora actual en segundos desde la época (1 de enero de 1970)
epoch_time = time.time()
print("Hora actual en segundos desde la época:", epoch_time)

# Convertir tiempo en segundos desde la época a una tupla de tiempo local
local_time = time.localtime(epoch_time)
print("Hora local:", local_time)

# Formatear una tupla de tiempo a una cadena de fecha y hora legible
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
print("Fecha y hora formateada:", formatted_time)

# Pausar la ejecución del programa por un tiempo determinado (en segundos)
print("Esperando 2 segundos...")
time.sleep(2)
print("Continuando después de la pausa")

# Medir el tiempo transcurrido entre dos eventos
start_time = time.time()
# Realizar alguna operación
time.sleep(1)
end_time = time.time()
elapsed_time = end_time - start_time
print("Tiempo transcurrido:", elapsed_time, "segundos")

## Sets pet_image variable to a filename 
pet_image = "Boston_terrier_02259.jpg"

## Sets string to lower case letters
low_pet_image = pet_image.lower()

## Splits lower case string by _ to break into words 
word_list_pet_image = low_pet_image.split("_")
print(word_list_pet_image, "ok")
## Create pet_name starting as empty string
pet_name = ""

## Loops to check if word in pet name is only
## alphabetic characters - if true append word
## to pet_name separated by trailing space 
for word in word_list_pet_image:
    if word.isalpha():
        pet_name += word + " "

## Strip off starting/trailing whitespace characters 
print(pet_name, "vale")
pet_name = pet_name.strip()
#
print(pet_name, "valeeee")
## Prints resulting pet_name
print("\nFilename=", pet_image, "   Label=", pet_name)'''

diccionario = dict()
with open('dognames.txt', "r") as f:
    for line in f:
        line = line.rstrip()
        if line not in diccionario:
            diccionario[line] = 1

print(diccionario)
    