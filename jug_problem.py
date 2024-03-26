from collections import deque

class State:
    def __init__(self, jug1, jug2):
        self.jug1 = jug1
        self.jug2 = jug2

    def __eq__(self, other):
        return self.jug1 == other.jug1 and self.jug2 == other.jug2

    def __hash__(self):
        return hash((self.jug1, self.jug2))

def get_possible_moves(state, max_capacity):
    moves = []
    # Fill jug1
    moves.append(State(max_capacity, state.jug2))
    # Fill jug2
    moves.append(State(state.jug1, max_capacity))
    # Empty jug1
    moves.append(State(0, state.jug2))
    # Empty jug2
    moves.append(State(state.jug1, 0))
    # Pour from jug1 to jug2
    pour_amount = min(state.jug1, max_capacity - state.jug2)
    moves.append(State(state.jug1 - pour_amount, state.jug2 + pour_amount))
    # Pour from jug2 to jug1
    pour_amount = min(state.jug2, max_capacity - state.jug1)
    moves.append(State(state.jug1 + pour_amount, state.jug2 - pour_amount))
    return moves

def solve_jug_problem(jug1_capacity, jug2_capacity, target_amount):
    max_capacity = max(jug1_capacity, jug2_capacity)
    start_state = State(0, 0)
    visited = set()
    queue = deque([(start_state, [])])

    while queue:
        current_state, path = queue.popleft()
        if current_state.jug1 == target_amount or current_state.jug2 == target_amount:
            return path
        visited.add(current_state)
        for move in get_possible_moves(current_state, max_capacity):
            if move not in visited:
                queue.append((move, path + [move]))

    return None

def main():
    jug1_capacity = 4
    jug2_capacity = 3
    target_amount = 2
    solution = solve_jug_problem(jug1_capacity, jug2_capacity, target_amount)
    if solution:
        print("Solution found:")
        for i, state in enumerate(solution):
            print(f"Step {i + 1}: Jug1={state.jug1}, Jug2={state.jug2}")
    else:
        print("No solution found")

if __name__ == "__main__":
    main()