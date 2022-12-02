
import pandas as pd

elf_dict = {}
calories = []
count = 0

with open('data/day1-input') as f:
    for line in f:
        if line == '\n':
            elf_dict[f"elf-{count}"] = calories
            count += 1
            calories=[]
        else:
            calories.append(int(line.strip('\n')))


df = pd.DataFrame.from_dict(elf_dict, orient='index')

cals_per_elf = df.sum(axis='columns')

top_carrier = cals_per_elf.max()

top_carriers = cals_per_elf.sort_values(ascending=False)[:3]

print(top_carriers.sum())