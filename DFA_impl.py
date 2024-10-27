class DFA:
    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.accepted = [False for i in range(n)]
        self.transitions = [[-1 for j in range(m)] for i in range(n)]
        self.start = -1

    def add_transition(self, _from: int, _to: int, symbol: int) -> None:
        assert 0 <= _from < self.n and 0 <= _to < self.n and 0 <= symbol < self.m
        self.transitions[_from][symbol] = _to

    def set_accepted(self, accepted_list):
        for i in range(self.n):
            self.accepted[i] = accepted_list[i]

    def set_start(self, _start: int) -> None:
        assert 0 <= _start < self.n
        self.start = _start

    def execute(self, array):
        assert self.start != -1
        current: int = self.start
        for val in array:
            if self.transitions[current][val] == -1:
                return False
            current = self.transitions[current][val]
        return self.accepted[current]

