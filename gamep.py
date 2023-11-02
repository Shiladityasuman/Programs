import random
print(" -----------------------------------------------------------------------\n "
      " --------------------------- Maths luck --------------------------------\n "
      " -----------------------------------------------------------------------\n ")
print("press \n"
      "1  to start game \n"
      "2  for help \n")
getInput = int(input())
if getInput == 1:
    NoOfTimes = 10
    PointsForP1 = 0
    PointsForC1 = 0
    PointsForP2 = 0
    PointsForC2 = 0
    while True:
        if NoOfTimes > 0:
            lst = [1, 2, 3, 4]
            lstb = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
            b = random.choice(lstb)
            d = random.choice(lstb)
            p = random.choice(lst)
            o = random.choice(lst)
            i = random.choice(lst)
            u = random.choice(lst)
            c1opt = random.choice(lst)
            c2opt = random.choice(lst)


            def fun1(w, x, y, z):
                out = p * w + o * x + i * y + u * z
                return out


            print("Function for this round is " + str(p) + "*a+" + str(o) + "*b+" + str(i) + "*c+" + str(u) + "*d")
            while True:
                try:
                    a = int(input("player 1 input number of your choice  "))
                    if a < 51 and a % 2 == 0:
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("You must input a even number within 50, try again")
            while True:
                try:
                    opt1 = int(input("choose your range \n"
                                     "1) for 0 to 200 \n"
                                     "2) for 201 to 400 \n"
                                     "3) for 401 to 600 \n"
                                     "4) for 601 to 800 \n "))
                    if opt1 in lst:
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("invalid input, try again")
            while True:
                try:
                    c = int(input("player 2 input number of your choice  "))
                    if c < 51 and c % 2 == 0:
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("You must input a even number within 50, try again")
            while True:
                try:
                    opt2 = int(input("choose your range \n"
                                     "1) for 0 to 200 \n"
                                     "2) for 201 to 400 \n"
                                     "3) for 401 to 600 \n"
                                     "4) for 601 to 800 \n "))
                    if opt2 in lst:
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("invalid input, try again")
            print(" \"automated player 1\" choose  " + str(b) + " \"automated player 2\" choose  " + str(d))
            print("Function for this round is solved as " + str(p) + "*" + str(a) + "+" + str(o) +
                  "" + str(b) + "+" + str(i) + "" + str(c) + "+" + str(u) + "*" + str(d) + "for player 1\n"
                  "\t \t \t \t \t \t \t and as  " + str(
                p) + "*" + str(c) + "+" + str(o) +
                  "" + str(d) + "+" + str(i) + "" + str(a) + "+" + str(u) + "*" + str(b) + "for player 2")
            result1 = str(fun1(a, b, c, d))
            result2 = str(fun1(c, d, a, b))
            cresult1 = str(fun1(b, c, d, a))
            cresult2 = str(fun1(d, a, b, c))
            print("Result of the equation of this round for player1 " + result1)
            print("Result of the equation of this round for player2 " + result2)
            print("Result of the equation of this round for automated player1 " + cresult1)
            print("Result of the equation of this round for automated player2 " + cresult2)
            a = int(result1)
            b = int(cresult1)
            c = int(result2)
            d = int(cresult2)
            if opt1 == 1:
                if a == 200 or a < 200:
                    PointsForP1 += 1
            if opt1 == 2:
                if 401 > a > 200:
                    PointsForP1 += 1
            if opt1 == 3:
                if 601 > a > 400:
                    PointsForP1 += 1
            if opt1 == 4:
                if a > 600:
                    PointsForP1 += 1
            if c1opt == 1:
                if b == 200 or b < 200:
                    PointsForC1 += 1
            if c1opt == 2:
                if 401 > b > 200:
                    PointsForC1 += 1
            if c1opt == 3:
                if 601 > b > 400:
                    PointsForC1 += 1
            if c1opt == 4:
                if b > 600:
                    PointsForC1 += 1
            if opt2 == 1:
                if c == 200 or c < 200:
                    PointsForP2 += 1
            if opt2 == 2:
                if 401 > c > 200:
                    PointsForP2 += 1
            if opt2 == 3:
                if 601 > c > 400:
                    PointsForP2 += 1
            if opt2 == 4:
                if c > 600:
                    PointsForP2 += 1
            if c2opt == 1:
                if d == 200 or d < 200:
                    PointsForC2 += 1
            if c2opt == 2:
                if 401 > d > 200:
                    PointsForC2 += 1
            if c2opt == 3:
                if 601 > d > 400:
                    PointsForC2 += 1
            if c2opt == 4:
                if d > 600:
                    PointsForC2 += 1
            print("Points of player 1 = " + str(PointsForP1) + "\n" +
                  "Points of player 2 = " + str(PointsForP2) + "\n" +
                  "Points of automated player 1 = " + str(PointsForC1) + "\n" +
                  "Points of automated player 2 = " + str(PointsForC2) + "\n")
            NoOfTimes = NoOfTimes - 1
            noot = str(NoOfTimes)
            print(noot + " more rounds remaining to complete the game")
        else:
            print("Points of player 1 = " + str(PointsForP1) + "\n" +
                  "Points of player 2 = " + str(PointsForP2) + "\n" +
                  "Points of automated player 1 = " + str(PointsForC1) + "\n" +
                  "Points of automated player 2 = " + str(PointsForC2) + "\n")
            if PointsForP1 > PointsForP2 and PointsForP1 > PointsForC1 and PointsForP1 > PointsForC2:
                print("Player 1 is winner")
            elif PointsForP2 > PointsForP1 and PointsForP2 > PointsForC1 and PointsForP2 > PointsForC2:
                print("Player 2 is winner")
            elif PointsForC1 > PointsForP1 and PointsForP2 < PointsForC1 and PointsForC1 > PointsForC2:
                print("Automated Player 1 is winner")
            elif PointsForC2 > PointsForP1 and PointsForC2 > PointsForC1 and PointsForP2 < PointsForC2:
                print("Automated Player 2 is winner")
            else:
                print("it is a tie")
            Re = input("y to play again \n any other key to exit")
            if Re == "y":
                NoOfTimes = 10
                PointsForP1 = 0
                PointsForC1 = 0
                PointsForP2 = 0
                PointsForC2 = 0
                continue
            else:
                break
elif getInput == 2:
    print(" -----------------------------------------------------------------------\n "
          " ---------------------------- GUIDE - 1 --------------------------------\n "
          " -----------------------------------------------------------------------\n "
          "This game is of 10 rounds."
          "\n It is basically a 2 player number game. "
          "\n Before each round some function is displayed. "
          "\n The function has four even variables under 50. "
          "\n Amongst four, two variables are entered by the two real time offline players."
          "\n Players are also given four possible range to try their luck."
          "\n While the rest two variables are chosen automatically and randomly."
          "\n All the variables are placed in the function differently for both players."
          "\n If the result of function for given variables falls in the range chosen by player, player wins the round."
          "\n Player to win maximum no. of rounds will win the game.")
else:
    print("invalid input")