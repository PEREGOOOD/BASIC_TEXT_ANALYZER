#ASK THE USER FOR A TEXT AND PUT IT IN A VARIABLE

txt = input("Write or paste down the text to analyze: ")

#ASK FOR THE LETTERS TO IDENTIFY AND STORE THEM INTO A LIST

ltrs = input("Now, write down three letters you wish to count in the text (Example: a b c ): ")

#EXTRACTING THE LENGHT OF THE LIST

lenght = len(ltrs)

#WHILE LOOK IF THE FORMAT WAS NOT WRITTEN CORRECTLY

while(lenght < 4 or lenght > 5):

    ltrs = input("You are not following the asked format, pelase try again (Example: a b c ): ")
    lenght = len(ltrs)

#STORE THE LETTERS INTO A LIST

ltrs_list=[]
ltrs_list.append(ltrs[0])
ltrs_list.append(ltrs[2])
ltrs_list.append(ltrs[4])
print(f"Your letters list is {ltrs_list}")

#USING THE LIST TO IDENTIFY THE TIMES EACH ONE APPEARS ON THE TEXT

print(f"The letter {ltrs_list[0]} is repeated {txt.count(ltrs_list[0])} times" )
print(f"The letter {ltrs_list[1]} is repeated {txt.count(ltrs_list[1])} times" )
print(f"The letter {ltrs_list[2]} is repeated {txt.count(ltrs_list[2])} times" )

#SPLIT THE TEXT INTO A LIST WITH THE WORDS TO COUNT THEM

txt_words = txt.split()
txt_words_size =len(txt_words)

print(f"Your text has {txt_words_size} words")

#SELECTING THE FIRST AND LAST LETTER OF THE TEXT

print(f"The first letter of you text is {txt[0]} and the last one is {txt[-1]}")

#REVERSING THE LIST OF THE WORDS IN THE TEXT AND PRINTING THEM BACKWARDS

txt_backwards = txt_words[::-1]
space = " "
txt_backwards_final = space.join(txt_backwards)
print(f"Your text backwards would look like this: '{txt_backwards_final}'")

#IF STATEMENT TO IDENTIFY IF THE WORD "PYTHON" IS ON THE TEXT

if "python" in txt:

    print("The word python is in the text")
else:
    print("The word python is not in the text")

