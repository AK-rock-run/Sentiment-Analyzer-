import string
positive_word=["good","nice","happy","amazing","loved","liked","worthit","satisfied"]
negative_word=["bad","sad","dislike","worse","unsatisfied","noworth","poor"]
text=input("Enter your review for this product:")
text=text.lower()
text = text.translate(str.maketrans('', '', string.punctuation))
words=text.split()
pos_count=0
neg_count=0
for i in range(len(words)):
    if words[i]=='not' and i+1<len(words):
        if words[i+1] in positive_word:
            neg_count+=1
        elif words[i+1] in negative_word:
            pos_count+=1 
        i+=1
    else:
        if words[i] in positive_word:
           pos_count+=1
        elif words[i] in negative_word:
           neg_count+=1

# final output
if pos_count>neg_count:
    print("Thank you for the review :) \nWe ensure maintaining similar satisfaction further <3")
elif pos_count<neg_count:
    print("We Apologize for inconvenince you faced...\n will make sure this not happens again >_< ")
else:
    print("Thank you for your review!!")
        


