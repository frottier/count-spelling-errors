#! /usr/bin/env python3

# dependencies: spylls, hunspell
# usage: takes target folder as positional argument
# reads all texts in target folder, counts spelling mistakes. this hopefully gives a rough number
# that lets us evaluate OCR output, depending on what we do in scantailor.

from sys import argv
import os
import re
from spylls.hunspell import Dictionary

# setup
target_folder = argv[1]
dictionary = Dictionary.from_files('/usr/share/hunspell/de_DE')

# scan for textfiles
files = os.scandir(target_folder)
textfiles = []
for file in files:
    if file.name.endswith('.txt'):
        textfiles.append(file)

print(f'Found {len(textfiles)} textfiles.')

# iterate and count
word_count = 0
error_count = 0

for file in textfiles:
    with open(file, 'r') as text:
        for line in text:
            char_num_line = re.sub('[^0-9a-zA-ZäöüÄÖÜß]', ' ', line)         # remove punctuation
            cleaned_line = re.sub(' +', ' ', char_num_line)                  # remove multiple spaces
            words = cleaned_line.split(' ')
            for word in words:
                word_count += 1
                if dictionary.lookup(word) is False:
                    error_count += 1

# calculate error ratio
error_ratio = round((error_count / word_count) * 100, 2)

# report the numbers
print(f'Reporting {word_count} words and {error_count} spelling errors.')
print(f'The error ratio is {error_ratio} percent.')

