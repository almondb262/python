# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
   filename = open("story.txt", "r")
   print(filename.read())
#    return "Hello World"
  
read_file_content("filename")
    

def count_words():
    text = read_file_content("./story.txt")
    text = open("story.txt")
    
    # [assignment] Add your code here
    d= dict()
    for line in text:
        line = line.strip()
        line = line.lower()
        words = line.split(" ")
        for word in words:
          if word in d:
            d[word] = d[word] + 1
          else:
           d[word] = 1

        for key in list(d.keys()):
          print(key, ":", d[key])
            
    # return {"as": 10, "would": 20}
count_words()