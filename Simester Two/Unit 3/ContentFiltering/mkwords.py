import pandas as pd
import pickle

def save_pickle(file, value):
    pickle.dump(value, open(file, "wb"))
def load_pickle(file):
    return pickle.load(open(file, "rb"))

prompts = load_pickle("Simester Two/Unit 3/ContentFiltering/data/prompts.p")
uselessWords = open("Simester Two/Unit 3/ContentFiltering/data/most_words.txt", "r").read()


words = {"word": [], "count": []}

print("counting...")

scentinces = 0
for scentince in prompts:
    for word in scentince:
        if word not in words['word']:
            words['word'].append(word)
            words['count'].append(0)
        
        index = words['word'].index(word)

        words['count'][index] += 1
    scentinces += 1
    print(str(scentinces) + "/" + str(len(prompts)) + " " + str(int((scentinces/len(prompts))*100)) + "%", end="\r")

words = pd.DataFrame(words)
save_pickle("Simester Two/Unit 3/ContentFiltering/data/words.p", words)