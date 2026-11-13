
def apply_substitution(term, subst):
    if isinstance(term, str):
        while term in subst:
            term = subst[term]
        return term

    if isinstance(term, tuple):
        return (term[0],) + tuple(
            apply_substitution(arg, subst)
            for arg in term[1:]
        )

    return term


def occurs_check(var, term, subst):
    term = apply_substitution(term, subst)

    if var == term:
        return True

    if isinstance(term, tuple):
        return any(
            occurs_check(var, arg, subst)
            for arg in term[1:]
        )

    return False


def unify(x, y, subst, step):
    x = apply_substitution(x, subst)
    y = apply_substitution(y, subst)

    step[0] += 1

    print(f"\nIteration {step[0]}:")
    print("Comparing:", x, "and", y)

    # Case 1: Identical expressions
    if x == y:
        print("Both expressions are identical.")
        return True

    # Case 2: First argument is a variable
    if isinstance(x, str) and x.islower():

        if occurs_check(x, y, subst):
            print("Occurs check failed!")
            print(f"{x} occurs inside {y}")
            return False

        subst[x] = y
        print(f"Substitution: {x} = {y}")
        print("Current substitution set:", subst)
        return True

    # Case 3: Second argument is a variable
    if isinstance(y, str) and y.islower():

        if occurs_check(y, x, subst):
            print("Occurs check failed!")
            print(f"{y} occurs inside {x}")
            return False

        subst[y] = x
        print(f"Substitution: {y} = {x}")
        print("Current substitution set:", subst)
        return True

    # Case 4: Both are compound expressions
    if isinstance(x, tuple) and isinstance(y, tuple):

        if x[0] != y[0]:
            print("FAILURE: Predicate/function symbols are different.")
            return False

        if len(x) != len(y):
            print("FAILURE: Number of arguments is different.")
            return False

        print("Symbols match. Checking arguments...")

        for i in range(1, len(x)):
            print(f"\nChecking argument {i}:")

            if not unify(x[i], y[i], subst, step):
                return False

        return True

    # Case 5: Different constants or incompatible terms
    print("FAILURE: Constants or terms do not match.")
    return False


def test_unification(expr1, expr2):

    print("\n" + "=" * 55)
    print("       UNIFICATION TEST")
    print("=" * 55)

    print("\nExpression 1:", expr1)
    print("Expression 2:", expr2)

    subst = {}
    step = [0]

    print("\n--- UNIFICATION PROCESS ---")

    result = unify(expr1, expr2, subst, step)

    print("\n--- FINAL RESULT ---")

    if result:
        print("UNIFICATION SUCCESSFUL!")

        print("Final Substitution Set:")

        for var, value in subst.items():
            print(f"{var} = {apply_substitution(value, subst)}")

        print("\nUnified Expression:")
        print(apply_substitution(expr1, subst))

    else:
        print("UNIFICATION FAILED!")
        print("No valid substitution exists.")

    print("\nTotal Iterations:", step[0])


# MAIN PROGRAM

print("UNIFICATION ALGORITHM")
print("=====================")

# Example 1: Successful Unification
test_unification(
    ("Eats", "x", "Apple"),
    ("Eats", "Riya", "y")
)

# Example 2: Predicate Symbol Mismatch
test_unification(
    ("P", "x", "a"),
    ("Q", "b", "y")
)

# Example 3: Different Number of Arguments
test_unification(
    ("P", "x", "y"),
    ("P", "a", "b", "c")
)

# Example 4: Occurs Check Failure
test_unification(
    ("P", "x"),
    ("P", ("f", "x"))
)

# Example 5: Constant Mismatch
test_unification(
    ("P", "a"),
    ("P", "b")
)

# Example 6: Conflicting Variable Substitution
test_unification(
    ("P", "x", "x"),
    ("P", "a", "b")
)
