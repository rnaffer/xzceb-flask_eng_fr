import unittest

from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_e2f_empty_input(self):
        self.assertEqual(english_to_french(None), 'Nothing to translate')
        self.assertEqual(english_to_french(''), 'Nothing to translate')
    
    def test_e2f(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
    
    def test_f2e_empty_input(self):
        self.assertEqual(french_to_english(None), 'Nothing to translate')
        self.assertEqual(french_to_english(''), 'Nothing to translate')
    
    def test_f2e(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

if __name__ == "__main__":
    unittest.main()