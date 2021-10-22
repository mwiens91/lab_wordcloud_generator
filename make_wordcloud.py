#!/usr/bin/env python3

import glob
import wordcloud

# Width and height in pixels
WIDTH = 2560
HEIGHT = 1440

# Number of words to include
MAX_WORDS = 1500

# Set of words to ban - note we're going to preprocess this
# instead of passing this to the wordcloud package, since
# we want to use its own stopwords as well
BAN_WORDS = {
    "fig",
    "figs",
    "figure",
    "table",
    "figures",
    "tables" "via",
    "well",
    "respectively",
    "one",
    "two",
    "three",
    "given",
    "thus",
    "lead",
    "despite",
    "shown",
    "resulting",
    "include",
    "may",
    "following",
    "similar",
    "ref",
    "refs",
    "CoV",
    "even",
    "seen",
    "rather" "using",
    "use",
    "via",
}

# Get all the paths
all_text_files = glob.glob("./text/*.txt")

# Open and grab text
list_of_texts = []

for path in all_text_files:
    with open(path, "r") as f:
        list_of_texts += [f.read()]

# Merge text
all_text = "\n".join(list_of_texts)

# Generate wordcloud
wordcl = wordcloud.WordCloud(
    width=WIDTH, height=HEIGHT, max_words=MAX_WORDS, min_word_length=3
)
wordcl.stopwords.update(BAN_WORDS)
wordcl.generate(all_text)

wordcl.to_file("out.png")
