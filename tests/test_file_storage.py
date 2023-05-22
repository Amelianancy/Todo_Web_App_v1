import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        # Set up a temporary file path for testing
        self.file_path = "test_file.json"
        FileStorage._FileStorage__file_path = self.file_path
        self.storage = FileStorage()

    def tearDown(self):
        # Remove the temporary file after testing
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_empty(self):
        # Test if `all` method returns an empty dictionary when there are no objects
        objects = self.storage.all()
        self.assertEqual(len(objects), 0)

    def test_new(self):
        # Test the `new` method to add a new object to the storage
        obj = BaseModel()
        self.storage.new(obj)
        objects = self.storage.all()
        self.assertEqual(len(objects), 1)
        self.assertIn(f"BaseModel.{obj.id}", objects)

    def test_save_reload(self):
        # Test the `save` and `reload` methods to ensure data persistence
        obj1 = BaseModel()
        obj1.name = "Object 1"
        self.storage.new(obj1)
        self.storage.save()

        # Create a new FileStorage instance to simulate reloading
        storage2 = FileStorage()
        storage2.reload()
        objects = storage2.all()

        self.assertEqual(len(objects), 1)
        self.assertIn(f"BaseModel.{obj1.id}", objects)
        self.assertEqual(objects[f"BaseModel.{obj1.id}"]["name"], "Object 1")

    def test_reload_nonexistent_file(self):
        # Test if `reload` method handles the case when the file doesn't exist
        # Set a non-existent file path
        FileStorage._FileStorage__file_path = "nonexistent_file.json"
        storage = FileStorage()
        storage.reload()

        objects = storage.all()
        self.assertEqual(len(objects), 0)

if __name__ == "__main__":
    unittest.main()

