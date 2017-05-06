from string import punctuation
filename = input('Please type in the document you want to result(please enter full file path) ')

## load_content reads file specified above by user, then saves it in RAM.

def load_content(filename):
    f = open(filename, "r")
    content = f.read()
    f.close()
    return content

## Creates dictionary and finished list.

def load_dictionary(content):
    my_list = content.split()
##    list_words(my_list)
##    strip_punctuation(my_list)
    dictionary = dict()
    count = len(my_list)
    while count > 0:
        count = count -1
        word = my_list[count]
        word2 = word.strip('!.*?:;,')
        word = word2.lower()
        if not word.isdigit():
            if word in dictionary:
                occurence = dictionary[word]
                occurence = occurence +1
                dictionary[word] = occurence
            else:               
                dictionary[word] = 1
    wordlist = sorted(dictionary.keys())
    for aword in wordlist:
         print(aword, dictionary[aword])
    return dictionary

## Defines the dictionary that load_dictionary works with.
def analyze_content(content):
    dictionary = load_dictionary(content)
    
content = load_content(filename)
analyze_content(content)
 
