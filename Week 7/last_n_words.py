import numpy as np

# Trump's speeches here: https://github.com/ryanmcdermott/trump-speeches
trump = open('speeches.txt', encoding='utf8').read()

corpus = trump.split()

n = 3


def make_n(corpus, n):
    for i in range(len(corpus)-n):
        yield tuple(corpus[i+j] for j in range(n+1))

word_groups = make_n(corpus, n)

word_dict = {}


for words in word_groups:
    if words[:-1] in word_dict.keys():
        word_dict[words[:-1]].append(words[-1])
    else:
        word_dict[words[:-1]] = [words[-1]]


# generate text
i = np.random.randint(0, len(corpus)-n)


chain = [corpus[i+j] for j in range(n)]

n_words = 800 + n

for i in range(n_words):
    chain.append(
            np.random.choice(
                word_dict[tuple(chain[-n:])]
            )
    )

chain = chain[n:]

result = ' '.join(chain)

print(result)
