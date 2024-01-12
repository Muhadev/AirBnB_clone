#!/usr/bin/python3
''' FileStorage module '''
import json
from models.base_model import BaseModel


class FileStorage:
	'''FileStorage class'''

	__file_path = 'file.json'
	__objects = {}
	
	def all(self, cls=None):
        """Return a dictionary of instantiated objects in __objects.

        If a cls is specified, returns a dictionary of objects of that type.
        Otherwise, returns the __objects dictionary.
        """
        if cls is not None:
            if type(cls) == str:
                cls = eval(cls)
            cls_dict = {}
            for k, v in self.__objects.items():
                if type(v) == cls:
                    cls_dict[k] = v
            return cls_dict
        return self.__objects

	def new(self, obj):
		'''
       		sets in objects with key classname.id
        	Args:
			object
        	'''
		key = "{}.{}".format(obj.__class__.__name__, obj.id)
		self.__objects[key] = obj
	def save(self):
		"""Serialize __objects to the JSON file __file_path."""
		obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
		with open(self.__file_path, 'w', encoding="utf-8") as file:
			json.dump(obj_dict, file)
	def reload(self):
		"""Deserialize the JSON file __file_path to __objects, if it exists."""
		try:
			with open(self.__file_path, 'r') as json_file:
				obj_dict = json.load(json_file)
			for key, value in obj_dict.items():
				class_name, obj_id = key.split('.')
				obj_instance = globals()[class_name](**value)
				self.__objects[key] = obj_instance
		except FileNotFoundError:
			pass		
