import numpy as np

# Trump's speeches here: https://github.com/ryanmcdermott/trump-speeches
trump = open('speeches.txt', encoding='utf8').read()

corpus = trump.split()

def make_trios(corpus):
    for i in range(len(corpus)-2):
        yield (corpus[i], corpus[i+1], corpus[i+2])

trios = make_trios(corpus)

word_dict = {}


for word_1, word_2, word_3 in trios:
    if (word_1, word_2) in word_dict.keys():
        word_dict[(word_1, word_2)].append(word_3)
    else:
        word_dict[(word_1, word_2)] = [word_3]


# generate text
i = np.random.randint(0, len(corpus)-2)


chain = [corpus[i], corpus[i+1]]

n_words = 800

for i in range(n_words):
    chain.append(np.random.choice(word_dict[(chain[-2], chain[-1])]))

result = ' '.join(chain)

print(result)
