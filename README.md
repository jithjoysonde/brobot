This brobot code is a fork from https://github.com/lizadaly/brobot

We are sharing our updates here so that it may potentially lead to future enhancements. :)
Please cite your sources appropriately.


Capabilities co-authored with Neha Shreshta
1. broize_enhanced.py - FAQ handling with SequenceMatcher
2. broize_iBERT.py - FAQ handling with DistilBert and computing cosine similarity
3. process_inputs.py - for handling automated testing of inputs.txt and output to outputs.csv
4. Brobot Arch.jpg - based on current understanding of original brobot https://github.com/lizadaly/brobot
![Brobot Arch](https://github.com/user-attachments/assets/ceb633ed-8960-4b7f-bb77-6418c09da689)
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
call it from the command line. Say something custom as an argument to the script.

`python broize.py "This is a program"`

`python broize_enhanced.py "This is the enhanced program using SequenceMatcher"`

`python broize_iBERT.py "This uses DistilBert"`

Automated testing

'python process_inputs.py'

Note that this bot is for use as a training tool. It's STILL not very interesting by itself!


## License
Copyright (c) 2016 Liza Daly / Licensed under the MIT license.
