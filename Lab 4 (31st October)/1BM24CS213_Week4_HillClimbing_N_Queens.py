import random

def calculate_heuristic(state):
    attacks = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j]:
                attacks += 1
            elif abs(state[i] - state[j]) == abs(i - j):
                attacks += 1
    return attacks


def get_best_neighbor(current_state):
    n = len(current_state)
    current_h = calculate_heuristic(current_state)
    best_state = list(current_state)
    best_h = current_h

    for col in range(n):
        original_row = current_state[col]
        for row in range(n):
            if row != original_row:
                neighbor = list(current_state)
                neighbor[col] = row
                neighbor_h = calculate_heuristic(neighbor)

                if neighbor_h < best_h:
                    best_h = neighbor_h
                    best_state = neighbor

    return best_state, best_h


def hill_climbing_4_queens():
    current_state = [random.randint(0, 3) for _ in range(4)]
    current_h = calculate_heuristic(current_state)

    step = 0
    print(f"Step {step}: Initial State = {current_state}, Attacking Pairs (h) = {current_h}")

    while True:
        best_neighbor, best_neighbor_h = get_best_neighbor(current_state)

        if best_neighbor_h >= current_h:
            break

        current_state = best_neighbor
        current_h = best_neighbor_h
        step += 1
        print(f"Step {step}: Moved to State = {current_state}, Attacking Pairs (h) = {current_h}")

    print("-" * 50)
    if current_h == 0:
        print(f"SUCCESS: Found Global Solution in {step} steps: {current_state}")
    else:
        print(f"STUCK IN LOCAL MINIMUM at state {current_state} with h = {current_h}")

    return current_state, current_h


def print_board(state):
    n = len(state)
    print("\nVisual Board Representation:")
    for row in range(n):
        line = ""
        for col in range(n):
            line += " Q " if state[col] == row else " . "
        print(line)


if __name__ == "__main__":
    final_state, final_h = hill_climbing_4_queens()