import copy

class PuzzleState:
    def __init__(self, board, parent=None, action=None, depth=0):
        self.board = board
        self.parent = parent
        self.action = action
        self.depth = depth
        self.empty_pos = self.find_empty()

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.board])

    def __eq__(self, other):
        if not isinstance(other, PuzzleState):
            return False
        return self.board == other.board

    def __hash__(self):
        return hash(str(self.board))

    def find_empty(self):
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == 0:
                    return r, c

    def get_neighbors(self):
        neighbors = []
        er, ec = self.empty_pos

        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

        for dr, dc in moves:
            new_er, new_ec = er + dr, ec + dc

            if 0 <= new_er < 3 and 0 <= new_ec < 3:
                new_board = copy.deepcopy(self.board)
                new_board[er][ec], new_board[new_er][new_ec] = new_board[new_er][new_ec], new_board[er][ec]
                neighbors.append(PuzzleState(new_board, self, (new_er, new_ec), self.depth + 1))
        return neighbors

    def is_goal(self, goal_board):
        return self.board == goal_board

def iterative_deepening_search(initial_board, goal_board):
    depth = 0
    while True:
        print(f"Trying depth limit: {depth}")
        result = depth_limited_search(initial_board, goal_board, depth)
        if result != "cutoff":
            return result
        depth += 1

def depth_limited_search(initial_board, goal_board, limit):
    initial_state = PuzzleState(initial_board)
    stack = [initial_state]
    visited = set()
    visited.add(initial_state)

    while stack:
        current_state = stack.pop()

        if current_state.is_goal(goal_board):
            return current_state  # Goal found

        if current_state.depth < limit:
            for neighbor in reversed(current_state.get_neighbors()):  # Reverse to explore in a consistent order
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
    
    # If the stack is empty and no goal found within the limit
    if not stack and current_state.depth >= limit and not current_state.is_goal(goal_board):
      return "cutoff"
    else:
      return "failure"

def reconstruct_path(state):
    path = []
    while state:
        path.append(state)
        state = state.parent
    return path[::-1]

# Example Usage:
initial_board = [
    [1, 2, 3],
    [4, 0, 5],
    [6, 7, 8]
]

goal_board = [
    [1, 2, 3],
    [4, 5, 0],
    [6, 7, 8]
]

solution_state = iterative_deepening_search(initial_board, goal_board)

if solution_state != "failure" and solution_state != "cutoff":
    path = reconstruct_path(solution_state)
    print(f"\nSolution Found at depth {solution_state.depth}!\n")
    
    # Print 2 steps per line side-by-side
    for idx in range(0, len(path), 2):
        left_idx = idx
        right_idx = idx + 1
        
        left_state = path[left_idx]
        right_state = path[right_idx] if right_idx < len(path) else None
        
        # Row labels
        print(f"  Step {left_idx:<15}" + (f"Step {right_idx}" if right_state else ""))
        for r in range(3):
            left_row = " ".join(map(str, left_state.board[r]))
            right_row = " ".join(map(str, right_state.board[r])) if right_state else ""
            print(f"  {left_row:<19} {right_row}")
        print()
else:
    print("\nNo solution found within the given depth limits.")