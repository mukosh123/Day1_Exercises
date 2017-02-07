#Polymorphic behaviour allows you to specify common methods in an "abstract" level, and implement them in particular instances.
class Person(object):
    def pay_bill():
        raise NotImplementedError

class Millionare(Person):
    def pay_bill():
        print "Here you go! Keep the change!"

class GradStudent(Person):
    def pay_bill():
        print "Can I owe you ten bucks or do the dishes?"
#You see, millionares and grad students are both persons. But when it comes to paying a bill, their specific "pay the bill" action is different.