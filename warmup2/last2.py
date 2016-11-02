def last2(str):
  final2 = str[-2:]
  count = 0
  for x in range(len(str)-2):
    if str[x:x+2] == final2:
      count += 1
  return count