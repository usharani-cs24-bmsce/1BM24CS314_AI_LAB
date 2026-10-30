def cost(state):
    count = 0
    for i in range(4):
        for j in range(i + 1, 4):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                count += 1
    return count


def print_board(state):
    print("  0 1 2 3")
    for row in range(4):
        print(row, end=" ")
        for col in range(4):
            if state[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


def hill_climbing():
    current = [3, 1, 2, 0]  # Given initial state
    step = 0

    while True:
        current_cost = cost(current)

        print(f"\nSTEP {step}: CURRENT STATE")
        print("State:", current)
        print("Cost:", current_cost)
        print_board(current)

        if current_cost == 0:
            print("Goal reached!")
            break

        neighbours = []

        # Swap positions of every pair of queens
        for i in range(4):
            for j in range(i + 1, 4):
                neighbour = current.copy()
                neighbour[i], neighbour[j] = neighbour[j], neighbour[i]
                neighbour_cost = cost(neighbour)

                neighbours.append((neighbour_cost, i, j, neighbour))

                print(f"\nNeighbour: Swap columns ({i}, {j})")
                print("State:", neighbour)
                print("Cost:", neighbour_cost)
                print_board(neighbour)

        # Minimum cost; ties use the smallest column pair
        best = min(neighbours, key=lambda x: (x[0], x[1], x[2]))
        best_cost, i, j, best_state = best

        print(f"\nSelected neighbour: Swap ({i}, {j})")
        print("Selected cost:", best_cost)

        if best_cost >= current_cost:
            print("No better neighbour. Hill climbing terminates.")
            break

        current = best_state
        step += 1

    print("\nFINAL BOARD")
    print_board(current)
    print("Final cost:", cost(current))


hill_climbing()