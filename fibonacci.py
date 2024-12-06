#For Assignment 6 a simple fibonacci sequence is defined below, using iterators.
class Fibonacci:
    def __init__(self, constructor):

        self.constructor= constructor


    def __iter__(self):
    #First two fibonacci numbers must be defined to start the sequence,
        self.one= 0
        self.two= 1
        self.counter = 0
        return self

    def __next__(self):
        if type(self.constructor) is not int:
            raise ValueError
        if self.counter>= self.constructor+1 :
           raise StopIteration
        self.counter +=1
        #Current value is the first fibonacci number in a sequence(I.e self one), that is saved before
        # the numbers are updated below.
        self.current= self.one
        self.one= self.two
        #Since self.one is now updated to self.two, the saved number is added to self.one so the fibonacci iterations are possible
        self.two= self.one + self.current
        #Last step is to return the current/first number of the iteration
        return self.current





print (list(Fibonacci(10)))
print (list(Fibonacci(0)))
print (list(Fibonacci(1)))
print (list(Fibonacci(-1)))




