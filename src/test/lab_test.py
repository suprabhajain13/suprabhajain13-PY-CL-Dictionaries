# lab_test.py

import unittest
from src.main.lab import create_dict_from_lists, clear_dict, copy_dict, get_value, get_items, get_keys, remove_key, get_values

class TestDictionaryMethods(unittest.TestCase):

    def test_create_dict_from_lists(self):
        keys = ['a', 'b', 'c']
        values = [1, 2, 3]
        expected_dict = {'a': 1, 'b': 2, 'c': 3}
        output_dict = create_dict_from_lists(keys, values)
        self.assertEqual(output_dict, expected_dict)
        self.assertIsInstance(output_dict, dict)


    def test_clear_dict(self):
        test_dict = {'a': 1, 'b': 2, 'c': 3}
        clear_dict(test_dict)
        self.assertEqual(test_dict, {})

    def test_copy_dict(self):
        test_dict = {'a': 1, 'b': 2, 'c': 3}
        copied_dict = copy_dict(test_dict)
        self.assertEqual(test_dict, copied_dict)
        self.assertIsNot(test_dict, copied_dict)

    def test_get_value(self):
        test_dict = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(get_value(test_dict, 'b'), 2)
        self.assertIsNone(get_value(test_dict, 'd'))

    def test_get_items(self):
        test_dict = {'a': 1, 'b': 2, 'c': 3}
        expected_items = [('a', 1), ('b', 2), ('c', 3)]
        self.assertEqual(get_items(test_dict), expected_items)

    def test_get_keys(self):
        test_dict = {'a': 1, 'b': 2, 'c': 3}
        expected_keys = ['a', 'b', 'c']
        self.assertEqual(get_keys(test_dict), expected_keys)

    def test_remove_key(self):
        test_dict = {'a': 1, 'b': 2, 'c': 3}
        removed_value = remove_key(test_dict, 'b')
        self.assertEqual(test_dict, {'a': 1, 'c': 3})
        self.assertEqual(removed_value, 2)
        removed_value = remove_key(test_dict, 'd')
        self.assertIsNone(removed_value)

    def test_get_values(self):
        test_dict = {'a': 1, 'b': 2, 'c': 3}
        expected_values = [1, 2, 3]
        self.assertEqual(get_values(test_dict), expected_values)


if __name__ == '__main__':
    unittest.main()
