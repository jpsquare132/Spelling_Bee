from pangram import is_pangram #DO NOT MODIFY
def get_point_value(word,letters):
  sign=True
  point=len(word)
  output=f"{word} \n{point}"
  pan_output=f"{word} - Pangram!\n{point}"
  for x in letters:
    if x not in word:
      sign=False
  for y in word:
    if y not in letters:
      sign=False
  if sign==False: # word is not a pangram
    print(word)
    return point
  else:
    point+=7
    pan_output=f"{word} - Pangram!\n"
    print(pan_output)
    return point