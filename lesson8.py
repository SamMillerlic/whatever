class Rational:
    counter = 0
    def __init__(self,a,b):
        self._num = a
        self._den = b
        Rational.counter+=1
        
    def __str__(self):
        return "GO"
        
    def _reciprocate(self):
        (self._num,self._den) = (self._den,self._num)
        
    def transfer(self):
        self._reciprocate()
    
    def print(self):
        print('{0}/{1}'.format(self._num,self._den))
    
    @classmethod
    def test(cls):
        print('test!')
        
    @staticmethod
    def show():
        print(Rational.counter)
        
r = Rational(15,2)
##g = Rational(28,8)
##print(r._num)
##r.print()
##r.transfer()
##r.print()
##print(r)
##r.show()
r.test()