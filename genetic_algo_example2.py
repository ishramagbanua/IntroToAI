import random
# 1 = Right, 0 = Left
OPTIMAL_LINE = [1, 0, 1, 1, 1, 0]

def ai_fitness(m):
    return sum(1 for i in range(len(OPTIMAL_LINE)) if m[i] == OPTIMAL_LINE[i])

pop = [[random.randint(0, 1) for _ in range(6)] for _ in range(20)]

print("--- [EVOLUTION: RACING AI TRAINING] ---")
for gen in range(1, 101):
    pop = sorted(pop, key=ai_fitness, reverse=True)
    score = ai_fitness(pop[0])
    
    if gen % 5 == 0 or score == 6:
        print(f"Generation {gen:02d} | Lap Completion: {int(score/6*100)}% | DNA: {pop[0]}")
        
    if score == 6:
        print("\nSUCCESS: AI has learned the optimal racing line.")
        break
    pop[10:] = [[random.randint(0, 1) for _ in range(6)] for _ in range(10)]