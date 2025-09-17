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
factor(908797, )