trail = [[]]

def push():
    trail.append([])

def back():
    for var, oldval, newval in reversed(trail.pop(-1)):
        var._value = oldval

def backtrack(n):
    while current() > n:
        back()

def current():
    return len(trail)-1

def reset():
    trail[:] = [[]]

class Var:
    def __init__(self, value):
        self._value = value
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, val):
        trail[-1].append((self, self._value, val))
        self._value = val

if __name__ == '__main__':
    def test1():
        v1 = Var(10)
        assert v1.value == 10
        push()
        v1.value = 100
        assert v1.value == 100

    def test2():
        v1 = Var(0)
        for i in range(8):
            push()
            for j in range(5):
                v1.value = (j+1)+i*5-1
        assert v1.value == 39
        assert current() == 8
        backtrack(6)
        assert v1.value == 29
        assert current() == 6
        backtrack(4)
        assert v1.value == 19
        assert current() == 4
        backtrack(0)
        assert v1.value == 0
        assert current() == 0

    test1()
    reset()
    test2()
