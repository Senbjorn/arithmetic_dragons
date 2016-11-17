# coding: utf-8
# license: GPLv3
from gameunit import *

class Hero(Attacker):
	_name = None
	_experience = 0

	def __init__(self, name):
		self._health = 100
		self._attack = 50
		self._name = name

	def set_experience(self, experience):
		self._experience = experience

	def get_experience(self):
		return self._experience

#FIXME:
"""В этом файле должен быть описан класс героя, унаследованный от Attacker
Герой должен иметь 100 поинтов здоровья, атаку 50, опыт 0, имя, задаваемое в конструкторе
Метод attack должен получать атрибут target и уменьшать его здоровье на величину атаки.

"""
