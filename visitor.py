"""
This script depicts the visitor design pattern
cat and mouse are classes under Visitor, where pray is the class
that connects every Visitor classes and can accept Visitor's classes
"""

class pray():

    def accept(self,predator):
        predator.visit(self)

    def eat(self,pray):
        print(self,'ate',pray)

    def get_eaten(self,predator):
        print(self,'got eaten by',predator)

class Visitor() :
    def __str__(self):
        return  self.__class__

class cat(Visitor):
    def visit(self,pray):
        pray.eat(self)


class mouse(Visitor):
    def visit(self,pray):
        pray.get_eaten(self)

if __name__ == '__main__':


    pray = pray()
    mouse = mouse()
    cat = cat()

    pray.accept(mouse)
    pray.accept(cat)