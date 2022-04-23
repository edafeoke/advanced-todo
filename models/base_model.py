#!/usr/bin/python3
'''
a class BaseModel that defines
all common attributes/methods for other classes
'''

from datetime import datetime
import uuid


class BaseModel:
    '''
    a class BaseModel that defines
    all common attributes/methods for other classes
    '''

    id: str
    created_at: datetime
    updated_at: datetime

    def __init__(self) -> None:
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self) -> str:
        '''
        str representation of this object
        '''
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self) -> None:
        '''
        updates the public instance attribute updated_at
        with the current datetime
        '''

        self.updated_at = datetime.now()

    def to_dict(self) -> dict:
        '''
        returns a dictionary containing all keys/values of __dict__ of the instance
        '''
        self.__dict__['__class__'] = self.__class__.__name__
        self.__dict__['created_at'] = self.__dict__['created_at'].isoformat()
        self.__dict__['updated_at'] = self.__dict__['updated_at'].isoformat()
        return self.__dict__