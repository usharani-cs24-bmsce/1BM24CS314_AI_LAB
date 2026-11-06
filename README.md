# 1BM24CS314_AI_LAB

## AI Lab – Week 1

### 1. Tic-Tac-Toe Game

Tic-Tac-Toe is a two-player game played on a 3×3 grid between a Human and a Computer. The players use X and O to mark their respective cells. The objective is to get three marks in a horizontal row, column, or diagonal. The first player to achieve this wins. If all cells are filled and no player wins, the game ends in a draw.

This program implements the Tic-Tac-Toe game using the concept of a Game Tree, where each node represents a possible game state and each branch represents a player's move. This helps the computer choose its moves intelligently.

### 2. Vacuum Cleaner Agent

The Vacuum Cleaner Agent is a simple AI-based program that demonstrates how an intelligent agent works in an environment. It consists of two rooms, each of which may be clean or dirty, and a vacuum cleaner that can move between them.

The main goal of the agent is to clean both rooms. It senses the current room's condition, cleans it if it is dirty, and moves to the other room when necessary. The problem has eight possible states, based on the vacuum cleaner's location and the cleanliness of the two rooms.

This program demonstrates the working of a Goal-Based Agent, which takes actions to achieve a specific goal.

### AI Concepts Used

- **Game Tree:** Represents all possible game states and moves in Tic-Tac-Toe.
- **Goal-Based Agent:** Takes actions to achieve a specific goal, such as cleaning both rooms.

### Conclusion

This lab demonstrates basic Artificial Intelligence concepts through the implementation of a Tic-Tac-Toe game using Game Tree concepts and a Vacuum Cleaner Agent using Goal-Based Agent concepts.

---

## AI Lab – Week 2

### 1. 8-Puzzle Problem Using Depth First Search (DFS)

The 8-Puzzle is a sliding puzzle consisting of a 3×3 board with eight numbered tiles and one blank space. The objective is to rearrange the tiles from the initial state to the specified goal state by sliding adjacent tiles into the blank space.

This program solves the 8-Puzzle problem using Depth First Search (DFS). DFS explores one path completely before backtracking and exploring other possible paths. It uses a search tree where each node represents a puzzle state and each branch represents a possible move.

### 2. Iterative Deepening Search (IDS)

Iterative Deepening Search (IDS), also known as Iterative Deepening Depth First Search (IDDFS), is a search algorithm that combines the advantages of Depth First Search (DFS) and Breadth First Search (BFS).

IDS repeatedly performs DFS with increasing depth limits until the goal state is found. It first searches at depth 0, then depth 1, depth 2, and continues until the solution is reached.

This algorithm provides the memory efficiency of DFS while finding the shallowest solution like BFS (when all moves have equal cost).

### 3. 8-Puzzle Problem Using Iterative Deepening Search

In this implementation, the 8-Puzzle problem is solved using the IDS algorithm. The algorithm explores different puzzle states by moving the blank space up, down, left, or right.

At each iteration, the depth limit is increased until the goal state is reached. This helps find a solution while avoiding unnecessary deep searches.

### AI Concepts Used

- **Depth First Search (DFS):** Explores one path completely before backtracking.
- **Breadth First Search (BFS):** Explores all neighboring states level by level.
- **Iterative Deepening Search (IDS):** Combines DFS with increasing depth limits to find the goal state.

### Conclusion

This lab demonstrates different search techniques in Artificial Intelligence by solving the 8-Puzzle problem using DFS and Iterative Deepening Search (IDS).

---

## AI Lab – Week 3

### 1. 8-Puzzle Problem Using A* Search Algorithm

The 8-Puzzle is a sliding puzzle consisting of a 3×3 board with eight numbered tiles and one blank space. The objective is to rearrange the tiles from the initial state to the specified goal state by sliding adjacent tiles into the blank space.

This program implements the A* Search Algorithm to solve the 8-Puzzle problem. A* is an informed search algorithm that finds an optimal path by evaluating the cost of reaching a state and the estimated cost of reaching the goal state.

The evaluation function is:

**f(n) = g(n) + h(n)**

Where:

