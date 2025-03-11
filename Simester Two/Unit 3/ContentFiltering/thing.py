import pandas as pd
import pickle
import re

def save_pickle(file, value):
    pickle.dump(value, open(file, "wb"))
def load_pickle(file):
    return pickle.load(open(file, "rb"))
def remove_garbage(strng):
    return re.sub(r'\d+', "", strng.replace(",", "").replace("-", " ").replace("?", "").replace("!", "").replace(".", ""))


df = pd.read_csv("Simester Two/Unit 3/ContentFiltering/data/prompt_db.csv")
df = df[df['image_nsfw'] >= .9]
#df.truncate(after='20000', inplace=True)

prompts = []

print("starting")

promptDict = df.to_dict()['prompt']
count = len(promptDict)
errCount = 0
prompt_nsfw = df.to_dict()['prompt_nsfw']


for prompt in promptDict:
    try:
        prompts.append(remove_garbage(promptDict[prompt]).split(" "))
    except:
        errCount += 1
    print("Status: " + str(prompt) + "/" + str(count) + " Errors: " + str(errCount), end="\r")

print("\nSaving with " + str(len(prompts)) + " rows")
save_pickle("Simester Two/Unit 3/ContentFiltering/data/prompts.p", prompts)