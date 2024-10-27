from DFA_impl import DFA
from NFA_impl import NFA

def NFA2DFA(nfa: NFA) -> DFA:
    n = nfa.n
    m = nfa.m
    dfa = DFA(1 << n, m)
    dfa.set_start(sum([(1 << i) for i in nfa.start]))
    for i in range(1 << n):
        for val in range(m):
            cup = [0 for i in range(n)]
            for j in range(n):
                if i & (1 << j) > 0:
                    for can in list(nfa.transitions[j][val]):
                        cup[can] = 1
            final = 0
            for ii in range(n):
                final += (1 << ii) * cup[ii]
            dfa.add_transition(i, final, val)
    list_accepted = []
    for i in range(1 << n):
        for j in range(n):
            if (i & (1 << j) > 0) and (nfa.accepted[j] == True):
                list_accepted.append(i)
    lst = []
    for i in range(1 << n):
        lst.append(i in list_accepted)
    dfa.set_accepted(lst)
    return dfa