- **g(n):** Actual cost or depth of the node from the initial state.
- **h(n):** Estimated cost from the current state to the goal state.
- **f(n):** Total estimated cost of the solution path.

### 2. Heuristic Functions

A* Search uses heuristic functions to estimate how close the current state is to the goal state.

#### Case 1: Number of Tiles Out of Place

In this heuristic, the number of tiles that are not in their correct positions compared to the goal state is counted. The blank space is not included in the calculation.

**Heuristic Function:**

h(n) = Number of misplaced tiles

#### Case 2: Manhattan Distance Heuristic

The Manhattan Distance heuristic calculates the total distance of each tile from its correct position in the goal state. The distance is measured by adding the horizontal and vertical differences.

**Heuristic Function:**

h(n) = Σ (|Current Row - Goal Row| + |Current Column - Goal Column|)

The blank space is excluded from the calculation.

### AI Concepts Used

- **A* Search Algorithm:** An informed search algorithm that finds an optimal solution using path cost and heuristic cost.
- **Misplaced Tiles Heuristic:** Calculates the number of tiles that are not in their correct positions.
- **Manhattan Distance Heuristic:** Calculates the total distance of misplaced tiles from their goal positions.

### Conclusion

This lab demonstrates the implementation of the A* Search Algorithm to solve the 8-Puzzle problem using two different heuristic functions: Number of Tiles Out of Place and Manhattan Distance. It helps understand how heuristic-based search algorithms efficiently find solutions to AI problems.

---

## AI Lab – Week 4

### 1. N-Queens Problem Using Hill Climbing Search Algorithm

The N-Queens problem is a classic Artificial Intelligence problem in which N queens must be placed on an N×N chessboard such that no two queens attack each other.

In this implementation, the 4-Queens Problem is considered, where four queens must be placed on a 4×4 chessboard. No two queens should be in the same row, column, or diagonal.

### 2. Hill Climbing Search Algorithm

Hill Climbing is a local search algorithm that starts with an initial state and continuously moves towards a better neighboring state until the goal state is reached.

In this program, the Hill Climbing algorithm is used to solve the N-Queens problem by finding a configuration in which no two queens attack each other.

#### Working

- Start with an initial arrangement of queens on the chessboard.
- Calculate the cost of the current state.
- Generate neighboring states by changing the positions of queens.
- Calculate the cost of each neighboring state.
- Select a neighbor with a lower cost.
- Repeat the process until the cost becomes zero, indicating that no queens attack each other.

### 3. Cost Calculation

The cost function calculates the number of pairs of queens attacking each other. Queens attacking along rows, columns, or diagonals contribute to the total cost.

**Goal State:** The cost must be 0, which means no two queens attack each other.

### Observation

The observation includes the cost calculation of the initial state and its neighboring states. The process is repeated by selecting better neighboring states until the goal configuration is achieved.

### AI Concepts Used

- **Hill Climbing:** A local search algorithm that improves the current state by selecting better neighboring states.
- **N-Queens Problem:** A constraint satisfaction problem where no two queens should attack each other.
- **Heuristic / Cost Function:** Measures the number of attacking queen pairs to evaluate each state.

### Conclusion

This lab demonstrates the implementation of the Hill Climbing Search Algorithm to solve the 4-Queens problem. It helps understand local search techniques, heuristic-based cost calculations, and how an AI algorithm reaches a goal state by continuously improving the current configuration.

---

## AI Lab – Week 5

### 1. 8-Queens Problem Using Simulated Annealing

The 8-Queens problem is a classic Artificial Intelligence problem in which eight queens must be placed on an 8×8 chessboard such that no two queens attack each other. No two queens should be in the same row, column, or diagonal.

This program implements the Simulated Annealing Algorithm to solve the 8-Queens problem. Simulated Annealing is a probabilistic local search algorithm inspired by the cooling process of metals. It searches for an optimal solution by gradually improving the current state.

### 2. Simulated Annealing Algorithm

Simulated Annealing is an optimization technique that explores different possible states to find a solution. Unlike Hill Climbing, it can sometimes accept a worse neighboring state to avoid getting stuck in a local minimum.

#### Working

