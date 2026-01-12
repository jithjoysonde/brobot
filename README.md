This brobot code is a fork from https://github.com/lizadaly/brobot

We are sharing our updates here so that it may potentially lead to future enhancements. :)

Capabilities co-authored with Neha Shreshta
1. broize_enhanced.py - FAQ handling with SequenceMatcher
2. broize_iBERT.py - FAQ handling with DistilBert and computing cosine similarity
3. process_inputs.py - for handling automated testing of inputs.txt and output to outputs.csv
4. Brobot Arch.jpg - based on current understanding of original brobot https://github.com/lizadaly/brobot


# Brobot

Sample code for a tutorial on bot creation in Python: <a href="https://apps.worldwritable.com/tutorials/chatbot">Chatbot Fundamentals:
An interactive guide to writing bots in Python</a>

## Installation

Requires Python 3

### Set up and activate a virtualenv

`python virtualenv venv`

`. venv/bin/activate`

### Install the Python-level dependencies

`pip install -r requirements.txt`


download Textblob corpora
'python -m textblob.download_corpora'

### Run the command-line interface

You can use the script as a library by calling `broback(sentence)` directly, or
call it from the command line. Say something custom as an argument to the script,
or the program will just use a default sentence:

`python broize.py "I am an engineer"`

Note that this bot is _extremely simple_ as it's been optimized for use
as a training tool. It's not very interesting by itself!


## License
Copyright (c) 2016 Liza Daly / Licensed under the MIT license.
