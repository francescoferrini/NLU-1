import spacy
nlp = spacy.load('en_core_web_sm')

''' Function that expracts a path of dependency relations from the ROOT to a token'''
def getDependency(sentence):
    doc = nlp(sentence)
    dep_list = []
    
    for token in doc:
        list1 = []
        while(token.head != token):
            list1.append(token.text)
            list1.append(token.dep_+":")
            list1.append("|")
            token = token.head
        list1.append(token.head)
        list1.append("ROOT:")
        list1.reverse()
        dep_list.append(list1)
        
    return dep_list 


''' Function that extracts subtree of a dependents given a token'''
def subtreeExtraction(sentence):
    doc = nlp(sentence)
    my_dict = {}
    
    for token in doc:
        my_dict[token] = []
        give_subtree = token.subtree
        for sent in give_subtree:
            if sent.text!=token.text:
                my_dict[token].append(sent.text)

    return my_dict


'''  Function that checks if a given list of tokens (segment of a sentence) forms a subtree'''
def checkSubtree(sentence, word_list):
    doc = nlp(sentence)

    for token in doc:
        give_subtree = token.subtree
        if ([t.text for t in give_subtree] == word_list):
            return True
    return False
        

''' Function that identifies head of a span, given its tokens'''
def spanHead(span):
    return span.root.text

''' Function  that extracts sentence subject, direct object and indirect object spans'''
def extractSpanInfo(sentence):
    doc = nlp(sentence)
    
    my_dict = {
        "subj": [],
        "dobj": [],
        "iobj": []
    }
    
    for token in doc:
        list = []
        if(token.dep_ == 'nsubj' or token.dep_ == 'nsubjpass'):
            subtree = token.subtree
            for word in subtree:
                list.append(word.text)
            list = " ".join(list)
            my_dict["subj"].append(list)
        elif(token.dep_ == 'dobj'):
            subtree = token.subtree
            for word in subtree:
                list.append(word.text)
            list = " ".join(list)
            my_dict["dobj"].append(list)
        elif(token.dep_ == 'dative'):
            subtree = token.subtree
            for word in subtree:
                list.append(word.text)
            list = " ".join(list)
            my_dict["iobj"].append(list)
            
    return my_dict

print("---------- Exercise1 ----------")

example = ("The fire was caused by the gas stove and not by the gas tank.")
print("The sentence is: ", example)

dependency_list = getDependency(example)
for list in dependency_list:
    print(list)
    
print("\n---------- Exercise2 ----------")

print("The sentence is: ", example)

dict = subtreeExtraction(example)
print(dict)
    
print("\n---------- Exercise3 ----------")

print("The sentence is: ", example)

word_list =["The", "fire"]

if checkSubtree(example, word_list) == True:
    print("The word list", word_list, "forms a subtree")
else:
    print("The word list", word_list, "doesn't form a subtree")
    
print("\n---------- Exercise4 ----------")

example2 = "Bills on ports and immigration were submitted by Brownback Republican Senator of Kansas"
print("The sentence is: ", example2)

doc = nlp(example2)
span = doc[7:12]
print("This is the span: ", span)

span_head = spanHead(span)
print("The head is: ", span_head)

print("\n---------- Exercise5 ----------")

example3 = "Carla bought an iphone and gave it to her boyfriend"
print("The sentence is: ", example3)

dict = extractSpanInfo(example3)
print(dict)
