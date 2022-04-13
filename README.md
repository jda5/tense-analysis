# Tense Analysis

The `tense-analysis.py` script contains the source code used to evaluate the ratio of past to present-tense verbs in a corpus created from academic mathematics papers uploaded to the ArXiv, as well as the Brown and LOB corpora.

This work was done by *** at *** [censored to protect the anonymity of the author(s) as their paper is being reviewed].

In order to run this script, you will need to install Python (version 3.8) and NLTK (version 3.6). Details on how to install Python can be found here: https://www.python.org, and you can learn how to install NLTK here: https://www.nltk.org/install.html.

Once you have these installed you can run the script by placing it in a folder with the corpora. Your file structure should look like this:

```
|-- tense_analysis.py
|-- corpus
   |-- file1.txt
   |-- file2.txt
   |-- file3.txt
   etc.
```
Finally, you will need to change the code on lines 122 and 123 to tell Python which folder the corpus is located in. For example, if you were analysing the LOB corpus, these two lines should read:

```
data = analyse_corpus('./lob_corpus')
save_data('lob_corpus.csv', data)
```

The example above tells Python to analyse the corpus located in the `lob_corpus` folder, and then to save the data to a file called `lob_corpus.csv`
