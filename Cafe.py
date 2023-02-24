import math

def cafeteria(bebida):
    if len(bebida) == 0:
        return "Nada"
    
    formato = bebida.split(', ')

    nombre = formato[0]
    tamanio = formato[1:]

    if len(nombre) < 2:
        return 'El nombre de la bebida debe tener al menos 2 caracteres'
    if len(nombre) > 15:
        return 'El nombre de la bebida debe ser menos de 15 caracteres'
    if not nombre.replace('','').isalpha():
        return 'No se puede tener un numero en el nombre'

    if len(tamanio) < 1:
        return 'Debe de por lo menos existir un tamaño de bebida'
    if len(tamanio) > 5:
        return 'Solo se puede hasta 5 tamaños de bebida'
    if not tamanio.replace('','').isdigit():
        return 'No se puede tener letras en el tamaño'

    for i in range(len(tamanio)):
        tamanio = tamanio[i]
        try:
            val = float(tamanio)
        except:
            if tamanio == '':
                return 'Se dejo un espacio vacio entre las comas'
        else:
            if math.floor(val) != val:
                return 'No se pueden usar decimales'
            if val == 0:
                return 'El tamaño es menor a 1'
            if val > 48:
                return 'El tamaño es mayor a 48'
            tamanio[i] = val
    
    if tamanio != sorted(tamanio):
        return 'Los tamaños solo pueden estar de forma ascendente'

    return 'La bebida y tamaños se agregaron correctamente'