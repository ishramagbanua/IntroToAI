from itertools import combinations

records = [['Gatsby', '1984'], ['Gatsby', '1984', 'Hamlet'], ['1984', 'Macbeth'], ['Gatsby', '1984']]

def library_apriori(data, min_support):
    counts = {}
    for t in data:
        for pair in combinations(sorted(t), 2):
            counts[pair] = counts.get(pair, 0) + 1
    
    print("--- [ANALYSIS: LIBRARY RECOMMENDATIONS] ---")
    for (book1, book2), count in counts.items():
        if count >= min_support:
            print(f"PAIRING: {book1} & {book2}")
            print(f" - Common Borrowers: {count}")
            print(f" - RULE: If a student borrows {book1}, suggest {book2}.\n")

library_apriori(records, 2)