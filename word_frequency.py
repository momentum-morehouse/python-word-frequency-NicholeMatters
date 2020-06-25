STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

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
    with open('real_love.txt') as workfile:
        read_data = workfile.read()
        data = read_data.split()
        print(data)
        for word1 in list:
            for word2 in data:
                if word1 == word2:
                    return data.remove(list)
                    print(remove_stopwords)



# from gensim.parsing.preprocessing import remove_stopwords
# text = "You see I'm searching for a real love And I don't know where to go I been around the world and high and low And still I'll never know How it feels to have a real love 'Cause it seems there's none around Gotta end it in this way because Seems he can't be We are lovers true and through And though we made it through the storm I really want you to realize I really want to put you on I've been searchin' for someone To satisfy my every need Won't you be my inspiration Be the real love that I need? Real love I'm searchin' for a real love Someone to set my heart free Real love I'm searchin' for a real love Ooh, when I met you I just knew That you would take my heart and run Until you told me how you felt for me You said I'm not the one So I slowly came to see All of the things that you were made of And now I hope my dreams and inspirations Lead me to want some real love Real love I'm searchin' for a real love Someone to set my heart free Real love I'm searchin' for a real love I got to have a real love Love's so true"

# filtered_sentence = remove_stopwords(text)

# print(filtered_sentence)



for word in match_pattern:
    count = frequency.get(word, 0)  #word is key, value = 0
    frequency[word] = count + 1
frequency_list = frequency.keys()
for words in frequency_list:
    print(words,frequency[words])