"""
This code implements the singleton design patterns.
Ruler is a class that creates a single instance only,
if a second (third..fourth..etc.) instance is created, the first instance is returned.
"""

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
        if Ruler._instance == None:
            Ruler._instance = createRuler(x)
        return Ruler._instance

    
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