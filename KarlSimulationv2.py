#← ↑ → ↓ ➲ ① ② ③ ④ ⑤ ⑥ ⑦ ⑧ ⑨ ⑩ ⑪ ⑫ ⑬ ⑭ ⑮ ⑯ ⑰ ⑱ ⑲ ⑳ ㉑ ㉒ ㉓ ㉔ ㉕ ㉖ ㉗ ㉘ ㉙ ㉚ ㉛ ㉜ ㉝ ㉞ ㉟ ㊱ ㊲ ㊳ ㊴ ㊵ ㊶ ㊷ ㊸ ㊹ ㊺ ㊻ ㊼ ㊽ ㊾ ㊿"
import os
import time
import csv
os.system("clear")

listL = []
listW = []
listS = []
ball = []
wall = []
wallS = []
keys = 0
key = []
door = []
portal_1 = []
portal_2 = []
belt = []
x = 0
y = 4
RunSpeed = 0.5
lenght = 20
width = 5
dir = 90

def loadLevel(level):
    global wall
    global wallS
    global ball
    global wallS
    global key
    global door
    global lenght
    global width
    global portal_1
    global portal_2
    if not (len(portal_1) == len(portal_2)):
        print("Failed to load level due to portal unable to linked.")
        quit()
    if level == 1:
        ball = [[1,3,1],[8,1,1]]
        wall = [[0,3],[0,2],[1,2],[2,2],[2,3],[7,3],[7,2],[8,2],[9,2],[9,3]]
        wallS = [[2,4],[7,4],[7,0],[7,1]]
        width = 5
        lenght = 10
    if level == 2:
        width = 5
        lenght = 5
        wall = [[3,0],[1,1],[3,1],[0,3],[1,3],[3,3],[4,3],[1,2]]
        ball = [[0,2,1]]
        key = [[4,4]]
        door = [[0,0]]
    if level == 3:
        width = 5
        lenght = 5
        wall = [[3,0],[3,1],[4,1]]
        portal_1 = [[4,2],[0,0],[0,1],[1,0],[2,0],[0,2],[1,1],[2,1],[1,2],[0,3],[0,4]]
        portal_2 = [[4,0],[2,2],[3,3],[4,4],[1,4],[3,4],[3,2],[4,3],[2,4],[2,3],[1,3]]
