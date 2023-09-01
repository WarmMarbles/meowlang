
# please use comments i forgot everything i wrote and i don't know what anything does :(((

def encode(text):
    meow = "meow"
    meowText = ""
    counter = 0
    # binaryText turns "text" input to binary
    binaryText = "".join(format(ord(i), "08b") for i in text)
    # print(binaryText) is only used for debugging purposes
    # print(binaryText)
    for char in binaryText:
        # if char is 1, add meow letter in uppercase. then add 1 to counter.
        if char == "1":
            meowText += meow[counter].upper()
            counter += 1
            if counter > 3:
                counter = 0
        # if char is 0, add meow letter in lowercase. then add 1 to counter.
        elif char == "0":
            meowText += meow[counter]
            counter += 1
            if counter > 3:
                counter = 0
        else:
            break
    return meowText


def decode(text):
    decodedText = ""
    binaryText = ""
    # for each character, add 1 if it's uppercase and add 0 if it's lowercase
    for char in text:
        if char.isupper():
            binaryText += "1"
        elif char.islower():
            binaryText += "0"
        else:
            break
    # transforms binaryText into ASCII (i think), then return as decodedText
    return decodedText.join(chr(int(binaryText[i*8:i*8+8],2)) for i in range(len(binaryText)//8))

while True:
    answer = input("Encode or Decode?\n").lower().strip()
    if answer == "encode":
        print("-----------")
        text = input(">>>")
        meowText = encode(text)
        print(meowText)
        print("-----------")
    elif answer == "decode":
        print("-----------")
        text = input(">>>")
        decodedText = decode(text)
        print(decodedText)
        print("-----------")
    else:
        print("<<missinput, try again>>")
