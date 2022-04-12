from collections import defaultdict
import csv
import nltk
import os
import sys


VERBS = {'MD', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'}


def is_verb(tag):
    """
    Checks if a Parts of Speech (POS) tag represents a verb. These include:
        MD  Modal verb (can, could, may, must)
        VB  Base verb (take)
        VBD Past tense (took)
        VBG Gerund, present participle (taking)
        VBN Past participle (taken)
        VBP Present tense (take)
        VBZ Present 3rd person singular (takes)

    Args:
        tag (str): A POS tag

    Returns:
        True: If the POS tag represents a string, False otherwise.
    """
    return tag in VERBS

def count_tags(text):
    """
    The funtion first tokenizes the texts then by way of a trained model, 
    the NLTK library tags the tokens using Parts of Speech (POS) tagging.
    Finally, the number of unique tags in the tagged texts are counted

    Args:
        text (str): A large chunk of text consisting of several sentences.

    Returns:
        dict: a dictionary-like object containing the counts of POS tags
            in the text string.
    """
    tokenized = [nltk.word_tokenize(sent) for sent in nltk.sent_tokenize(text)]
    tagged = nltk.pos_tag_sents(tokenized)

    pos_freq = defaultdict(lambda: 0)
    for sentence in tagged:
        for word, tag in sentence:
            if is_verb(tag):
                pos_freq[tag] += 1
    return pos_freq

def print_progress(curr, total):
    """
    Prints how many files have been analysed and what percentage of the way
    though the analysis is.

    Args:
        curr (int): The current file number
        total (int): The total number of files to be analysed 
    """
    sys.stdout.flush()
    sys.stdout.write(f"\rFile {curr} of {total} | {round((curr/total)*100, 1)}%")
    
def analyse_corpus(path):
    """
    Counts the number of verbs in text files located in a given directory

    Args:
        path (str): The absolute or relative path to the folder containing the
            text files.

    Returns:
        list(dict): a list of dictionaries each with the verbs as keys and their
            counts as values
    """
    data = []
    total = len([name for name in os.listdir(path)])
    for i, filename in enumerate(os.listdir(path)):
        try:
            paper_id, num = filename.split('--')
            num = num[:-4]
        except ValueError:
            paper_id = filename[:-4]
            num = None
        filepath = os.path.join(path, filename)
        with open(filepath, 'r') as file:
            text = file.read()
        pos_freq = count_tags(text)
        pos_freq['paper_id'] = paper_id
        pos_freq['file_num'] = num
        data.append(pos_freq)
        print_progress(i, total)
    return data

def save_data(filename, data):
    """
    Adds data to a csv file and saves it in the current working directory

    Args:
        filename (str): the name of the csv file, e.g. 'example.csv'
        data (list(dict)): a list of dictionaries each with the verbs as keys and their
            counts as values

    Note:
        The filename attribute contain the .csv extension.
    """
    cols = ['paper_id', 'file_num'] + list(VERBS) 
    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=cols)
        writer.writeheader()
        for row in data:
            writer.writerow(row)


if __name__ == '__main__':
    # Download the required packages
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')

    # Analyse the tense of the corpus
    data = analyse_corpus('./brown_corpus') # CHANGE THIS
    save_data('brown_corpus.csv', data)     # CHANGE THIS

