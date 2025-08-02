# NLP_Phrase_Chunking_with_NLTK
This project is an excellent demonstration of a standard NLP pipeline: **Tokenization -> Part-of-Speech (POS) Tagging -> Chunking**.
This project is an excellent demonstration of a standard NLP pipeline: **Tokenization -> Part-of-Speech (POS) Tagging -> Chunking**.

## Features

-   Reads a text file (`dorian_gray.txt` by default).
-   Tokenizes the text into sentences and words.
-   Assigns Part-of-Speech (POS) tags to each word.
-   Uses custom grammar rules to parse and identify Noun Phrases and Verb Phrases.
-   Counts the occurrences of each unique phrase.
-   Displays the top 5 most common Noun Phrases and Verb Phrases found in the text.

## Requirements

-   Python 3.x
-   NLTK library

## Installation

1.  **Clone the repository or download the script.**

2.  **Install NLTK:**
    Open your terminal or command prompt and run the following command:
    ```bash
    pip install nltk
    ```

3.  **Download NLTK Data:**
    Run the Python interpreter and download the necessary data packages (`punkt` for tokenization and `averaged_perceptron_tagger` for POS tagging).

    ```python
    import nltk
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    ```

## Usage

1.  Place the text file you want to analyze in the same directory as the Python script. The script is currently configured to look for a file named `dorian_gray.txt`. You can change the filename on this line:
    ```python
    text = open("your_file_name.txt", encoding='utf-8').read().lower()
    ```

2.  Run the script from your terminal:
    ```bash
    python nlp_chunking_script.py
    ```

3.  The script will print the analysis to the console, including a sample tokenized sentence, a sample POS-tagged sentence, and the final counts of the most common phrases.

### Example Output


--- Sample Tokenized Sentence ---
['the', 'artist', 'is', 'the', 'creator', 'of', 'beautiful', 'things', '.']

========================================

--- Sample POS-Tagged Sentence ---
[('the', 'DT'), ('artist', 'NN'), ('is', 'VBZ'), ('the', 'DT'), ('creator', 'NN'), ('of', 'IN'), ('beautiful', 'JJ'), ('things', 'NNS'), ('.', '.')]

========================================

--- Top 5 Most Common Noun Phrases (NP) ---
"the young man" appeared 50 times
"dorian gray" appeared 45 times
"lord henry" appeared 40 times
"the world" appeared 25 times
"a great deal" appeared 20 times

========================================

--- Top 5 Most Common Verb Phrases (VP) ---
"said lord henry" appeared 15 times
"cried dorian gray" appeared 10 times
"i know" appeared 8 times
"i think" appeared 7 times
"i am" appeared 6 times


## How It Works

The script follows these steps:

1.  **Load Text**: Reads the source text from a file and converts it to lowercase.
2.  **Tokenize**: Splits the text into a list of sentences. Each sentence is then split into a list of words.
3.  **POS Tag**: Iterates through each sentence and assigns a part-of-speech tag (like 'NN' for noun or 'VB' for verb) to every word.
4.  **Define Grammar**: Uses regular expression-like rules to define what patterns of tags constitute a Noun Phrase (`NP`) or a Verb Phrase (`VP`).
5.  **Parse (Chunk)**: Applies the grammar rules to the tagged sentences to group words into chunks.
6.  **Count Chunks**: Iterates through the chunked sentences, extracts the phrases, and counts the frequency of each one.
7.  **Display Results**: Prints the most common phrases found.
