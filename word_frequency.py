
import re
import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
] #relies on lists of words

def flatten_lol(lol):
  flat_list = []
  for l in lol:
    for word in l:
      flat_list.append(word)
  return flat_list


def print_word_freq(): #the main function
    file_name = input("Enter a song")
    """Read in file and print out the frequency of words in that file."""
    # Your code will go here. You can write additional functions if you want, and call them inside this function.
    # first open the file
    with open(file_name,"r") as f:
        text_string = f.read().lower()
    frequency = {}
    match_pattern = re.findall(r'\b[a-z]{1,15}\b',text_string)
    for word in match_pattern:
        count = frequency.get(word, 0)  #word is key, value = 0
        frequency[word] = count + 1
    frequency_list = frequency.keys()
    print(frequency)
    for words in frequency_list:
        print(words,frequency[words])
# This is an "incantation." You will not see it very often, and it needs to be here to be able to pass file names as arguments.
if _name_ == "_main_":
    import argparse
    from pathlib import Path
    print_word_freq()  #calling on each file