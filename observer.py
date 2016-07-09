'''
This code implements observer design pattern
observable will be a class that other class can follow after
each class (one/two) that follows observable will have a method named update

'''

class observable():

    obs = None


    def __init__(self):
        self.obs = []

    def add_observer(self,observer):
        self.obs.append(observer)

    def inform_all(self):
        print 'informing\n'
        for observer in self.obs:
            try:
                observer.update()
            except:
                continue
class one():

    def update(self):
        print 'one'

class two():

    def update(self):
        print 'two'


if __name__ == '__main__':

    one = one()
    two = two()

    obs = observable()

    obs.inform_all()
    obs.add_observer(one)
    obs.add_observer(two)

    obs.inform_all()