import unittest
from DFA_impl import DFA
from NFA_impl import NFA
from nfa2dfa import NFA2DFA


def ExecuteDFA(filename): # returns dfa, result
    file = open(filename, "r+")
    lines = file.readlines()
    n = int(lines[0].strip())
    m = int(lines[1].strip())
    q = int(lines[2].strip())
    dfa = DFA(n, m)
    start = int(lines[3].strip())
    accepted = list(map(int, lines[4].strip()))
    dfa.set_start(start)
    dfa.set_accepted(accepted)
    for i in range(q):
        f, t, val = map(int, lines[5 + i].strip().split())
        dfa.add_transition(f, t, val)
    file.close()
    return dfa, dfa.execute(list(map(int, lines[-1].strip().split())))

def ExecuteNFA(filename): #returns nfa, result
    file = open(filename, "r+")
    lines = file.readlines()
    n = int(lines[0].strip())
    m = int(lines[1].strip())
    q = int(lines[2].strip())
    nfa = NFA(n, m)
    start = list(map(int, lines[3].strip().split()))
    accepted = list(map(int, lines[4].strip()))
    nfa.set_start(start)
    nfa.set_accepted(accepted)
    for i in range(q):
        f, t, val = map(int, lines[5 + i].strip().split())
        nfa.add_transition(f, t, val)
    file.close()
    return nfa, nfa.execute(list(map(int, lines[-1].strip().split())))




def createDFA(n: int, m: int, start: int, accepted: [bool], transitions) -> DFA:
    dfa = DFA(n, m)
    dfa.set_start(start)
    dfa.set_accepted(accepted)
    for (u, v, w) in transitions:
        dfa.add_transition(u, v, w)
    return dfa

def createNFA(n: int, m: int, start: [], accepted: [bool], transitions) -> NFA:
    nfa = NFA(n, m)
    nfa.set_start(start)
    nfa.set_accepted(accepted)
    for (u, v, w) in transitions:
        nfa.add_transition(u, v, w)
    return nfa

import random

def gen_random_array(n: int, m: int):  # generates random array of n numbers in [0...m - 1]
    assert(n > 1)
    return [random.randint(0, m - 1) for _ in range(n)]


#Example
def MyTest():
    dfa = createDFA(3, 2, 0, [False, False, True], [(0, 1, 0), (1, 2, 0), (2, 0, 0)])
    assert(dfa.execute([0, 0]) == True)
    assert(dfa.execute([0, 0, 0, 0, 0]) == True)
    assert(dfa.execute([0, 1, 0]) == False)

    nfa = createNFA(3, 2, [0], [False, False, True], [(0, 1, 0), (1, 2, 0), (2, 0, 0)])
    assert(nfa.execute([0, 0]) == True)
    assert(nfa.execute([0, 0, 0, 0, 0]) == True)
    assert(nfa.execute([0, 1, 0]) == False)

    #nfa1 = createNFA(6, 2, [0, 1, 5], [False, True, True, False, False, True], [])
    nfa1 = createNFA(6, 4, [0, 1, 5], [False, False, True, False, False, False], [])
    for i in range(40):
        nfa1.add_transition(random.randint(0,  5), random.randint(0, 5), random.randint(0, 3))

    dfa1 = NFA2DFA(nfa1)


    for test in range(100):
        n = random.randint(5, 10)
        m = 3
        x = gen_random_array(n, m)
        assert(dfa1.execute(x) == nfa1.execute(x))





if __name__ == '__main__':
    MyTest()
    #unittest.main()