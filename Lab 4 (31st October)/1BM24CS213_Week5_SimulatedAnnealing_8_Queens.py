import math
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


def get_random_neighbor(state):
    neighbor = list(state)
    col = random.randint(0, 7)
    current_row = state[col]
    new_row = random.choice([r for r in range(8) if r != current_row])
    neighbor[col] = new_row
    return neighbor


def simulated_annealing_8_queens(initial_temp=10.0, cooling_rate=0.995, min_temp=0.001, max_steps=100000):
    current_state = [random.randint(0, 7) for _ in range(8)]
    current_h = calculate_heuristic(current_state)

    temperature = initial_temp
    step = 0

    print(f"Initial State: {current_state} | Initial Conflicts (h): {current_h}\n")

    while temperature > min_temp and current_h > 0 and step < max_steps:
        neighbor_state = get_random_neighbor(current_state)
        neighbor_h = calculate_heuristic(neighbor_state)

        delta_h = neighbor_h - current_h

        if delta_h < 0:
            current_state = neighbor_state
            current_h = neighbor_h
        else:
            acceptance_prob = math.exp(-delta_h / temperature)
            if random.random() < acceptance_prob:
                current_state = neighbor_state
                current_h = neighbor_h

        temperature *= cooling_rate
        step += 1

    print("-" * 55)

    if current_h == 0:
        print(f"SUCCESS: Found solution in {step} iterations!")
    else:
        print(f"TERMINATED: Reached minimum temperature at step {step}.")

    print(f"Final State: {current_state}")
    print(f"Final Conflicts (h): {current_h}")

    return current_state, current_h


def print_board(state):
    n = len(state)
    print("\nVisual Board Representation:")
    print("┌───" + "┬───" * (n - 1) + "┐")

    for row in range(n):
        line = "│"
        for col in range(n):
            line += " Q │" if state[col] == row else "   │"
        print(line)

        if row < n - 1:
            print("├───" + "┼───" * (n - 1) + "┤")

    print("└───" + "┴───" * (n - 1) + "┘")


if __name__ == "__main__":
    solution_state, final_conflicts = simulated_annealing_8_queens()
    print_board(solution_state)