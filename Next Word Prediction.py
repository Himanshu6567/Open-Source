import numpy as np
lexicon = {}
def update_lexicon(current : str, next_word : str) -> None:
 # Add the input word to the lexicon if it in there yet.
 if current not in lexicon:
 lexicon.update({current: {next_word: 1} })
 return
 # Recieve te probabilties of the input word.
 options = lexicon[current]
 # Check if the output word is in the propability list.
 if next_word not in options:
 options.update({next_word : 1})
 else:
 options.update({next_word : options[next_word] + 1})
 # Update the lexicon
 lexicon[current] = options
So we created the function to fill the vocabulary of words, now let’s use this function on the 
dataset which will just split the sentences into words and select the last word of the sentence:
with open('dataset.txt', 'r') as dataset:
 for line in dataset:
 words = line.strip().split(' ')
 for i in range(len(words) - 1):
 update_lexicon(words[i], words[i+1])
Now we are ready to find the next predicted words:
for word, transition in lexicon.items():
 transition = dict((key, value / sum(transition.values())) for key, value in transition.items())
 lexicon[word] = transition
 
line = input('> ')
word = line.strip().split(' ')[-1]
if word not in lexicon:
 print('Word not found')
else:
 options = lexicon[word]
 predicted = np.random.choice(list(options.keys()), p=list(options.values()))
 print(line + ' ' + predicted)
The code above will take user input and find your input in the dataset, so to test your code, use 
the sentences that are familiar with the sentences written by you in the dataset. The code will find 
the next word and print it at the end of your input sentence.
This is how we can predict the next word with Python. Below is the complete code used in this 
article for the next word prediction task with Python.
import numpy as np
lexicon = {}
def update_lexicon(current : str, next_word : str) -> None:
 # Add the input word to the lexicon if it in there yet.
 if current not in lexicon:
 lexicon.update({current: {next_word: 1} })
 return
 # Recieve te probabilties of the input word.
 options = lexicon[current]
 # Check if the output word is in the propability list.
 if next_word not in options:
 options.update({next_word : 1})
 else:
 options.update({next_word : options[next_word] + 1})
 # Update the lexicon
 lexicon[current] = options
# Populate lexicon
with open('dataset.txt', 'r') as dataset:
 for line in dataset:
 words = line.strip().split(' ')
 for i in range(len(words) - 1):
 update_lexicon(words[i], words[i+1])
 
# Adjust propability
for word, transition in lexicon.items():
 transition = dict((key, value / sum(transition.values())) for key, value in transition.items())
 lexicon[word] = transition
# Predict next word
line = input('> ')
word = line.strip().split(' ')[-1]
if word not in lexicon:
 print('Word not found')
else:
 options = lexicon[word]
 predicted = np.random.choice(list(options.keys()), p=list(options.values()))
 print(line + ' ' + predicted)