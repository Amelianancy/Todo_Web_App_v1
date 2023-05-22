import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_init(self):
        my_instance = BaseModel()
        self.assertIsInstance(my_instance, BaseModel)
        self.assertIsInstance(my_instance.id, str)
        self.assertIsInstance(my_instance.created_at, datetime)
        self.assertIsInstance(my_instance.updated_at, datetime)
        # Test initialization with kwargs
        kwargs = {
            'id': 'my_id',
            'created_at': '2022-01-01T00:00:00.000000',
            'updated_at': '2022-01-01T01:00:00.000000',
            'name': 'my_name'
        }
        my_instance = BaseModel(**kwargs)
        self.assertIsInstance('my_id', str)
        self.assertEqual(my_instance.created_at, datetime(2022, 1, 1, 0, 0))
        self.assertEqual(my_instance.updated_at, datetime(2022, 1, 1, 1, 0))
        self.assertIsInstance('my_name', str)

    def test_str(self):
        my_instance = BaseModel()
        self.assertEqual(str(my_instance), f"[BaseModel] ({my_instance.id}) {my_instance.__dict__}")

    def test_save(self):
        my_instance = BaseModel()
        old_updated_at = my_instance.updated_at
        my_instance.save()
        self.assertNotEqual(old_updated_at, my_instance.updated_at)

    def test_to_dict(self):
        my_instance = BaseModel()
        result_dict = my_instance.to_dict()
        self.assertIsInstance(result_dict, dict)
        self.assertEqual(result_dict['__class__'], 'BaseModel')
        self.assertEqual(result_dict['created_at'], my_instance.created_at.isoformat())
        self.assertEqual(result_dict['updated_at'], my_instance.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()
