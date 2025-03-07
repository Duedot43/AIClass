import pandas as pd

df = pd.read_csv("Simester Two/Unit 3/ContentFiltering/data/prompt_db.csv")
df = df[df['prompt_nsfw'] <= 1.0]

prompts = []

print("starting")

for key, value in df.to_dict().items():
    prompts[key] = value.split(" ")