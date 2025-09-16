# mapreduce_functions.py

import re

def mapper(text_chunk):
    """
    Processes a chunk of text, finds words, and returns a list of (word, 1) tuples.
    """
    # Convert the chunk to lowercase and find all words.
    text_chunk = text_chunk.lower()
    words = re.findall(r'\b[a-z]{3,}\b', text_chunk)
    
    # Create a list of (word, 1) tuples and return it.
    mapped_results = [(word, 1) for word in words]
    return mapped_results


def reducer(item):
    """
    Reduces a key and its list of values to a single value.
    Takes one item from the shuffled list, e.g., ('whale', [1, 1, 1, 1]).
    """
    word, counts = item
    # Return a tuple of the word and the sum of its counts.
    return (word, sum(counts))