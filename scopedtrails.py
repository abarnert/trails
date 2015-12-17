class VarSet:
    def __init__(self):
        self._trail = [[]]
        self._vars = {}
    def push(self):
        self._trail.append([])
    def back(self):
        for var, oldval, newval in reversed(self._trail.pop(-1)):
            if oldval is not None:
                self._vars[var] = oldval
            else:
                del self._vars[var]
    def backtrack(self, n):
        while self.current() > n:
            self.back()
    def current(self):
        return len(self._trail)-1
    def reset(self):
        self._trail[:] = [[]]
    def __getattr__(self, name):
        if name.startswith('_'):
            return super().__getattr__(name)
        return self._vars[name]
    def __setattr__(self, name, value):
        if name.startswith('_'):
            return super().__setattr__(name, value)
        self._trail[-1].append((name, self._vars.get(name, None), value))
        self._vars[name] = value
    def __delattr__(self, name):
        self._trail[-1].append((name, self._vars.get(name, None), None))
        del self._vars[name]

if __name__ == '__main__':
    def test1():
        v = VarSet()
        v.v1 = 10
        assert v.v1 == 10
        v.push()
        v.v1 = 100
        assert v.v1 == 100

    def test2():
        v = VarSet()
        v.v1 = 0
        for i in range(8):
            v.push()
            for j in range(5):
                v.v1 = (j+1)+i*5-1
        assert v.v1 == 39
        assert v.current() == 8
        v.backtrack(6)
        assert v.v1 == 29
        assert v.current() == 6
        v.backtrack(4)
        assert v.v1 == 19
        assert v.current() == 4
        v.backtrack(0)
        assert v.v1 == 0
        assert v.current() == 0

    test1()
    test2()
