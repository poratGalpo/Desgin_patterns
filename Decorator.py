"""
This code implements the decorator design patterns.
We'll create a class of a person and create method of controlling him
"""

class person:



    def __init__(self):
        print 'New Person was created'

    ############################
    # Let's create some setters#
    ############################

    def put_shirt(fun):
        def inner(*args, **kwargs):
            person.get_wrapped('shirt')
            return fun(*args, **kwargs)
        return inner

    def put_shoes(fun):
        def inner(*args, **kwargs):
            person.get_wrapped('shoes')
            return fun(*args, **kwargs)
        return inner

    def put_underwear(fun):
        def inner(*args, **kwargs):
            person.get_wrapped('underwear')
            return fun(*args, **kwargs)
        return inner

    def put_pants(fun):

        def inner(*args, **kwargs):
            person.get_wrapped('pants')
            return fun(*args, **kwargs)
        return inner

    @staticmethod
    def get_wrapped (item):
        print 'Wearing %s\n' % item


    @put_underwear
    @put_pants
    @put_shoes
    @put_shirt
    def leave_house(self):
        """
        We want to make sure that the person does not leave the house without a full cloths
        :return:
        """
        print 'Leaving the house'

if __name__ == '__main__':

    person_instance = person()
    person_instance.leave_house()