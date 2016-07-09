"""
This code implements the factory design patterns.
we create a single class called Colors that can create several different classes instances
"""

class Colors():

    color_palate = []

    def factory(type):
        """
        Inner classes we wish to create with through the Colors class
        :return:
        """
        class Black():
            def paint(self): print 'Paint it Black'
        class Blue():
            def paint(self):print 'Paint it Blue'

        if type =='Black':
            return Black()
        elif type == 'Blue':
            return Blue()

    factory = staticmethod(factory)

if __name__ == '__main__':

    Colors.factory('Black').paint()
    Colors.factory('Blue').paint()