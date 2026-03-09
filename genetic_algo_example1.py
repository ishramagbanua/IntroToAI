import random
# 1 = Play, 0 = Rest (Target Schedule)
TARGET = [1, 1, 0, 1, 0, 1, 1]

def get_fitness(s):
    return sum(1 for i in range(len(TARGET)) if s[i] == TARGET[i])

pop = [[random.randint(0, 1) for _ in range(7)] for _ in range(20)]

print("--- [EVOLUTION: SPORTS SCHEDULER] ---")
for gen in range(1, 101):
    pop = sorted(pop, key=get_fitness, reverse=True)
    score = get_fitness(pop[0])
    
    if gen % 5 == 0 or score == 7:
        print(f"Generation {gen:02d} | Fitness: {score}/7 | Best: {pop[0]}")
    
    if score == 7:
        print("\nOPTIMIZATION COMPLETE: Conflict-free schedule found.")
        break
    
    # Selection and Mutation
    pop[10:] = [[random.randint(0, 1) for _ in range(7)] for _ in range(10)]