def updateCanvas(l, w, kx, ky):
    global listL
    global listW
    global listS
    global x
    global y
    listL = []
    listW = []
    listS = []
    with open('pos.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for i in range (l):
            if i == kx:
                listS.append('K')
                listL.append(0)
            else:
                listS.append(0)
                listL.append(0)
        listS.append('+')
        listL.append('+')
        for i in range (w):
            if i == ky:
                writer.writerow(listS)
            else:
                writer.writerow(listL)
        x = kx
        y = ky        
        os.system("clear")

def updateBall():
    global ball
    global key
    global x
    global y
    r = csv.reader(open('pos.csv')) # Here your csv file
    lines = list(r)
    for i in range (len(ball)):
        if not (ball[i][1] == y and ball[i][0] == x):
            lines[ball[i][1]][ball[i][0]] = ball[i][2]
    i = 0
    for i in range (len(key)):
        if not (key[i][1] == y and key[i][0] == x):
            lines[key[i][1]][key[i][0]] = 'L'
    with open('pos.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(lines)

def updateWall():
    global wall
    global wallS
    global door
    global x
    global y
    global keys

    r = csv.reader(open('pos.csv')) # Here your csv file
    lines = list(r)
    i = 0
    for i in range (len(wall)):
        lines[wall[i][1]][wall[i][0]] = "-"
    for i in range (len(door)):
        lines[door[i][1]][door[i][0]] = "|"
    for i in range (len(wallS)):
        if not (wallS[i][0] == x and wallS[i][1] == y):
            lines[wallS[i][1]][wallS[i][0]] = "="
    for i in range (len(portal_1)):
        if not (portal_1[i][0] == x and portal_1[i][1] == y):
            lines[portal_1[i][1]][portal_1[i][0]] = "*"
        if not (portal_2[i][0] == x and portal_2[i][1] == y):
            lines[portal_2[i][1]][portal_2[i][0]] = "*"
    with open('pos.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(lines)
    i = 0
    if [x, y] in wallS:
        wall.append([x,y])
        wallS.remove([x, y])
    if [x, y] in door:
        if keys > 0:
            door.remove([x, y])
            keys -= 1
def printCanvas():
    current = ""
    Clist = []
    global dir
    global lenght
    global width
    global keys
    with open('pos.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            Clist.append(row)
    for i in range (len(str(Clist))):
            if str(Clist)[i-1] == "K":
                if dir == 90:
                    current = current + "→"
                if dir == -90:
                    current = current + "←"
                if dir == 0:
                    current = current + "↑"
                if abs(dir) == 180:
                    current = current + "↓"
            elif str(Clist)[i-1] == "0":
                current = current + "·"
            elif str(Clist)[i-1] == "1":
                current = current + "①"
            elif str(Clist)[i-1] == "2":
                current = current + "②"
            elif str(Clist)[i-1] == "3":
                current = current + "③"
            elif str(Clist)[i-1] == "4":
                current = current + "④"
            elif str(Clist)[i-1] == "5":
                current = current + "⑤"
            elif str(Clist)[i-1] == "6":
                current = current + "⑥"
            elif str(Clist)[i-1] == "7":
                current = current + "⑦"
            elif str(Clist)[i-1] == "8":
                current = current + "⑧"
            elif str(Clist)[i-1] == "9":
                current = current + "⑨"
            elif str(Clist)[i-1] == "10":
                current = current + "⑩"
            elif str(Clist)[i-1] == "11":
                current = current + "⑪"
            elif str(Clist)[i-1] == "12":
                current = current + "⑫"
            elif str(Clist)[i-1] == "13":
                current = current + "⑬"
            elif str(Clist)[i-1] == "14":
                current = current + "⑭"
            elif str(Clist)[i-1] == "15":
                current = current + "⑮"
            elif str(Clist)[i-1] == "16":
                current = current + "⑯"
            elif str(Clist)[i-1] == "17":
                current = current + "⑰"
            elif str(Clist)[i-1] == "18":
                current = current + "⑱"
            elif str(Clist)[i-1] == "19":
                current = current + "⑲"
            elif str(Clist)[i-1] == "20":
                current = current + "⑳"
            elif str(Clist)[i-1] == "21":
                current = current + "㉑"
            elif str(Clist)[i-1] == "22":
                current = current + "㉒"
            elif str(Clist)[i-1] == "23":
                current = current + "㉓"
            elif str(Clist)[i-1] == "24":
                current = current + "㉔"
            elif str(Clist)[i-1] == "25":
                current = current + "㉕"
            elif str(Clist)[i-1] == "26":
                current = current + "㉖"
            elif str(Clist)[i-1] == "27":
                current = current + "㉗"
            elif str(Clist)[i-1] == "28":
                current = current + "㉘"
            elif str(Clist)[i-1] == "29":
                current = current + "㉙"
            elif str(Clist)[i-1] == "30":
                current = current + "㉚"
            elif str(Clist)[i-1] == "31":
                current = current + "㉛"
            elif str(Clist)[i-1] == "32":
                current = current + "㉜"
            elif str(Clist)[i-1] == "33":
                current = current + "㉝"
            elif str(Clist)[i-1] == "34":
                current = current + "㉞"
            elif str(Clist)[i-1] == "35":
                current = current + "㉟"
            elif str(Clist)[i-1] == "36":
                current = current + "㊱"
            elif str(Clist)[i-1] == "37":
                current = current + "㊲"
            elif str(Clist)[i-1] == "38":
                current = current + "㊳"
            elif str(Clist)[i-1] == "39":
                current = current + "㊴"
            elif str(Clist)[i-1] == "40":
                current = current + "㊵"
            elif str(Clist)[i-1] == "41":
                current = current + "㊶"
            elif str(Clist)[i-1] == "42":
                current = current + "㊷"
            elif str(Clist)[i-1] == "43":
                current = current + "㊸"
            elif str(Clist)[i-1] == "44":
                current = current + "㊹"
            elif str(Clist)[i-1] == "45":
                current = current + "㊺"
            elif str(Clist)[i-1] == "46":
                current = current + "㊻"
            elif str(Clist)[i-1] == "47":
                current = current + "㊼"
            elif str(Clist)[i-1] == "48":
                current = current + "㊽"
            elif str(Clist)[i-1] == "49":
                current = current + "㊾"
            elif str(Clist)[i-1] == "50":
                current = current + "㊿"
            elif str(Clist)[i-1] == "+":
                current = current + "\n"
            elif str(Clist)[i-1] == "-":
                current = current + "◼"
            elif str(Clist)[i-1] == "=":
                current = current + "⬚"
            elif str(Clist)[i-1] == "|":
                current = current + "⚿"
            elif str(Clist)[i-1] == "L":
                current = current + "ꄗ"
            elif str(Clist)[i-1] == "*":
                current = current + "⧇"
            elif str(Clist)[i-1] == ",":
                pass
            elif str(Clist)[i-1] == "'":
                pass
            else:
                current = current + " "
    print(current)
    print("Keys: " + str(keys))

def reload():
    global x
    global y
    updateCanvas(lenght, width, x, y)
    updateBall()
    updateWall()
    printCanvas()
#Basic code
def move():
    global x
    global y
    global dir
    global width
    global lenght
    global wall
    global door
    global keys
    if dir == 90:
        x += 1
    elif dir == -90:
        x -= 1
    elif dir == 0:
        y -= 1
    elif abs(dir) == 180:
        y += 1
    if x >= lenght or y >= width or y < 0 or x < 0:
        if dir == 90:
            x -= 1
        elif dir == -90:
            x += 1
        elif dir == 0:
            y += 1
        elif dir == 180:
            y -= 1
        time.sleep(RunSpeed)
        print("Error! Karl Crashes into a wall!\n")
        quit()
    elif [x,y] in wall:
        if dir == 90:
            x -= 1
        elif dir == -90:
            x += 1
        elif dir == 0:
            y += 1
        elif dir == 180:
            y -= 1
        time.sleep(RunSpeed)
        print("Error! Karl Crashes into a wall!\n")
        quit()
    elif [x,y] in door:
        if keys < 1:
            if dir == 90:
                x -= 1
            elif dir == -90:
                x += 1
            elif dir == 0:
                y += 1
            elif dir == 180:
                y -= 1
            time.sleep(RunSpeed)
            print("Error! Karl Crashes into a door!\n")
            quit()
        else:
            updateWall()
            time.sleep(RunSpeed)
            os.system("clear")
            reload()
    else:
        time.sleep(RunSpeed)
        os.system("clear")
        reload()

def turn_left():
    global dir
    global x
    global y
    global width
    global lenght
    if abs(dir) == 180:
        dir = 90
    else:
        dir -= 90
    time.sleep(RunSpeed)
    reload()

def put_ball():
    global ball
    global x
    global y
    time.sleep(RunSpeed)
    found = False
    for i in range(1, 9):
        if [x, y, i] in ball:
            ball[ball.index([x, y, i])][2] += 1
            found = True
            break
    if not found:
        ball.append([x, y, 1])
    reload()

def take_ball():
    global ball
    global x
    global y
    time.sleep(RunSpeed)
    for i in range(1, 9):
        if [x, y, i] in ball:
            index = ball.index([x, y, i])
            ball[index][2] -= 1
            if ball[index][2] < 1:
                ball.remove([x, y, 0])
    reload()
#Super Karl code
def turn_right():
    global dir
    global x
    global y
    global width
    global lenght
    if abs(dir) == 180:
        dir = -90
    else:
        dir += 90
    time.sleep(RunSpeed)
    reload()
def turn_around():
    global dir
    global x
    global y
    global width
    global lenght
    if abs(dir) == 180:
        dir = 0
    elif dir == 90:
        dir = -90
    elif dir == 0:
        dir = 180
    elif dir == -90:
        dir = 90
    time.sleep(RunSpeed)
    reload()

#Khoa Mod Code
def take_key():
    global key
    global keys
    global x
    global y
    if [x, y] in key:
        key.remove([x, y])
        keys += 1
    time.sleep(RunSpeed)
    reload()
def portal():
    global x
    global y
    global portal_1
    global portal_2
    if ([x,y] in portal_1):
        index = portal_1.index([x,y])
        x = portal_2[index][0]
        y = portal_2[index][1]
    elif ([x,y] in portal_2):
        index = portal_2.index([x,y])
        x = portal_1[index][0]
        y = portal_1[index][1]
    else:
        print("Karl cannot use a portal because the portal is not even there!")
        quit()
    time.sleep(RunSpeed)
    reload()

#Conditions
def front_is_clear():
    global x
    global y
    global dir
    global width
    global lenght
    global wall
    if (dir == 90 and (x+1 >= lenght or [x+1,y] in wall)) or (abs(dir) == 180 and (y+1 >= width or [x,y+1] in wall)) or (dir == 0 and (y-1 < 0 or [x,y-1] in wall)) or (dir == -90 and (x-1 < 0 or [x-1,y] in wall)):
        return False
    else:
        return True
def left_is_clear():
    global x
    global y
    global dir
    global width
    global lenght
    global wall
    if (dir == 90 and (y-1 >= lenght or [x,y-1] in wall)) or (abs(dir) == 180 and (x+1 >= width or [x+1,y] in wall)) or (dir == 0 and (x-1 < 0 or [x-1,y] in wall)) or (dir == -90 and (y+1 < 0 or [x,y+1] in wall)):
        return False
    else:
        return True
def right_is_clear():
    global x
    global y
    global dir
    global width
    global lenght
    global wall
    if (dir == 90 and (y+1 >= lenght or [x,y+1] in wall)) or (abs(dir) == 180 and (x-1 >= width or [x-1,y] in wall)) or (dir == 0 and (x+1 < 0 or [x+1,y] in wall)) or (dir == -90 and (y-1 < 0 or [x,y-1] in wall)):
        return False
    else:
        return True
    
def facing_north():
    if dir == 0:
        return True
    else:
        return False

def facing_south():
    if abs(dir) == 180:
        return True
    else:
        return False

def facing_east():
    if abs(dir) == 90:
        return True
    else:
        return False

def facing_west():
    if abs(dir) == -90:
        return True
    else:
        return False
    
def balls_present():
    for i in range (len(ball)):
        if ball[i][1] == y and ball[i][0] == x:
            return True
    return False

def front_is_blocked():
    global x
    global y
    global dir
    global width
    global lenght
    global wall
    if (dir == 90 and (x+1 >= lenght or [x+1,y] in wall)) or (abs(dir) == 180 and (y+1 >= width or [x,y+1] in wall)) or (dir == 0 and (y-1 < 0 or [x,y-1] in wall)) or (dir == -90 and (x-1 < 0 or [x-1,y] in wall)):
        return True
    else:
        return False
def left_is_blocked():
    global x
    global y
    global dir
    global width
    global lenght
    global wall
    if (dir == 90 and (y-1 >= lenght or [x,y-1] in wall)) or (abs(dir) == 180 and (x+1 >= width or [x+1,y] in wall)) or (dir == 0 and (x-1 < 0 or [x-1,y] in wall)) or (dir == -90 and (y+1 < 0 or [x,y+1] in wall)):
        return True
    else:
        return False
def right_is_blocked():
    global x
    global y
    global dir
    global width
    global lenght
    global wall
    if (dir == 90 and (y+1 >= lenght or [x,y+1] in wall)) or (abs(dir) == 180 and (x-1 >= width or [x-1,y] in wall)) or (dir == 0 and (x+1 < 0 or [x+1,y] in wall)) or (dir == -90 and (y-1 < 0 or [x,y-1] in wall)):
        return True
    else:
        return False
    
def not_facing_north():
    if dir == 0:
        return False
    else:
        return True

def not_facing_south():
    if abs(dir) == 180:
        return False
    else:
        return True

def not_facing_east():
    if abs(dir) == 90:
        return False
    else:
        return True

def not_facing_west():
    if abs(dir) == -90:
        return False
    else:
        return True
    
def no_balls_present():
    for i in range (len(ball)):
        if ball[i][1] == y and ball[i][0] == x:
            return False
    return True


#developer
def loadSolution(level):
    if level == 1:
        move()
        turn_left()
        move()
        take_ball()
        turn_around()
        move()
        turn_left()
        move()
        move()
        turn_left()
        move()
        move()
        move()
        move()
        turn_right()
        move()
        move()
        move()
        move()
        move()
        turn_right()
        move()
        take_ball()
        turn_right()
        move()
        move()
        turn_left()
        move()
        move()
        move()
        turn_left()
        move()
        move()
        turn_left()
        move()
        put_ball()
        put_ball()
        turn_around()
        move()
        turn_left()
        move()
    if level == 2:
        move()
        move()
        move()
        move()
        take_key()
        turn_around()
        move()
        move()
        turn_right()
        move()
        move()
        move()
        move()
        turn_left()
        move()
        move()
        turn_left()
        move()
        move()
        take_ball()
        turn_around()
        move()
        move()
        turn_right()
        move()
        move()
        turn_right()
        move()
        move()
        turn_left()
        move()
        move()
        turn_left()
        move()
        move()
        put_ball()
        turn_around()
        move()
        move()
        turn_right()
        move()
        move()
        turn_left()
        move()
        move()
        turn_left()
        move()
        move()
    if level == 3:
        move()
        move()
        move()
        move()
        turn_left()
        move()
        move()
        portal()
        turn_right()
def levelCheck(level):
    solution = []
    with open('pos.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            solution.append(row)
    if level == 1:
        if solution == [['0', '0', '0', '0', '0', '0', '0', '-', '0', '0', '+'], ['0', '0', '0', '0', '0', '0', '0', '-', '0', '0', '+'], ['-', '-', '-', '0', '0', '0', '0', '-', '-', '-', '+'], ['-', '0', '-', '0', '0', '0', '0', '-', '2', '-', '+'], ['0', '0', '-', '0', '0', '0', '0', '-', '0', 'K', '+']]:
            print("You pass the level!!!")
        else:
            print("You failed, restart!")
    if level == 2:
        if solution == [['0', '0', '0', '-', '1', '+'], ['0', '-', '0', '-', '0', '+'], ['0', '-', '0', '0', '0', '+'], ['-', '-', '0', '-', '-', '+'], ['0', '0', '0', '0', 'K', '+']]:
            print("You pass the level!!!")
        else:
            print("You failed, restart!")
    if level == 3:
        if solution == [['*', '*', '*', '-', 'K', '+'], ['*', '*', '*', '-', '-', '+'], ['*', '*', '*', '*', '*', '+'], ['*', '*', '*', '*', '*', '+'], ['*', '*', '*', '*', '*', '+']]:
            print("You pass the level!!!")
        else:
            print("You failed, restart!")  
def printSolution():
    solution = []
    with open('pos.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            solution.append(row)
    print(solution)
