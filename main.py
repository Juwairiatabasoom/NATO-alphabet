import pandas as pd

data=pd.read_csv("nato_phonetic_alphabet.csv")



#TODO 1. Create a dictionary in this format:

data_dict={row.letter:row.code for (index,row) in data.iterrows()}
print(data_dict)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_words():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError :
        print("Sorry! enter only letters")
        generate_words()
    else:
        print(output_list)

generate_words()


