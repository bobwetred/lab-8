# coding: utf-8

"""
Приспособленец (Flyweight) - паттерн, структурирующий объекты.
Использует разделение для эффективной поддержки множества мелких объектов.
"""

import weakref


class Attribute_flowers(object):
    """Приспособленец"""
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class Attribute_flowersFactory(object):
    """Фабрика приспособленцев"""
    _attribute = weakref.WeakValueDictionary()

    @classmethod
    def get_attribute(cls, name):
        value = cls._attribute.get(name)
        if value is None:
            value = Attribute_flowers(name)
            cls._attribute[name] = value
        return value


class FlowerBoutique(object):
    def __init__(self, flowers, color, attribute_name):
        self._flowers = flowers
        self._color = color
        self._attribute = Attribute_flowersFactory.get_attribute(attribute_name)

    def __str__(self):
        args = (self._attribute, self._flowers, self._color)
        return 'Атрибут букета: %s; Букет состоит из: (%s, %s)' % args


posy0 = FlowerBoutique('розы', 'красные', 'ленточка для букета')  
posy1 = FlowerBoutique('пионы', 'желтые', 'ленточка для букета')  

print (posy0)
print (posy1)
print (posy0._attribute) is (posy1._attribute)