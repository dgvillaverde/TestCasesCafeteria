import unittest
from Cafe import cafeteria


class CafeTest(unittest.TestCase):

    #Case 1 - Se ingresa una bebida y 3 tamaños
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
        self.assertEqual(cafeteria('Squirt, -2, 3, 5, 10'), 'No se pueden numeros negativos')
    
    #Case 12 - Se ingresa un bebida y tamaños iguales
    def test_n12(self):
        self.assertEqual(cafeteria('Delaware, 2, 3, 5, 5'), 'No se puede tener tamaños iguales')
    
    #Case 13 - Se ingresa un bebida y tamaños en desorden
    def test_n13(self):
        self.assertEqual(cafeteria('Manzanita, 10, 3, 40, 1'), 'Los numeros estan en desorden')
    
    #Case 14 - Se ingresa un bebida con numero 
    def test_n14(self):
        self.assertEqual(cafeteria('1, 2, 5, 20, 40'), 'Solo numeros enteros')
    
    #Case 15 - Se ingresa un bebida y letras en los tamaños 
    #def test_n15(self):
    #    self.assertEqual(cafeteria('Boing, 2, mediano, 20, 40'), 'Solo numeros enteros')

    #Case 16 - Se ingresa una bebida y tamaños grandes
    def test_n16(self):
        self.assertEqual(cafeteria('CocaCola, 10, 20, 30, 48'), 'La bebida y tamaños se agregaron correctamente')
    
    #Case 17 - Se ingresa una bebida y 0 en los tamaños
    def test_n17(self):
        self.assertEqual(cafeteria('Jugo, 0, 20, 30, 48'), 'No se pueden tener 0 en los tamanios')
    
    #Case 18 - Se ingresa una bebida y 5 tamaños
    def test_n18(self):
        self.assertEqual(cafeteria('FuzeTea, 10, 20, 30, 40, 48'), 'La bebida y tamaños se agregaron correctamente')
    

if __name__ == '__main__':
    unittest.main()