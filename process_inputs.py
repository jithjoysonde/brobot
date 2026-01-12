from __future__ import print_function
import csv
from difflib import SequenceMatcher
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
INPUTS_FILE = os.path.join(ROOT, 'inputs.txt')
OUTPUTS_FILE = os.path.join(ROOT, 'outputs.csv')

try:
    import broize_enhanced as be
except Exception as e:
    print('Failed to import broize_enhanced:', e)
    sys.exit(1)


def best_faq_score_and_answer(text):
    text_lower = text.lower()
    best_score = 0.0
    best_question = None
    for q in be.FAQ.keys():
        score = SequenceMatcher(None, text_lower, q.lower()).ratio()
        if score > best_score:
            best_score = score
            best_question = q
    best_answer = be.FAQ.get(best_question) if best_score > 0 else None
    return best_score, best_answer


def process():
    if not os.path.exists(INPUTS_FILE):
        print('inputs.txt not found at', INPUTS_FILE)
        sys.exit(1)

    with open(INPUTS_FILE, 'r', encoding='utf-8') as f_in, \
         open(OUTPUTS_FILE, 'w', encoding='utf-8', newline='') as f_out:
        writer = csv.writer(f_out)
        writer.writerow(['input', 'response', 'faq_score'])

        for raw in f_in:
            line = raw.strip()
            if not line:
                continue

            # compute best FAQ match score
            score, answer = best_faq_score_and_answer(line)
            faq_score = round(score, 3) if score > 0.0 and score > 0.0 else ''

            try:
                response = be.broback(line)
            except Exception as e:
                response = f'__ERROR__: {e}'

            # If the bot already returned the FAQ answer, keep the score; otherwise keep score only when above threshold
            if score <= 0.7:
                faq_score = ''

            writer.writerow([line, response, faq_score])

    print('Wrote outputs to', OUTPUTS_FILE)


if __name__ == '__main__':
    process()
