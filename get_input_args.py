import argparse
# Argpase es un módulo de Python que facilita la creación de
# interfaces de línea de comandos. 
# La principal ventaja de argparse es que automáticamente genera
# ayuda y mensajes de error.

def get_input_args():
    # Create Parse using ArgumentParser
    # Argument Parser es una clase que permite la lectura de argumentos
    parse = argparse.ArgumentParser(description = 'Arguments for pet image classifier ')
    # El parser especifica el tipo de datos en argumentso
    parse.add_argument('--dir', type=str, default = 'pet_images/', help = 'path to the folder of pet images')
    parse.add_Argument('arch', type=str, default = 'vgg', help = 'CNN model architecture to use')
    parse.add_Argument('--dogfile', type = str, default = 'dognames.txt', help = 'text file' )
    
    args = parse.parse_args()
    # parse_args() es un método que analiza los argumentos de la línea de comandos
    # y los devuelve como un objeto.
    
    return args

if __name__ == "__main__":
    get_input_args()
    
# The get_input_args function returns these three arguments as the variable in_arg. 