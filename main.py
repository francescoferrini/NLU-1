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
    
    for token_pos in (range(len(doc))):
        my_dict[doc[token_pos]] = []
        give_subtree = doc[token_pos].subtree
        for sent in give_subtree:
            if sent.text!=doc[token_pos].text:
                my_dict[doc[token_pos]].append(sent.text)

    return my_dict


'''  Function that checks if a given list of tokens (segment of a sentence) forms a subtree'''
def checkSubtree(sentence, token_list):
    doc = nlp(sentence)
    
    for i in range(len(doc)):
        give_subtree = doc[i].subtree
        if ([t.text for t in give_subtree] == token_list):
            return True
    return False
        

''' Function that identifies head of a span, given its tokens'''
def spanHead(span):
    span_length = len(span)
    span_as_doc = span.as_doc()
    for token in span_as_doc:
        if(token.text == token.head.text):
            head = token.text
    return head
    

''' Function  that extracts sentence subject, direct object and indirect object spans'''
def extractSpanInfo(sentence):
    doc = nlp(sentence)
    
    my_dict = {
        "subj": [],
        "dobj": [],
        "iobj": []
    }
    
    for token in doc:
        if(token.dep_ == 'nsubj' or token.dep_ == 'nsubjpass'):
            my_dict["subj"].append(token.text)
        elif (token.dep_ == 'dobj'):
            my_dict["dobj"].append(token.text)
        elif (token.dep_ == 'iobj'):
            my_dict["iobj"].append(tokrn.text)
            
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

#subtree_list = subtreeExtraction(example)
#for list in subtree_list:
    #print(list)
    
print("\n---------- Exercise3 ----------")

print("The sentence is: ", example)

token_list =["The", "fire"]

if checkSubtree(example, token_list) == True:
    print("The token list", token_list, "forms a subtree")
else:
    print("The token list", token_list, "doesn't form a subtree")
    
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
