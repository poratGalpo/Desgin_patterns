"""
This code implements the singleton design patterns.
Ruler is a class that creates a single instance only,
if a second (third..fourth..etc.) instance is created, the first instance is returned.
"""
active_classes = {}
import random


def createRuler(x):

    """
    This method is responsible for deferring between instances of Ruler class
    :param x: str.
    :return: string containing x
    """
    return "This is ruler number {0}".format(x)




class Ruler():
    """
    Ruler is the singleton class we wish to create only once
    _instance will be the instance it of Ruler
    """
    _instance = None

    def create_instance(self,x):
        return self.__new__(x)

    def __new__(cls,x, *args, **kwargs):
        if cls._instance == None:
            Ruler._instance = createRuler(x)
        return Ruler._instance


def singleton(cls):
    global active_classes
    def inner(*args, **kwargs):
        if cls not in active_classes:
            instance = cls(*args, **kwargs)
            active_classes[cls] = instance

        return active_classes[cls]
    return inner()

@singleton
class Ruler2():
    """
    Ruler2 creates is instance in a much more elegant manner
    it uses a outer function as a decorator and a global variable that keeps track of
    all the instances already created
    """

    def __init__(self):
        """
        To see if the instance is really the same, let us randomize some number upon instance creation
        :return: None
        """
        self.x = random.randint(0,100)

    def __call__(self, *args, **kwargs):
        return self.x

    def __str__(self):
        return str(self.x)

if __name__ == '__main__':
    """
    Checking if the class we created correctly
    """


    test_instance = Ruler()
    ruler1 = test_instance.create_instance('6')
    ruler2 = test_instance.create_instance('7')
    abc = Ruler()
    ruler3 = abc.create_instance('8')
    print "Ruler1 : {0} \n Ruler2: {1}".format(ruler1,ruler3)
    ruler3_prime = Ruler2()
    ruler4_prime = Ruler2()
    print "Ruler3 : {0} \n Ruler4: {1}".format(ruler3_prime,ruler4_prime)
