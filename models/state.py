#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import environ
import models


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete-orphan",
                          backref="state")

    if environ.get('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """ getter attribute that connects relationship"""
            cities = [
                value for key, value in models.storage.all(models.City).items()
                if value.state_id == self.id
            ]
            return cities
