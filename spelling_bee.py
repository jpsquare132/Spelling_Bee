# DO NOT REMOVE
from get_word import get_word                 
from score import get_point_value  


def spelling_bee():
  letters=input("Welcome to Spelling Bee! Enter your 7 letters, separated by commas: \n")
  letters=letters.split(",")
  #next is required letter statement
  required_letter=input(f"Which of these 7 letters {letters} will be your required letter?\n")
  while required_letter not in letters:
    print(f"{required_letter} is not an available letter. Please choose from the following:{letters}\n")
    required_letter=input(f"Which of these 7 letters {letters} will be your required letter?\n")
  #need used word list
  word= ""
  used_words=[]
  point=0 #keeps score

  while word != "END":
    word=get_word(letters, required_letter, used_words)
    used_words.append(word)
    if word=="END":
      print(f"Your final score is {point}")
    else:
      point+=get_point_value(word, letters)
      used_words.append(word)

spelling_bee() # DO NOT REMOVE
