
import random
import math

N = 8


# Calculate the number of attacking queen pairs
def calculate_cost(state):
    conflicts = 0

    for i in range(N):
        for j in range(i + 1, N):
            if abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1

    return conflicts


# Generate a random neighboring state
def get_neighbor(state):
    neighbor = state.copy()

    col = random.randint(0, N - 1)
    new_row = random.randint(0, N - 1)

    while new_row == neighbor[col]:
        new_row = random.randint(0, N - 1)

    neighbor[col] = new_row
    return neighbor


# Display the chessboard
def print_board(state):
    print("  " + " ".join(str(i + 1) for i in range(N)))

    for row in range(N):
        print(str(row + 1) + " ", end="")

        for col in range(N):
            if state[col] == row:
                print("Q ", end="")
            else:
                print(". ", end="")

        print()

    print("Cost:", calculate_cost(state))
    print("-" * 25)


# Simulated Annealing algorithm
def simulated_annealing():
    current = [random.randint(0, N - 1) for _ in range(N)]

    T = 100.0
    cooling_rate = 0.95
    min_temperature = 0.01
    iteration = 0

    print("\nINITIAL STATE")
    print_board(current)

    while T > min_temperature:
        next_state = get_neighbor(current)

        current_cost = calculate_cost(current)
        next_cost = calculate_cost(next_state)

        delta_E = current_cost - next_cost

        # Accept a better state
        if delta_E > 0:
            current = next_state

        # Accept a worse or equal state probabilistically
        else:
            probability = math.exp(delta_E / T)

            if random.random() < probability:
                current = next_state

        iteration += 1

        print(
            f"\nIteration: {iteration} | "
            f"Temperature: {T:.2f}"
        )
        print_board(current)

        # Stop when all queens are safe
        if calculate_cost(current) == 0:
            print("\nSOLUTION FOUND!")
            return current

        # Cool down
        T *= cooling_rate

    print("\nTemperature reached minimum.")

    return current


# Main program
if __name__ == "__main__":
    print("SIMULATED ANNEALING - 8 QUEENS PROBLEM")

    solution = simulated_annealing()

    print("\nFINAL CHESSBOARD")
    print_board(solution)

    if calculate_cost(solution) == 0:
        print("SUCCESS: All 8 queens are placed safely!")
    else:
        print("No solution found in this run. Run the program again.")
