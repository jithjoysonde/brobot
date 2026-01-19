from __future__ import print_function, unicode_literals
import re
import json
import os

DB_FILE = "colors.json"

def load_db():
   #Load favorite colors from JSON file.
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            return json.load(f)
    return {}

def save_db(data):
    #Save favorite colors to JSON file.
    with open(DB_FILE, "w") as f:
        json.dump(data, f)

# Load database at start
people_colors = load_db()

def set_favorite_color(name, color):
    #Store a person's favorite color persistently.
    people_colors[name.lower()] = color
    save_db(people_colors)
    return f"Okay! {name}'s favorite color is set to {color}."

def get_favorite_color(name):
    #Retrieve a person's favorite color, or return Unknown.
    key = name.lower()
    if key in people_colors:
        return f"{name}'s favorite color is {people_colors[key]}."
    else:
        return f"No favorite color stored for {name}."

def parse_input(sentence):

    # Pattern 1: "Neha's favorite color is Black"
    match_set = re.match(r"(\w+)'?s favorite color is (\w+)", sentence, re.I)
    if match_set:
        name, color = match_set.groups()
        return set_favorite_color(name, color)

    # Pattern 2: "What is the favorite color of Neha?"
    match_get = re.match(r"What is the fav(?:orite)? color of (\w+)", sentence, re.I)
    if match_get:
        name = match_get.group(1)
        return get_favorite_color(name)

    # Pattern 3: "Set Jith color to Green"
    match_set2 = re.match(r"Set (\w+).*color.*(\w+)", sentence, re.I)
    if match_set2:
        name, color = match_set2.groups()
        return set_favorite_color(name, color)

    return "Unrecognized command."

def broback(sentence):
    return parse_input(sentence)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        saying = " ".join(sys.argv[1:])
        print(broback(saying))
    else:
        print("No input provided.")
