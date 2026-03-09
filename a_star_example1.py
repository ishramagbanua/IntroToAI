import heapq

# 0 = Clear Hallway, 1 = Crowded Zone (Wall)
campus_grid = [
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

def a_star_campus(start, goal):
    queue, came_from, cost = [(0, start)], {start: None}, {start: 0}
    while queue:
        curr = heapq.heappop(queue)[1]
        if curr == goal: break
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            nb = (curr[0]+dx, curr[1]+dy)
            if 0 <= nb[0] < 5 and 0 <= nb[1] < 5 and campus_grid[nb[0]][nb[1]] == 0:
                new_cost = cost[curr] + 1
                if nb not in cost or new_cost < cost[nb]:
                    cost[nb] = new_cost
                    priority = new_cost + abs(goal[0]-nb[0]) + abs(goal[1]-nb[1])
                    heapq.heappush(queue, (priority, nb))
                    came_from[nb] = curr
    return came_from

# Generate and print detailed results
results = a_star_campus((0,0), (4,4))
path, curr = [], (4,4)
while curr:
    path.append(curr)
    curr = results.get(curr)
final_path = path[::-1]

print("--- [REPORT: CAMPUS NAVIGATOR] ---")
print(f"START: Gym (0,0) | GOAL: Science Lab (4,4)")
print(f"OPTIMAL ROUTE: {' -> '.join(map(str, final_path))}")
print(f"PATH EFFICIENCY: Found in {len(final_path)} coordinates.")