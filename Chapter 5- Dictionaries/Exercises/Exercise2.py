#A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
# * Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store 
# their meanings as values.
# * Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print 
# the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between 
# each word-meaning pair in your output.

glossary = {
    'loop': 'Work through a collection of items, one at a time.',
    'float': 'Floating point numbers are decimal values or fractional numbers.',
    'list': 'A collection of items in a particular order.',
    'integer': 'a whole number, positive or negative, without decimals, of unlimited length.',
    'dictionary': "A collection of key-value pairs.",
    }

for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)