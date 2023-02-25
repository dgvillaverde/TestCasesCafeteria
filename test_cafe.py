import unittest
from Cafe import cafeteria


class CafeTest(unittest.TestCase):

    #Test Cases Individuales
    #Case 1 - Se ingresa una bebida de 4 Caracteres y 3 tamaños
    def test_n1(self):
        self.assertEqual(cafeteria('Agua, 1, 2, 3'), 'La bebida y tamaños se agregaron correctamente')
    
    #Case 2 - Se ingresa una bebida de 2 caracteres y 1 tamaño
    def test_n2(self):
        self.assertEqual(cafeteria('UP, 3'), 'La bebida y tamaños se agregaron correctamente')
    
    #Case 3 - Se ingresa una bebida y mas de 5 tamaños
    def test_n3(self):
        self.assertEqual(cafeteria('Agua de Limon, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11'), 'Son demasiados tamaños')
    
    #Case 4 - Se ingresa una bebida de 1 caracter y 1 tamaño
    def test_n4(self):
        self.assertEqual(cafeteria('A, 3'), 'Recuerda que deben ser al menos 2 caracteres para el nombre')

    #Case 5 - Se ingresa una bebida de 0 caracteres y 1 tamaño
    def test_n5(self):
        self.assertEqual(cafeteria(', 10'), 'Falta el nombre de la bebida')
    
    #Case 6 - Se ingresa una bebida y 0 tamaños
    def test_n6(self):
        self.assertEqual(cafeteria('Cafe, '), 'Falta los tamaños de las bebidas')

    #Case 7 - Se ingresa una bebida de 16 caracteres y 5 tamaños
    def test_n7(self):
        self.assertEqual(cafeteria('Agua de pepino y limon, 1, 5, 10, 30'), 'Son demasiados caracteres en el nombre')
    
    #Case 8 - Se ingresa una doble coma
    def test_n8(self):
        self.assertEqual(cafeteria('Sprite,, 5, 7'), 'Pusiste dos comas')
    
    #Case 9 - Se ingresa una bebida y tamaños de forma descendente
    def test_n9(self):
        self.assertEqual(cafeteria('Fanta, 10, 4, 2, 1'), 'Los tamanios deben ser ascendentes')
    
    #Case 10 - Se ingresa un bebida y tamaños con decimales 
    def test_n10(self):
        self.assertEqual(cafeteria('Limonada, 2.5, 3, 5.5, 10'), 'Solo numeros enteros')
    
    #Case 11 - Se ingresa un bebida y tamaños con negativos
    def test_n11(self):
        self.assertEqual(cafeteria('Squirt, -2, 3, 5, 10'), 'Solo numeros enteros')

    #Test Cases del Profesor


if __name__ == '__main__':
    unittest.main()