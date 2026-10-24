
import heapq

def heuristic(state, goal):
    distance = 0

    for i in range(9):
        if state[i] != 0:
            goal_pos = goal.index(state[i])

            r1, c1 = i // 3, i % 3
            r2, c2 = goal_pos // 3, goal_pos % 3

            distance += abs(r1 - r2) + abs(c1 - c2)

    return distance

def get_neighbors(state):
    neighbors = []
    pos = state.index(0)
    row, col = pos // 3, pos % 3

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        r, c = row + dr, col + dc

        if 0 <= r < 3 and 0 <= c < 3:
            new_pos = r * 3 + c
            new_state = list(state)
            new_state[pos], new_state[new_pos] = (
                new_state[new_pos], new_state[pos]
            )
            neighbors.append(tuple(new_state))

    return neighbors

def astar(start, goal):
    pq = [(heuristic(start, goal), 0, start, [start])]
    best_g = {start: 0}

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if g != best_g[state]:
            continue

        if state == goal:
            return path

        for next_state in get_neighbors(state):
            new_g = g + 1

            if new_g < best_g.get(next_state, float('inf')):
                best_g[next_state] = new_g
                h = heuristic(next_state, goal)
                heapq.heappush(pq, (
                    new_g + h, new_g, next_state,
                    path + [next_state]
                ))

    return None

def read_state():
    state = []
    for i in range(3):
        row = list(map(int, input().split()))
        state.extend(row)
    return tuple(state)

print("Enter Initial State (0 for blank):")
start = read_state()

print("Enter Goal State (0 for blank):")
goal = read_state()

if sorted(start) != list(range(9)) or sorted(goal) != list(range(9)):
    print("Invalid puzzle! Use numbers 0 to 8 exactly once.")
else:
    path = astar(start, goal)

    if path:
        for g, state in enumerate(path):
            h = heuristic(state, goal)
            print(f"\nStep {g}: g={g}, h={h}, f={g+h}")

            for i in range(0, 9, 3):
                print(*state[i:i+3])

        print("\nTotal Moves:", len(path) - 1)
    else:
        print("No solution found")
