#!/usr/bin/python3
"""A module for a filestorage engine"""
import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        objects = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(objects, f)

    def reload(self):
        from models.base_model import BaseModel
        classmap = {"BaseModel": BaseModel}
        try:
            with open (self.__file_path) as f:
                objects = json.load(f)
             #   print(objects)
            for obj_dict in objects.values():
                cls_string = obj_dict["__class__"]
                clsname = classmap[cls_string]
                if clsname:
                    obj = clsname(**obj_dict)
                    self.new(obj)
        except (FileNotFoundError):
            pass
