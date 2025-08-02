import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import pos_tag, RegexpParser
from collections import Counter
import re

# It's good practice to ensure the necessary NLTK data is downloaded.
# You can uncomment these lines to run them once.
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

# --- 1. Load and Tokenize Text ---

# Use a try-except block to handle cases where the file might not be found.
try:
    text = open("dorian_gray.txt", encoding='utf-8').read().lower()
except FileNotFoundError:
    print("Warning: 'dorian_gray.txt' not found. Using a sample text for demonstration.")
    text = "the artist is the creator of beautiful things. to reveal art and conceal the artist is art's aim. the critic is he who can translate into another manner or a new material his impression of beautiful things."

# Sentence and word tokenize the text using standard NLTK functions.
# This creates a list of sentences, where each sentence is a list of words.
sentences = sent_tokenize(text)
word_tokenized_text = [word_tokenize(sentence) for sentence in sentences]

# Store and print the first word-tokenized sentence.
# Accessing by index is more direct than creating a full copy in a loop.
single_word_tokenized_sentence = word_tokenized_text[0]
print("--- Sample Tokenized Sentence ---")
print(single_word_tokenized_sentence)
print("\n" + "="*40 + "\n")

# --- 2. Part-of-Speech (POS) Tagging ---

# Create a list to hold POS-tagged sentences.
pos_tagged_text = []

# Loop through each tokenized sentence, apply POS tags, and append.
for sentence in word_tokenized_text:
    pos_tagged_text.append(pos_tag(sentence))

# Store and print a sample POS-tagged sentence.
single_pos_sentence = pos_tagged_text[0]
print("--- Sample POS-Tagged Sentence ---")
print(single_pos_sentence)
print("\n" + "="*40 + "\n")


# --- 3. Define Grammars and Parse Chunks ---

# Define Noun Phrase (NP) chunk grammar.
np_chunk_grammar = "NP: {<DT>?<JJ.*>*<NN.*>+}"
np_chunk_parser = RegexpParser(np_chunk_grammar)

# Define Verb Phrase (VP) chunk grammar.
# This grammar looks for an optional NP, any number of verbs, and one or more adverbs.
vp_chunk_grammar = "VP: {<VB.*><RB.*>+}" # A slightly adjusted grammar for better VP matching
vp_chunk_parser = RegexpParser(vp_chunk_grammar)

# Create lists to hold the chunked sentences (as NLTK Trees).
np_chunked_text = []
vp_chunked_text = []

# Loop through each POS-tagged sentence and apply the parsers.
for sentence in pos_tagged_text:
    np_chunked_text.append(np_chunk_parser.parse(sentence))
    vp_chunked_text.append(vp_chunk_parser.parse(sentence))

# --- 4. Count and Display Most Common Chunks ---

def chunk_counter(chunked_sentences, chunk_label):
    """
    A function to find all chunks of a specific label in a list of parsed sentences
    and count their occurrences.
    This replaces the need for an external chunk_counters.py file.
    """
    # Using collections.Counter is highly efficient for counting items.
    chunks = Counter()

    # Iterate through each parsed sentence (which is an NLTK Tree).
    for tree in chunked_sentences:
        # tree.subtrees() finds all chunks. The filter gets only the ones with our label.
        for subtree in tree.subtrees(filter=lambda t: t.label() == chunk_label):
            # Join the words of the chunk to create a readable phrase.
            phrase = " ".join(word for word, tag in subtree.leaves())
            # Sanitize the phrase to remove punctuation for better counting.
            phrase = re.sub(r"[.,'!?]", "", phrase)
            if phrase: # Ensure the phrase is not empty after sanitization
                chunks[phrase] += 1
    
    # .most_common() returns a list of (item, count) tuples, sorted by count.
    return chunks.most_common()

# Store and print the 5 most common NP chunks.
most_common_np_chunks = chunk_counter(np_chunked_text, "NP")
print("--- Top 5 Most Common Noun Phrases (NP) ---")
# Handle case where fewer than 5 chunks are found
limit_np = min(5, len(most_common_np_chunks))
if not most_common_np_chunks:
    print("No Noun Phrases found with the specified grammar.")
else:
    for chunk, count in most_common_np_chunks[:limit_np]:
        print(f'"{chunk}" appeared {count} times')

print("\n" + "="*40 + "\n")

# Store and print the 5 most common VP chunks.
most_common_vp_chunks = chunk_counter(vp_chunked_text, "VP")
print("--- Top 5 Most Common Verb Phrases (VP) ---")
# Handle case where fewer than 5 chunks are found
limit_vp = min(5, len(most_common_vp_chunks))
if not most_common_vp_chunks:
    print("No Verb Phrases found with the specified grammar.")
else:
    for chunk, count in most_common_vp_chunks[:limit_vp]:
        print(f'"{chunk}" appeared {count} times')

