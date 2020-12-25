
class Time(object):
    """Срок хранения"""
    def __init__(self, time):
        self._time = time
        print ('Срок хранения 3 месяца')

    def __getattr__(self, item):
        return getattr(self._time, item)

    def long(self):
        print('%s срок хранения продлен на 1 год' % self._time._name)

class Recipe(object):
    """Назначение врача"""
    def __init__(self, name):
        self._name = name

    def say(self):
        print('Принимать 2 раза в день по одной таблетке %s!' % self._name)





def main():
    recipe = Recipe('Флемоксин')

    recipe_time = Time(recipe)
    recipe_time.say()
    recipe_time.long()  



main()