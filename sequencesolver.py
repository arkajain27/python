from abc import ABC, abstractmethod

class Sequence(ABC):
    def _init_(self):
        self._numberList = []

    def _str_(self):
        return '\nSequence = %s' %(self._numberList)

    @abstractmethod
    def findFormula(self):
        pass

    @property
    def numberList(self):
        return self._numberList

    @numberList.setter
    def numberList(self, value):
        if all(isinstance(x, int) for x in value):
            self._numberList = value
        else:
            print('\n%s is not a linear/quadratic sequence'%(value))

class Quadratic(Sequence):
    def _init_(self):
        super()._init_()

    def _str_(self):
        return super()._str_() + '\nThis is a quadratic sequence'

    def findFormula(self):
        a = (self.numberList[0] + self.numberList[2] - 2*self.numberList[1])/2
        b = (8*self.numberList[1] - 5*self.numberList[0] - 3*self.numberList[2])/2
        c = 3*self.numberList[0] - 3*self.numberList[1] + self.numberList[2]
        return ('T(n) = %sn^2 + %sn + %s' %(a, b, c)).replace('+-', '- ')

class Linear(Sequence):
    def _init_(self):
        super()._init_()

    def _str_(self):
        return super()._str_() + '\nThis is a linear sequence'

    def findFormula(self):
        a = (self.numberList[1] - self.numberList[0])
        b = (self.numberList[0] - a)
        return ('T(n) = %sn + %s' %(a, b)).replace('+-', '- ')

