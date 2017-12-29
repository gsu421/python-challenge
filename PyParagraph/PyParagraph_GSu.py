
# coding: utf-8

# In[13]:


import os
import re


# In[20]:


file_to_load = os.path.join('raw_data/paragraph_2.txt')
file_to_write = os.path.join('analysis/paragraph_analysis.txt')

paragraph = ''
with open (file_to_load, newline='') as txt_data:
    paragraph = txt_data.read()
print(paragraph)


# In[15]:


# word count
word_split = paragraph.split(' ')
word_count = len(word_split)

# letter count
letter_count = []
for words in word_split:
    letter_count.append(len(words))

# Letter Count per Word
letter_count_per_word = sum(letter_count) / word_count


# In[17]:


# Sentence Count
sentence_split = re.split('(?<=[!.?]) +',paragraph) #this is tricky
sentence_count = len(sentence_split)
# print(sentence_split)
word_count_per_sentence = []

for words in sentence_split:
    word_count_per_sentence.append(len(words.split(' ')))
# print(word_count_per_sentence)
# Word Count per Sentence
avg_sentence_length = sum(word_count_per_sentence) / sentence_count


# In[18]:


print('Approximate word count: %s' %word_count)
print('Approximate sentence count: %s' %sentence_count)
print('Approximate letter count (per word): %s' %int(letter_count_per_word))
print('Average sentence length (in words): %s' %int(avg_sentence_length))


# In[19]:


# Generate Analysis Outputs
output = (
    f"\nParagraph Analysis\n"
    f"-----------------\n"
    f"Approximate Word Count: {word_count}\n"
    f"Approximate Sentence Count: {sentence_count}\n"
    f"Average Letter Count: {letter_count_per_word}\n"
    f"Average Sentence Length: {avg_sentence_length}\n")

with open(file_to_write, 'a') as txt_output:
    txt_output.write(output)

