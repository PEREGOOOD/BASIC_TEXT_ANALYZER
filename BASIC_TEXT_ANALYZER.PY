#FIRST LET'S ASK THE USER TO WRITE THE TEXT AND THE LETTERS TO ANALYZE AND STORE THEM INTO A VARIABLE.

txt = input("Write or paste down the text to analyze: ")

ltrs = input("Now, write down three letters you wish to count in the text (Example: a b c ): ")
lenght = len(ltrs)

while(lenght < 4 or lenght > 5):

    ltrs = input("You are not following the asked format, pelase try again (Example: a b c ): ")
    lenght = len(ltrs)

#THE FIRST TASK IS TO COUNT HOW MANY TIMES THE LETTERS IN THE VARIABLE ltrs APEARS ON THE TEXT
#LET'S CREATE A LIST TO STORE THE LETTERS THE USER WROTE

ltrs_list=[]
ltrs_list.append(ltrs[0])
ltrs_list.append(ltrs[2])
ltrs_list.append(ltrs[4])
print(ltrs_list)

print(f"La letra {ltrs_list[0]} se repite {txt.count(ltrs_list[0])} veces" )

