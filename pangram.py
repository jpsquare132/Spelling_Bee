def is_pangram(guess, letters):
  sign=True
  for x in letters:
    if x not in guess:
      sign=False
      return sign
  for y in guess:
    if y not in letters:
      sign=False
      return sign
  return sign
  


      