- Start with a random arrangement of eight queens on the chessboard.
- Calculate the cost of the current state.
- Generate a neighboring state by changing the position of a queen.
- Calculate the cost of the neighboring state.
- Accept the new state if it has a lower cost.
- Sometimes accept a worse state based on a probability determined by the temperature.
- Gradually decrease the temperature and continue searching until the goal state is reached or the stopping condition is met.

### 3. Cost Calculation

The cost function calculates the number of pairs of queens attacking each other along rows, columns, or diagonals.

**Goal State:** The cost must be 0, which means no two queens attack each other.

### AI Concepts Used

- **Simulated Annealing:** A probabilistic optimization algorithm used to find solutions by exploring neighboring states.
- **Local Search:** Searches for a solution by moving between neighboring states.
- **Heuristic / Cost Function:** Calculates the number of attacking queen pairs.
- **Temperature:** Controls the probability of accepting worse neighboring states and gradually decreases during the search.

# 1BM24CS314_AI_LAB

## AI Lab – Week 6

### 1. Knowledge Base Using Propositional Logic

Propositional Logic is a branch of Artificial Intelligence used to represent knowledge using logical statements that can have either True or False values. A Knowledge Base (KB) is created by combining multiple logical statements using operators such as AND, OR, NOT, and Implication.

In this program, three propositions (Q, P, and R) are used to construct a Knowledge Base consisting of the following statements:

- Q → P
- P → ¬Q
- Q ∨ R

The complete Knowledge Base is represented as:

**KB = (Q → P) ∧ (P → ¬Q) ∧ (Q ∨ R)**

### 2. Truth-Table Enumeration Algorithm

Truth-Table Enumeration is an algorithm used to determine whether a given query is logically entailed by a Knowledge Base. It generates all possible truth-value combinations of the propositions and evaluates each combination.

Since the program contains three propositions (Q, P, and R), the total number of possible combinations is:

**2³ = 8**

The program uses Python's `itertools.product()` function to generate all eight combinations. It evaluates the individual logical statements, constructs the complete Knowledge Base, and generates a truth table.

### 3. Checking Logical Entailment

Logical Entailment determines whether a query is guaranteed to be true whenever the Knowledge Base is true.

It is represented as:

**KB ⊨ Query**

The program evaluates the following three queries:

1. **Query 1:** R
2. **Query 2:** R → P
3. **Query 3:** Q → R

The entailment algorithm checks whether any truth assignment exists where the Knowledge Base is True but the selected query is False.

- If such an assignment exists, the query is not entailed.
- Otherwise, the Knowledge Base entails the query.

### AI Concepts Used

- **Propositional Logic:** Represents statements using True and False values.
- **Knowledge Base:** Stores logical facts and rules used for reasoning.
- **Logical Operators:** Uses AND, OR, NOT, and Implication to construct logical expressions.
- **Truth Table:** Represents all possible truth-value combinations of propositions.
- **Truth-Table Enumeration:** Checks every possible assignment to determine logical entailment.
- **Logical Entailment:** Determines whether a query logically follows from the Knowledge Base.
- **Model:** A truth assignment that satisfies the complete Knowledge Base.
- **Counterexample:** A model where the Knowledge Base is True but the query is False.

### Complexity Analysis

- **Time Complexity:** O(2ⁿ × m), where n is the number of propositions and m is the size of the Knowledge Base.
- **Space Complexity:** O(n + m) auxiliary space for the iterator-based implementation.

### Conclusion

This lab demonstrates the implementation of a Knowledge Base using Propositional Logic and the Truth-Table Enumeration algorithm in Python. All possible truth-value combinations are generated and evaluated to determine whether the given queries are logically entailed by the Knowledge Base.

The final results are:

- **KB entails R:** True
- **KB entails R → P:** False
- **KB entails Q → R:** True

Thus, the experiment successfully demonstrates how Artificial Intelligence uses logical reasoning and truth-table enumeration to represent knowledge and verify conclusions.

### Conclusion

This lab demonstrates the implementation of the Simulated Annealing Algorithm to solve the 8-Queens problem. It helps understand probabilistic search, optimization techniques, and how temperature-based exploration helps overcome local minima.
