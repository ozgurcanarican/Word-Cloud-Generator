##@author__: Özgür Can Arıcan
##@contact__: ozgurcanarican95@gmail.com
##@github__: www.github.com/ozgurcanarican

import matplotlib.pyplot as plt
from wordcloud import WordCloud

data = []

print("""
***************************************************************************************

Welcome to WordCloud Generator...

The program is going to take your words for creating wordcloud.

    1)Please enter one word for each time.
    2)If your expression has multiple words, write it without space between them.
        "Example: Machine Learning ------> MachineLearning"
        "Example: Artificial Intelligence ------> ArtificialIntelligence"
    3)Initially, write your important words. They will appear bigger than others.
    4)When you have done with it, enter "q" or "Q" as a last word to stop words entries.

***************************************************************************************
""")

while True:
    word = input("Please enter your word/(Enter 'q' or 'Q' for stop entries): ")
    if word == "q" or word == "Q":
        break
    else:
        data.append(word)

print("""
****************************************
Please choose your background color:

1)Black        4)Blue          7)Orange
2)White        5)Yellow        8)Purple
3)Red          6)Green         9)Gray
****************************************
""")

while True:
    chosen_color = input("Please enter the number of the color you choosed: ")
    
    if chosen_color == "1":
        chosen_color = "black"
        print(chosen_color)
        break
    elif chosen_color == "2":
        chosen_color = "white"
        break
    elif chosen_color == "3":
        chosen_color = "red"
        break
    elif chosen_color == "4":
        chosen_color = "blue"
        break
    elif chosen_color == "5":
        chosen_color = "yellow"
        break
    elif chosen_color == "6":
        chosen_color = "green"
        break
    elif chosen_color == "7":
        chosen_color = "orange"
        break
    elif chosen_color == "8":
        chosen_color = "purple"
        break
    elif chosen_color == "9":
        chosen_color = "gray"
        break
    else:
        print("\n\nYou entered a character or a number out of range. Please reenter a number\n\n")
        

plt.subplots(figsize = (8, 8))

wordcloud = WordCloud(background_color = chosen_color).generate(" ".join(data))
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig("wordcloud.png")
