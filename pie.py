friend_comes = False
money = False

def or_movies(friend, money):
    if friend and money:
        print("Going to the movies")
    else: 
        print("I have no friends or i have no money")
or_movies(friend_comes, money)

homework = True
def not_movies(homework):
    if not homework:
        print("movie time")
    else:
        print("homework time, I hate russian")
not_movies(homework)

def factor(x,y):
    if x % y == 0:
        print(f"{y} is a factor of {x}")
factor(25, 5)

def factor(x,y):
    if x % y == 0:
        print(f"{y} is a factor of {x}")
    else:
        print("x is not a factor of y")
factor(8568938538, 2)

def factor(x,y):
    if x % y == 0:
        print(f"{x} is an even number")
    else:
        print("x is an odd number")
factor(9,2)

 
def ser(s):
    if s == ("bad") :
            def tip (x):
                print(f"tip= {x}")
            tip(5)
    if s == ("okay"):
        print('15')
    elif s == ("good"):
        print('20')
    elif s == ("great"):
        print('25')
ser("bad")


def ser(s):
    def bill(b):
        if s == ("bad") :
         def tip (x):   
            print(b * x)
            tip(0.05)
        elif s == ("okay"):
            def tip(x):
                    print(b * x)
            tip(0.15)
        elif s == ("good"):
            def tip(x):
                    print(b * x)
            tip(0.20)
        elif s == ("great"):
            def tip(x):
                    print(b * x)
            tip(0.25)
    bill(30)
ser("okay")

min[x,y]
for i in range(x):



