
def word_split(phrase, list_of_words, output = None):
    if output is None:
        output = []
        k = 0    
    for word in list_of_words:
        for i in range(0, len(phrase)):
            k = len(word)+i
            if word == phrase[i:k]:
                output.append(word)          
    
    return output    
    
  
