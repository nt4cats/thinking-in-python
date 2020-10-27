class Dog:
    def eat(self, food):
        print('This dog eats the {}.'.format(food))

class Cat:
    def munch(self, food):
        print('This cat munches the {}.'.format(food))

    def get_munch(self):
        return self.munch

d = Dog()
c = Cat()

animal_feed = d.eat
animal_feed('popcorn')

animal_feed = c.get_munch()
animal_feed('steak')

