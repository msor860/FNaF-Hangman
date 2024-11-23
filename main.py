import random
k = 6
l = ["freddy", "bonnie", "chica", "foxy", "the puppet", "springtrap","ennard", "william afton", "dreadbear", "balloon boy","toy freddy", "toy bonnie", "toy chica", "mangle", "nightmare freddy", "nightmare bonnie", "nightmare chica", "nightmare foxy", "plushtrap", "nightmare fredbear", "nightmare", "nightmare balloon boy", "fredbear", "spring bonnie", "rwqfsfasxc"]
x = random.randint(0,24)
if x == 24:
  r = random.randint(0,4)
  if r != 4:
    x = random.randint(0, 23)
t = (len(l[x]))
blanks = []
non_spaces = 0
for c in l[x]:
  if c == " ":
    blanks.append(" ")
  else:
    non_spaces += 1
    blanks.append("_")


count = 0
while True:
  print(' '.join(blanks))
  a = input("")
  found = False
  for i in range(len(l[x])):
    if l[x][i] == a:
      blanks[i] = a
      count += 1
      found = True
  
  if count == non_spaces:
    print(l[x])
    print("You Won!")
    break
  if found == False:
    k -= 1
    if k == 0:
      print("GAME OVER")
      print(l[x])
      break
    else:
      print(k)