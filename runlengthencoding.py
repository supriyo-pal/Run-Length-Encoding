def encode(message):
    word_size=0
    encoded_message=''
    for i in range (len(message)):
        ch=message[i]
        word_size=word_size+1
        if i ==len(message)-1:
            encoded_message=encoded_message+str(word_size)+ch
            break
        else:
            if ch == message[i+1]:
                pass
            else:
                encoded_message=encoded_message+str(word_size)+ch
                word_size=0
    return encoded_message            
            
            
    #Remove pass and write your logic here

#Provide different values for message and test your program
x="AAA"
y=encode(x)
print(y)

x="ABABABAB"
y=encode(x)
print(y)

x="AAABBBBBGGHHHHJJJKKKKLLLLOOOO"
y=encode(x)
print(y)