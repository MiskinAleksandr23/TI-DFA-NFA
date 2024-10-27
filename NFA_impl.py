class NFA:
    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.accepted = [False for i in range(n)]
        self.transitions = [[[] for j in range(m)] for i in range(n)]
        self.start = []

    def add_transition(self, _from: int, _to: int, symbol: int) -> None:
        assert 0 <= _from < self.n and 0 <= _to < self.n and 0 <= symbol < self.m
        self.transitions[_from][symbol].append(_to)

    def set_accepted(self, accepted_list):
        for i in range(self.n):
            self.accepted[i] = accepted_list[i]

    def set_start(self, start_list) -> None:
        assert(all([0 <= x < self.n for x in start_list]))
        self.start = start_list

    def execute(self, array):
        size = len(array)
        def dfs(current: int, index: int) -> bool:
            if index == size:
                return self.accepted[current]
            if len(self.transitions[current][array[index]]) == 0:
                return False
            for nxt in list(self.transitions[current][array[index]]):
                if dfs(nxt, index + 1): return True
            return False
        for start in self.start:
            if dfs(start, 0): return True
        return False
