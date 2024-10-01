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

class TestStringMethods(unittest.TestCase):
    def test_DFA1(self):
        self.assertEqual(ExecuteDFA("DFA_test1")[1], True)
    def test_DFA2(self):
        self.assertEqual(ExecuteDFA("DFA_test2")[1], False)
    def test_NFA1(self):
        self.assertEqual(ExecuteNFA("NFA_test1")[1], True)
    def test_NFA2(self):
        self.assertEqual(ExecuteNFA("NFA_test2")[1], False)
    def test_NFAtoDFA1(self):
        nfa, result = ExecuteNFA("NFA_test1")
        file = open("NFA_test1", "r+")
        dfa = NFA2DFA(nfa)
        self.assertEqual(result, dfa.execute(list(map(int, file.readlines()[-1].split()))))
    def test_NFAtoDFA2(self):
        nfa, result = ExecuteNFA("NFA_test2")
        file = open("NFA_test2", "r+")
        dfa = NFA2DFA(nfa)
        self.assertEqual(result, dfa.execute(list(map(int, file.readlines()[-1].split()))))
    def test_public(self):
        dfa = DFA(3, 2)
        dfa.set_start(0)
        dfa.set_accepted([2])
        dfa.add_transition(0, 1, 0)
        dfa.add_transition(1, 2, 0)
        dfa.add_transition(2, 0, 0)
        self.assertEqual(dfa.execute([0, 0, 0, 0, 0]), True)



if __name__ == '__main__':
    unittest.main()