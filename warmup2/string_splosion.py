# Given a non-empty string like "Code" return a string like "CCoCodCode".
def string_splosion(str):
  result = ""
  for x in range(1, len(str) + 1):
    result += str[0:x]

  return result

