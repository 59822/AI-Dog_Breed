#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED: Katherinne lucia Paguatian Moreno
# REVISED DATE: 14/07/2024
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It 
#          should also allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results 
#          dictionary (results_dic).  
#         This function inputs:
#            -The results dictionary as results_dic within print_results 
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within 
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main. 
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.
##
# TODO 6: Define print_results function below, specifically replace the None
#       below by the function definition of the print_results function. 
#       Notice that this function doesn't to return anything because it  
#       prints a summary of the results using results_dic and results_stats_dic
# 
def print_results(results_dic, results_stats_dic, model, print_incorrect_dogs = False, print_incorrect_breed = False):
    """
    Imprime los resultados resumidos de la clasificación y luego imprime
    los casos de perros clasificados incorrectamente y razas de perros 
    clasificadas incorrectamente si el usuario indica que desea esos resultados.
    
    Parámetros:
    results_dic - Diccionario con clave como el nombre del archivo de imagen y valor como una Lista 
                (índice)idx 0 = etiqueta de la imagen de mascota (string)
                        idx 1 = etiqueta del clasificador (string)
                        idx 2 = 1/0 (int) donde 1 = coincidencia entre la etiqueta de la imagen de mascota
                                y las etiquetas del clasificador y 0 = no coincidencia entre etiquetas
                        idx 3 = 1/0 (int) donde 1 = la imagen de la mascota 'es un' perro y 
                                0 = la imagen de la mascota 'NO es un' perro.
                        idx 4 = 1/0 (int) donde 1 = El clasificador clasifica la imagen 
                                'como un' perro y 0 = El clasificador clasifica la imagen  
                                'como NO un' perro.
    results_stats_dic - Diccionario que contiene las estadísticas de los resultados (ya sea
                        un porcentaje o un conteo) donde la clave es el nombre de la estadística 
                        (por ejemplo, 'n_correct_dogs') y el valor es el valor de esa estadística
                        (por ejemplo, un número entero 30).
    model - El nombre de la arquitectura del modelo de la CNN (string).
    print_incorrect_dogs - Booleano que indica si se imprimen los perros clasificados incorrectamente 
                            (defaults a False).
    print_incorrect_breed - Booleano que indica si se imprimen las razas de perros clasificadas incorrectamente 
                            (defaults a False).
    
    No retorna nada, solo imprime un resumen de los resultados.
    """    
    print(f"El modelo es {model}")
    print("El numero de imagenes es {}\nEl numero de perros es {}\nEl numero de imagenes que no son perros es {}".format(results_stats_dic['n_images'], results_stats_dic['n_dogs_img'], results_stats_dic['n_notdogs_img']))
    #Imprimir estadisticas de porcentaje
    print("El porcentaje es:")
    for key, value in results_stats_dic.items():
        if key.startswith('pct'): #Si empieza con pct
            print(f"{key} : {value}")
    #Imprimir los perros clasificados incorrectamente
    if (print_incorrect_dogs and 
        (results_stats_dic['n_correct_dogs']  != results_stats_dic['n_correct_breed'])
        ):
            print("Perros clasificados incorrectamente:")
    
    for key in results_dic:
        if sum(results_dic[key][3:]) == 2 and results_dic[key][2] == 0:
            print(f"Image: {key}\nReal label: {results_dic[key][0]}\nClasifier label: {results_dic[key][1]}")
    
    if print_incorrect_breed and ((results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs']) != results_stats_dic['n_images']):
        for key in results_dic:
            if sum(results_dic[key][3:]) == 1:
                print(f"Image: {key}\nReal label: {results_dic[key][0]}\nClasifier label: {results_dic[key][1]}")
            

