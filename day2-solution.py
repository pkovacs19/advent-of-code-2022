import pandas as pd

shapes = {"A": "rock", "B": "paper", "C": "scissors", "X": "rock", "Y": "paper", "Z": "scissors"}
shape_points = {"rock": 1, "paper": 2, "scissors": 3}
outcome_points = {
    "rock-v-rock": 3, 
    "rock-v-paper": 0, 
    "rock-v-scissors": 6,
    "paper-v-rock": 6,
    "paper-v-paper": 3,
    "paper-v-scissors": 0,
    "scissors-v-rock": 0,
    "scissors-v-paper": 6,
    "scissors-v-scissors": 3
    }
total_score = 0
df = pd.read_csv('data/day2-input', header=None, sep=' ', names=["opponent", "me"])

for _, row in df.iterrows():
    myplay = shapes[row["me"]]
    opponent = shapes[row["opponent"]]
    
    game = f"{myplay}-v-{opponent}"
    
    score = shape_points[myplay] + outcome_points[game]
    total_score = total_score + score
print(total_score)


df = pd.read_csv('data/day2-input', header=None, sep=' ', names=["opponent", "outcome"])

choices = ("rock", "paper", "scissors")
encoded_outcomes = {"X": -1, "Y": 0, "Z": 1}
encoded_choices = {"A": 0, "B": 1, "C": 2}
outcome_points = {"X": 0, "Y": 3, "Z": 6}
total_score = 0
for _, row in df.iterrows():
    myplay = choices[(encoded_choices[row['opponent']] + encoded_outcomes[row['outcome']])%3]
    total_score += outcome_points[row['outcome']] + shape_points[myplay]

print(total_score)