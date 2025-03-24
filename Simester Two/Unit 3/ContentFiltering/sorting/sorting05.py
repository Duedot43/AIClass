import pandas as pd
import pickle
import re
import seaborn as sb
import re

def save_pickle(file, value):
    pickle.dump(value, open(file, "wb"))
def load_pickle(file):
    return pickle.load(open(file, "rb"))
def remove_garbage(strng):
    return re.sub(r'[^a-zA-Z0-9 ]', '', strng)


df = pd.read_csv("Simester Two/Unit 3/ContentFiltering/data/prompt_db.csv")
df = df[df['image_nsfw'] <= .05]
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


# COUNT THE WORDS

uselessWords = open("Simester Two/Unit 3/ContentFiltering/data/most_words.txt", "r").read()


words = {"word": [], "count": []}

print("counting...")

scentinces = 0
for scentince in prompts:
    for word in scentince:
        if word not in words['word']:
            words['word'].append(word)
            words['count'].append(1)
        
        index = words['word'].index(word)

        words['count'][index] += 1
    scentinces += 1
    print(str(scentinces) + "/" + str(len(prompts)) + " " + str(int((scentinces/len(prompts))*100)) + "%", end="\r")

words = pd.DataFrame(words)
print()

# GRAPH IT AND SORT IT

print("sorting")
for x in range(words.count()['count']):
    words.at[x, 'word'] = words.loc[x]['word'].lower()
    if (words.loc[x]['word'] in uselessWords and len(words.loc[x]['word']) <= 2):
        words.drop(index=x, inplace=True)

print("saving")

save_pickle("Simester Two/Unit 3/ContentFiltering/data/dot05_nsfw_words.p", words)
words.to_csv("Simester Two/Unit 3/ContentFiltering/data/dot05_nsfw_words.csv")

#sb.barplot(data=pd.DataFrame(words), x='word', y='count')

