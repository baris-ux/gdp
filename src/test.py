import unittest

from utils import calculer_moyenne, convertir_temperature  # Remplace 'utils' par le nom de ton fichier si nécessaire

class TestFonctionsUtilitaires(unittest.TestCase):

    # Tests pour calculer_moyenne
    def test_moyenne_liste_entiers(self):
        self.assertEqual(calculer_moyenne([1, 2, 3, 4, 5]), 3)

    def test_moyenne_liste_flottants(self):
        self.assertAlmostEqual(calculer_moyenne([1.5, 2.5, 3.5]), 2.5)

    def test_moyenne_liste_mixte(self):
        self.assertAlmostEqual(calculer_moyenne([1, 2.5, 4]), 2.5)

    def test_moyenne_liste_vide(self):
        self.assertIsNone(calculer_moyenne([]))

    def test_moyenne_element_non_numerique(self):
        with self.assertRaises(TypeError):
            calculer_moyenne([1, 'a', 3])

    # Tests pour convertir_temperature
    def test_conversion_C_vers_F(self):
        self.assertAlmostEqual(convertir_temperature(0, 'C', 'F'), 32)

    def test_conversion_C_vers_K(self):
        self.assertAlmostEqual(convertir_temperature(0, 'C', 'K'), 273.15)

    def test_conversion_F_vers_C(self):
        self.assertAlmostEqual(convertir_temperature(32, 'F', 'C'), 0)

    def test_conversion_F_vers_K(self):
        self.assertAlmostEqual(convertir_temperature(32, 'F', 'K'), 273.15)

    def test_conversion_K_vers_C(self):
        self.assertAlmostEqual(convertir_temperature(273.15, 'K', 'C'), 0)

    def test_conversion_K_vers_F(self):
        self.assertAlmostEqual(convertir_temperature(273.15, 'K', 'F'), 32)

    def test_conversion_meme_unite(self):
        self.assertEqual(convertir_temperature(100, 'C', 'C'), 100)

    def test_conversion_unite_invalide(self):
        with self.assertRaises(ValueError):
            convertir_temperature(100, 'X', 'C')

        with self.assertRaises(ValueError):
            convertir_temperature(100, 'C', 'Z')

if __name__ == '__main__':
    unittest.main()
