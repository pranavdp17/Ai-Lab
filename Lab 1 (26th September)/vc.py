import random

rooms = [random.choice(["dirty", "clean", "obstacle"]) for _ in range(10)]

# Make sure there is at least one dirty room
if "dirty" not in rooms:
    rooms[random.randint(0, 9)] = "dirty"

# Make sure there is at least one obstacle
if "obstacle" not in rooms:
    rooms[random.randint(0, 9)] = "obstacle"

# Choose a starting position
pos = random.randint(0, 9)

while rooms[pos] == "obstacle":
    pos = random.randint(0, 9)

print("Rooms:", rooms)
print("Vacuum starts at:", pos)


def clean_rooms(rooms, pos):
    rooms = rooms.copy()

    print("\nCleaning started...")

    # Move towards right
    for i in range(pos, 10):
        if rooms[i] == "obstacle":
            print("Obstacle found at", i)
            break

        if rooms[i] == "dirty":
            print("Cleaning room", i)
            rooms[i] = "clean"
        else:
            print("Room", i, "is already clean")

    # Move towards left
    for i in range(pos - 1, -1, -1):
        if rooms[i] == "obstacle":
            print("Obstacle found at", i)
            break

        if rooms[i] == "dirty":
            print("Cleaning room", i)
            rooms[i] = "clean"
        else:
            print("Room", i, "is already clean")

    return rooms


final_rooms = clean_rooms(rooms, pos)

print("\nBefore cleaning:", rooms)
print("After cleaning: ", final_rooms)

if "dirty" not in final_rooms:
    print("All rooms are clean!")
else:
    print("Some rooms are still dirty.")