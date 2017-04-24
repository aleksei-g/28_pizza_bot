from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import base


class Pizza(base):
    __tablename__ = 'pizza'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), unique=True)
    description = Column(String(200))
    choices = relationship('PizzaChoices',
                           order_by='PizzaChoices.price',
                           back_populates='pizza')

    def __init__(self, title=None, description=None):
        self.title = title
        self.description = description

    def __repr__(self):
        return '{}: {}'.format(self.title, self.description)


class PizzaChoices(base):
    __tablename__ = 'pizza_choices'
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    price = Column(Float)
    pizza_id = Column(Integer, ForeignKey('pizza.id'))
    pizza = relationship('Pizza', back_populates='choices')

    def __init__(self, title=None, price=0):
        self.title = title
        self.price = price

    def __repr__(self):
        return '{} {} руб.'.format(self.title, self.price)
