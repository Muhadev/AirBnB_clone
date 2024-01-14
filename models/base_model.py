#!/usr/bin/python3
"""
Module for Base class
Parent class for the airBnb clone project.
"""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Class for Base Model"""

    def __init__(self, *args, **kwargs):
        """Initialization for the Base instance
        Args:
            - *args: list of arguments
            - **kwargs: dict of key/value arguments
        """
        tformat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tformat)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def __str__(self):
        """String representation for instances"""
        return "[{}] ({}) <{}>".format(cls_name, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute `updated_at` with
        the current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of
        the instance"""
        my_dict = self.__dict__.copy()
        my_dict['created_at'] = my_dict['created_at'].isoformat()
        my_dict['updated_at'] = my_dict['updated_at'].isoformat()
        my_dict['__class__'] = self__class__.__name__
        return my_dict
