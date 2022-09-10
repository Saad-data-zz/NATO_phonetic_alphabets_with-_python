# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
import pandas

#reading csv using pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
#the function to_dic will covert the list into the dictionary
#print(data.to_dict())

#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
#print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():
    # input prompt for word
    word = input("Enter the word: ").upper()
    #check the word in the phonetic_dict

    #adding Exception considering that if the user enter the integar like number 1243 then
    #how to avoid the such kind of error
    #catch the exceptions
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only the letters in the alphabet pls.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()