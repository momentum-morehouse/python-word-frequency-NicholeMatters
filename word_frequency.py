# STOP_WORDS = [
#     'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
#     'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
#     'will', 'with'
# ]

# def flatten_lol(lol):
#   flat_list = []
#   for sublist in lol:
#     for item in sublist: 
#       flat_list.append(item)
#   return flat_list


# def print_word_freq(file):
#     """Read in `file` and print out the frequency of words in that file."""
#     # Your code will go here. You can write additional functions if you want, and call them inside this function.
#     # first open the file
#     with open(file) as f:
#         lyrics = f.readlines()
#         word_list = [line.split() for line in lyrics]
#         print(word_list)

# # This is an "incantation." You will not see it very often, and it needs to be here to be able to pass file names as arguments.
# if __name__ == "__main__":
#     import argparse
#     from pathlib import Path

#     parser = argparse.ArgumentParser(
#         description='Get the word frequency in a text file.')
#     parser.add_argument('file', help='file to read')
#     args = parser.parse_args()

#     file = Path(args.file)
#     if file.is_file():
#         print_word_freq(file)
#     else:
#         print(f"{file} does not exist!")
#         exit(1)




import re
import string
frequency = {}  #empty dictionary
file_object = open("real_love.txt","r") #enables the program open &  read love
text_string = file_object.read().lower()
match_pattern = re.findall(r'\b[a-z]{1,15}\b',text_string) #enables program to read  words called in  line 6
print(text_string)
def remove_stopwords(review_words):
    with open('Stop_words.txt') as stopfile:
        stopwords = stopfile.read()
    list = stopwords.split()
    print(list)
    with open('a.txt') as workfile:
        read_data = workfile.read()
        data = read_data.split()
        print(data)
        for word1 in list:
            for word2 in data:
                if word1 == word2:
                    return data.remove(list)
                    print(remove_stopwords)
for word in match_pattern:
    count = frequency.get(word, 0)  #word is key, value = 0
    frequency[word] = count + 1
frequency_list = frequency.keys()
for words in frequency_list:
    print(words,frequency[words])