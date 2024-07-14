from os import listdir 
#metodo listdir recupera todos los nombres de los archivos que estan en una carpetya

#filename_list = listdir("pet_images/")
def get_pet_labels(image_dir):
    #Crear un diccionario de etiquetas de mascotas basado en nombres de archivos de imagen del 
    #direectorio
    filename_list = listdir(image_dir)
    dict_pet = dict()
    #Esto devuelve una lista de nombres de archivos en el directorio dado
    #Esto es para ver si la lista de archivos recuperada es correcta
    # Acá vamos a hacer un diccionario, donde la clave es el nombre de la imagen y el valor es el nombre de la mascota
    # Con parametros que el valor de la clave sean minusculas, y sin guiones bajos, y sin numeros
    for index in range (0, len(filename_list), 1):
        if filename_list[index][0] != ".": #Mira que el primer caracter del archivo que itera no sea un punto, porque significa que no es imagen
            low_pet = filename_list[index].lower() 
            pet_slip = low_pet.split("_")
            pet_name = ""
            for x in pet_slip:
                if x.isalpha(): #Verifica que sean solo algabeticos
                    pet_name += x + ""
            pet_name = pet_name.strip()
            
            if filename_list[index] not in dict_pet:
                filename_list[index] = pet_name
            else:
                print("**Warning: Key=", filename_list[index], "already exists in dict with value=", dict_pet[filename_list[index]])
            
    return dict_pet        
        
        
    results_dic = dict()