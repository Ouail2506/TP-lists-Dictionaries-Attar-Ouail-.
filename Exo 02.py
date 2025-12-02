scores = {
    "Alice": 88,
    "Bob": 95,
    "Charlie": 90
}

HighestScore = max(scores, key=scores.get)

print(HighestScore)