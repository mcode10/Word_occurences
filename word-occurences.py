filename = input('Please type the document you want to result ')
def load_content(filename):
    f = open(filename, "r")
    content = f.read()
    f.close()
    return content

def analyze_content(content):
    print(content)
    
content = load_content(filename)
analyze_content(content)
