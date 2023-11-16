import biblib.bib
import biblib.messages
import biblib.algo
import argparse
import sys
import re
from protected_word_list import list_of_capitalized_words 
from protected_word_list import list_of_dangerous_words
from protected_word_list import list_of_first_letter_capitalized_words
from protected_word_list import list_of_replaceable_words

MONTHS = 'January February March April May June July August September October November December'.split()


# Sort list of capitalized words by length, longest first
list_of_capitalized_words.sort(key=len, reverse=True)
list_of_dangerous_words.sort(key=len, reverse=True)
list_of_first_letter_capitalized_words.sort(key=len, reverse=True)
list_of_replaceable_words.sort(key=len, reverse=True)

title_line = '  title'
file_input = open('00000_references.bib', 'r')
file_output = open('002_references.bib', 'w')
word_delimiters = "[().,;:\-' ]"
# For each line in the file change the title to be add {} around words from the list of capitalized words
# and write out a new file
for line in file_input:
    # If it contains title, 
    if (title_line) in line:
        replaced = False
        # Get text between {}
        title = re.search(r'\{(.*)\}', line).group(1)
        # Split it into words and remove punctuation
        title_words = re.split(word_delimiters, title)
        # Find segments enclosed in {}
        replaced_words = ""
        # For each word
        for word in list_of_capitalized_words:
            # If it is in line and is not contained in {} within the line
            if word in line:# and word not in replaced_words:
                replaced = True
                # Search and replace line with word surrounded by {}
                #line = line.replace(word, "{"+word+"}")
                line = re.sub(r'\b'+word+r'\b', "{"+word+"}", line)
                replaced_words = replaced_words + word + ", "
        for word in list_of_dangerous_words:
            if word in title_words:# and word not in replaced_words:
                replaced = True
                # Search and replace line with word surrounded by {}
                # but only if the word is standalone
                line = re.sub(r'\b'+word+r'\b', "{"+word+"}", line)
                replaced_words = replaced_words + word + ", "
        for word in list_of_first_letter_capitalized_words:
            # If it is in line and is not contained in {} within the line
            if word in line:# and word not in replaced_words:
                replaced = True
                # Search and replace line with word surrounded by {}
                line = line.replace(word, "{"+word[0]+"}"+word[1:])
                replaced_words = replaced_words + word + ", "

        for word in list_of_replaceable_words:
            # If it is in line and is not contained in {} within the line
            if word in line:# and word not in replaced_words:
                replaced = True
                # Search and replace line with word surrounded by {}
                line = line.replace(word, "{"+word+"}")
                replaced_words = replaced_words + word + ", "

        if replaced:
            print("Replaced words: " + replaced_words)
        print(line.strip("\n"))
    # Write it to the file
    file_output.write(line)
file_input.close()
file_output.close()
