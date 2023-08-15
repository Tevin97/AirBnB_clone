#!/usr/bin/python3
"""Defines all common attributes/methods for other classes"""

import uuid
from datetime import datetime
import models


class BaseModel():
    """Base class for all models"""

    def __init__(self, *args, **kwargs):
        """class constructor for class BaseModel: Initialization of a Base instance.
        
        Args: 
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """
        if kwargs:

            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                    '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                    '%Y-%m-%dT%H:%M:%S.%f')

            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        string of BaseModel instance:
            Returns a readable string representation of BaseModel instances
        """

        return "[{}] ({}) {}".format(self.__class__.__name__,
                self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary that contains all
        keys/values of the instance
        """
        new_dict = dict(self.__dict__)
        new_dict['created_at'] = self.__dict__['created_at'].isoformat()
        new_dict['updated_at'] = self.__dict__['updated_at'].isoformat()
        new_dict['__class__'] = self.__class__.__name__
        return (new_dict)
