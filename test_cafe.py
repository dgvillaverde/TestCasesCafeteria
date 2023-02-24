import unittest
from Cafe import cafeteria


class CafeTest(unittest.TestCase):

    #Case 1 - Se ingresa un nombre de 4 Caracteres y 3 tamaños
    def test_n1(self):
        self.assertEqual(cafeteria('Agua, 1, 2, 3'), 'La bebida y tamaños se agregaron correctamente')
    
    #Case 2 - Se ingresa un nombre de 2 caracteres y 1 tamaño
    def test_n2(self):
        self.assertEqual(cafeteria('UP, 3'), 'La bebida y tamaños se agregaron correctamente')
if __name__ == '__main__':
    unittest.main()