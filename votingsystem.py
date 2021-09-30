turn = 0
h = 1
s = 1
c = 1
skiph = 1
skips = 1 
skipc = 1
PlayerOne = str( input ("Player 1 is ") )
PlayerTwo = str( input ("Player 2 is ") )
PlayerThree = str( input ("Player 3 is ") )
while True:
    h = float( input ("has " + PlayerOne + " Used any skips? 1 = yes") )
    s = float( input ("has " + PlayerTwo + " Used any skips? 1 = yes") )
    c = float( input ("has " + PlayerThree + " Used any skips? 1 = yes") )
    if h==1:
        skiph = skiph - 1
    if s==1:
        skips = skips - 1
    if c==1:
        skipc = skipc - 1
    print (str(PlayerOne) + " has " + str(skiph) + " Skips")
    print (str(PlayerTwo) + " has " + str(skips) + " Skips")
    print (str(PlayerThree) + " has " + str(skipc) + " Skips")
    turn = turn + 1
    print ("turn " + str(turn))
    mod = turn % 2
    if mod > 0:
        skiph = skiph + 1
        skips = skips + 1
        skipc = skipc + 1