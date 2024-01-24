import random
class Master(object):
    def __init__(self):
        self.kongfu = '[old method]'

    def make_cake(self):
        print(f'use {self.kongfu} make cake')


class School(object):
    def __init__(self):
        self.kongfu = '[new method]'

    def make_cake(self):
        print(f'use {self.kongfu} make cake')

class Prentice(School,Master):
    def __init__(self):
        self.kongfu = '[myown method]'

    def make_cake(self):
        print(f'use {self.kongfu} make cake')


daqiu = Prentice()
print(daqiu.kongfu)
daqiu.make_cake()

print(Prentice.__mro__)