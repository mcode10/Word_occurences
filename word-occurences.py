from string import punctuation
filename = input('Please type in the document you want to result ')
def load_content(filename):
    f = open(filename, "r")
    content = f.read()
    f.close()
    return content

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
                print(word, occurence)
            else:
                print("First occurence", word)               
                dictionary[word] = 1
##      print (dictionary)
    return dictionary

    
def list_words(my_list):
    count = len(my_list)
    while count > 0:
        count = count -1
        word = my_list[count]
##        if word.isalpha() is False:
##           print(word)

def analyze_content(content):
    dictionary = load_dictionary(content)
##    for k,v in dictionary.items():
##        print(k, v)
##    print(dictionary)   
    
content = load_content(filename)
analyze_content(content)
 
