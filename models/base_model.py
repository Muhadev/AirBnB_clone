#!/usr/bin/python3
""" Class BaseModel """
from datetime import datetime
import uuid


class BaseModel:
    """ construct class """
    def __init__(self, *args, **kwargs):
        """
        Initialization for the base instance
        Args:
            - *args: list of arguments
            - **kwargs: dict of key/value arguments
        """
        if kwargs != {} and kwargs is not None:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f"
                    )
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"
                    )
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        return "[{}] ({}) <{}>".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return a dictionary containing all keys/values of __dict__ of the instance.
        """ 
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = self.['created_at'].isoformat()
        obj_dict['updated_at'] = self.['updated_at'].isoformat()
        return obj_dict
