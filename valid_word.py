def is_valid_word(word, letters, required_letter, used_words):
  wordgrabber='' #used for the string to store the letters
  boolean=False
  if len(word) >=4:
    if required_letter in word:
      for x in word:
        wordgrabber+=x
        if x in letters:
          if word in used_words:
            return f"Already used \n{boolean}"
            break
        else:
          return f"{x} is not a letter you can use. The only letters you can use are {letters} \n{boolean}"
          break
    else:
      return f"Your word must contain the letter {required_letter} \n{boolean}"
  else:
    return f"Your word must be at least 4 letters long \n{boolean}"
  return True
  

