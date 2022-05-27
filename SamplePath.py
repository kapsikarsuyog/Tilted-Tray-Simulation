import random
def SamplePath(n,epochs):
  if(2000%n !=0):
    return print("Error! 2000 can not be devided ny n")

  class Tray:
    def __init__(self, loc, ordr):
      self.currLocation = loc
      self.carryOrder = ordr


  trays = [Tray(i, 0) for i in range(1, 2001)]
  sortedItem = 0
  induction = []
  k=0
  while(k!=2000):
    k+=2000/n
    induction.append(k)

  induction=tuple(induction)

  for itr in range(epochs):
    #if (itr%10000 ==0):
     # print(itr)
    for tray in trays:
      if (tray.currLocation in induction):
        tray.carryOrder = random.randint(1, 2000) if tray.carryOrder == 0 else tray.carryOrder

      if tray.currLocation < 2000:
        tray.currLocation = tray.currLocation + 1
      else:
        #print(tray.currLocation)
        tray.currLocation = 1

      if (tray.currLocation == tray.carryOrder):
        tray.carryOrder = 0
        sortedItem += 1

  return(sortedItem)