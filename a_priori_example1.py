from itertools import combinations

trays = [['Pizza', 'Milk'], ['Pizza', 'Milk', 'Apple'], ['Burger', 'Coke'], ['Pizza', 'Milk'], ['Burger', 'Coke', 'Fries']]

def cafeteria_apriori(data, min_support):
    counts = {}
    for t in data:
        for pair in combinations(sorted(t), 2):
            counts[pair] = counts.get(pair, 0) + 1
    
    print("--- [ANALYSIS: CAFETERIA BUNDLES] ---")
    for (a, b), count in counts.items():
        if count >= min_support:
            support_pct = (count / len(data)) * 100
            print(f"FOUND PATTERN: {a} + {b}")
            print(f" - Frequency: {count} trays")
            print(f" - Support: {support_pct:.1f}%")
            print(f" - RECOMMENDATION: Create a '{a}-{b} Special Combo'.\n")

cafeteria_apriori(trays, 2)