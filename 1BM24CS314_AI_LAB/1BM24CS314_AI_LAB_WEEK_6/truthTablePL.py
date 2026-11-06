from itertools import product

# Evaluating function for Q -> P
def evaluate_1(Q, P):
    return (not Q) or P

# Evaluating function for P -> not Q
def evaluate_2(P, Q):
    return (not P) or (not Q)

# Evaluating function for Q OR R
def evaluate_3(Q, R):
    return Q or R

# Evaluating the complete Knowledge Base
def evaluate_kb(Q, P, R):
    return evaluate_1(Q, P) and evaluate_2(P, Q) and evaluate_3(Q, R)

# Evaluating queries
def evaluate_query(Q, P, R):
    return R, ((not R) or P), ((not Q) or R)


print("Q\tP\tR\tQ->P\tP->!Q\tQ|R\tKB\tR\tR->P\tQ->R")

for Q, P, R in product([True, False], repeat=3):

    a = evaluate_1(Q, P)
    b = evaluate_2(P, Q)
    c = evaluate_3(Q, R)

    kb = evaluate_kb(Q, P, R)

    q1, q2, q3 = evaluate_query(Q, P, R)

    print(Q, P, R, a, b, c, kb, q1, q2, q3, sep="\t")


# Check entailment
def entails(query_number):

    for Q, P, R in product([True, False], repeat=3):

        kb = evaluate_kb(Q, P, R)
        queries = evaluate_query(Q, P, R)

        if kb and not queries[query_number]:
            return False

    return True


print("\nKB entails R:", entails(0))
print("KB entails R -> P:", entails(1))
print("KB entails Q -> R:", entails(2))
