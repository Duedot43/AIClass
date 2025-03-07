import pandas as pd
import pickle

def save_pickle(file, value):
    pickle.dump(value, open(file, "wb"))
def load_pickle(file):
    return pickle.load(open(file, "rb"))


df = pd.read_csv("Simester Two/Unit 3/ContentFiltering/data/prompt_db.csv")
df = df[df['prompt_nsfw'] >= .7]

prompts = []

print("starting")

promptDict = df.to_dict()['prompt']
count = len(promptDict)
errCount = 0
prompt_nsfw = df.to_dict()['prompt_nsfw']


for prompt in promptDict:
    try:
        prompts.append(promptDict[prompt].split(" "))
    except:
        errCount += 1
    print("Status: " + str(prompt) + "/" + str(count) + " Errors: " + str(errCount), end="\r")

print("\nSaving with " + str(len(prompts)) + " rows")
save_pickle("Simester Two/Unit 3/ContentFiltering/data/prompts.p", prompts)