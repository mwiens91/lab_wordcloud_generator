[![Python version](https://img.shields.io/badge/python-3.9-blue.svg)](https://github.com/mwiens91/JuanBot)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Lab wordcloud generator

This is a "quick and dirty" script to generate a wordcloud of my lab's
research output using Python and the [wordcloud
package](https://github.com/amueller/word_cloud).

It adds in a bunch of stopwords for scientific paper "filler" words,
e.g., thus, therefore, figure, table, etc.

## Usage

Put text in `./text`. Run `./make_wordcloud.py`. Get wordcloud in
`out.png`.

I'm not including any ready-to-go text in `./text` because of copyright,
licenses, etc., but I do have them available.
