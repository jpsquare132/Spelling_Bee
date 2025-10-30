from valid_word import is_valid_word # DO NOT MODIFY

# Write the get_word function here.
def get_word(letters, required_letter, used_words):
  word=input("Enter your word: \n")
  while word != "END":
    if word not in used_words:
      if len(word)>=4:
        if required_letter in word:
          word_collector = True
          for char in word:
            if char not in letters:
              print(f"{char} is not a letter you can use. The only letters you can use are {letters}")
              word_collector = False
          if word_collector:
            return word
        else:
          print(f"Your word must contain the letter {required_letter}")
      else:
          print("Your word must be at least 4 letters long")
    else:
      print("Already used")
    
    word=input("Enter your word: \n")
  return word

  



