#Game choice
#the availbale games: Snake game, Tron, Pac man, Memory, Tiles
#Games can be accessed through choice
print(" Welcome to Game Choice")
print("The Availabe games:")
print(" 1. Snake Game")
print(" 2.Pac Man")
print(" 3.Memory game")
print(" 4.Tron")
print(" 5.Tiles")
while True:
    a=int(input("Enter the choice for the game required"))
    if a==1:
        #SNAKE GAME 
        from random import randrange
        from turtle import *

        from freegames import square, vector

        food = vector(0, 0)
        snake = [vector(10, 0)]
        aim = vector(0, -10)


        def change(x, y):
           "Change snake direction."
           aim.x = x
           aim.y = y


        def inside(head):
           "Return True if head inside boundaries."
           return -200 < head.x < 190 and -200 < head.y < 190


        def move():
           "Move snake forward one segment."
           head = snake[-1].copy()
           head.move(aim)

           if not inside(head) or head in snake:
               square(head.x, head.y, 9, 'red')
               update()
               return

           snake.append(head)

           if head == food:
               print('Snake:', len(snake))
               food.x = randrange(-15, 15) * 10
               food.y = randrange(-15, 15) * 10
           else:
               snake.pop(0)

           clear()

           for body in snake:
               square(body.x, body.y, 9, 'black')

           square(food.x, food.y, 9, 'green')
           update()
           ontimer(move, 100)


        setup(420, 420, 370, 0)
        hideturtle()
        tracer(False)
        listen()
        onkey(lambda: change(10, 0), 'Right')
        onkey(lambda: change(-10, 0), 'Left')
        onkey(lambda: change(0, 10), 'Up')
        onkey(lambda: change(0, -10), 'Down')
        move()
        done()
        break
    elif a==2:
        #PAC MAN
        from random import choice
        from turtle import *

        from freegames import floor, vector

        state = {'score': 0}
        path = Turtle(visible=False)
        writer = Turtle(visible=False)
        aim = vector(5, 0)
        pacman = vector(-40, -80)
        ghosts = [
            [vector(-180, 160), vector(5, 0)],
            [vector(-180, -160), vector(0, 5)],
            [vector(100, 160), vector(0, -5)],
            [vector(100, -160), vector(-5, 0)],
        ]
        # fmt: off
        tiles = [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
            0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        ]
        # fmt: on


        def square(x, y):
            "Draw square using path at (x, y)."
            path.up()
            path.goto(x, y)
            path.down()
            path.begin_fill()

            for count in range(4):
                path.forward(20)
                path.left(90)

            path.end_fill()


        def offset(point):
            "Return offset of point in tiles."
            x = (floor(point.x, 20) + 200) / 20
            y = (180 - floor(point.y, 20)) / 20
            index = int(x + y * 20)
            return index


        def valid(point):
            "Return True if point is valid in tiles."
            index = offset(point)

            if tiles[index] == 0:
               return False

            index = offset(point + 19)

            if tiles[index] == 0:
               return False

            return point.x % 20 == 0 or point.y % 20 == 0


        def world():
            "Draw world using path."
            bgcolor('black')
            path.color('blue')

            for index in range(len(tiles)):
                tile = tiles[index]

                if tile > 0:
                   x = (index % 20) * 20 - 200
                   y = 180 - (index // 20) * 20
                   square(x, y)

                   if tile == 1:
                       path.up()
                       path.goto(x + 10, y + 10)
                       path.dot(2, 'white')


        def move():
             "Move pacman and all ghosts."
             writer.undo()
             writer.write(state['score'])

             clear()

             if valid(pacman + aim):
                 pacman.move(aim)

             index = offset(pacman)

             if tiles[index] == 1:
                 tiles[index] = 2
                 state['score'] += 1
                 x = (index % 20) * 20 - 200
                 y = 180 - (index // 20) * 20
                 square(x, y)

             up()
             goto(pacman.x + 10, pacman.y + 10)
             dot(20, 'yellow')

             for point, course in ghosts:
                 if valid(point + course):
                     point.move(course)
                 else:
                     options = [
                         vector(5, 0),
                         vector(-5, 0),
                         vector(0, 5),
                         vector(0, -5),
                     ]
                     plan = choice(options)
                     course.x = plan.x
                     course.y = plan.y

                 up()
                 goto(point.x + 10, point.y + 10)
                 dot(20, 'red')

             update()

             for point, course in ghosts:
                 if abs(pacman - point) < 20:
                     return

             ontimer(move, 100)


        def change(x, y):
            "Change pacman aim if valid."
            if valid(pacman + vector(x, y)):
                aim.x = x
                aim.y = y


        setup(420, 420, 370, 0)
        hideturtle()
        tracer(False)
        writer.goto(160, 160)
        writer.color('white')
        writer.write(state['score'])
        listen()
        onkey(lambda: change(5, 0), 'Right')
        onkey(lambda: change(-5, 0), 'Left')
        onkey(lambda: change(0, 5), 'Up')
        onkey(lambda: change(0, -5), 'Down')
        world()
        move()
        done()
        break
    elif a==3:
        #MEMORY GAME
        from random import *
        from turtle import *

        from freegames import path

        car = path('car.gif')
        tiles = list(range(32)) * 2 
        state = {'mark': None}
        hide = [True] * 64


        def square(x, y):
            "Draw white square with black outline at (x, y)."
            up()
            goto(x, y)
            down()
            color('black', 'white')
            begin_fill()
            for count in range(4):
                forward(50)
                left(90)
                end_fill()


        def index(x, y):
            "Convert (x, y) coordinates to tiles index."
            return int((x + 200) // 50 + ((y + 200) // 50) * 8)


        def xy(count):
            "Convert tiles count to (x, y) coordinates."
            return (count % 8) * 50 - 200, (count // 8) * 50 - 200


        def tap(x, y):
            "Update mark and hidden tiles based on tap."
            spot = index(x, y)
            mark = state['mark']

            if mark is None or mark == spot or tiles[mark] != tiles[spot]:
                state['mark'] = spot
            else:
                hide[spot] = False
                hide[mark] = False
                state['mark'] = None


        def draw():
            "Draw image and tiles."
            clear()
            goto(0, 0)
            shape(car)
            stamp()

            for count in range(64):
                if hide[count]:
                    x, y = xy(count)
                    square(x, y)

            mark = state['mark']

            if mark is not None and hide[mark]:
                x, y = xy(mark)
                up()
                goto(x + 2, y)
                color('black')
                write(tiles[mark], font=('Arial', 30, 'normal'))

            update()
            ontimer(draw, 100)


        shuffle(tiles)
        setup(420, 420, 370, 0)
        addshape(car)
        hideturtle()
        tracer(False)
        onscreenclick(tap)
        draw()
        done()
        break
    elif a==4:
        #TRON
        from turtle import *

        from freegames import square, vector

        p1xy = vector(-100, 0)
        p1aim = vector(4, 0)
        p1body = set()

        p2xy = vector(100, 0)
        p2aim = vector(-4, 0)
        p2body = set()


        def inside(head):
            "Return True if head inside screen."
            return -200 < head.x < 200 and -200 < head.y < 200


        def draw():
            "Advance players and draw game."
            p1xy.move(p1aim)
            p1head = p1xy.copy()

            p2xy.move(p2aim)
            p2head = p2xy.copy()

            if not inside(p1head) or p1head in p2body:
                print('Player blue wins!')
                return

            if not inside(p2head) or p2head in p1body:
                print('Player red wins!')
                return

            p1body.add(p1head)
            p2body.add(p2head)

            square(p1xy.x, p1xy.y, 3, 'red')
            square(p2xy.x, p2xy.y, 3, 'blue')
            update()
            ontimer(draw, 50)


        setup(420, 420, 370, 0)
        hideturtle()
        tracer(False)
        listen()
        onkey(lambda: p1aim.rotate(90), 'Right')
        onkey(lambda: p1aim.rotate(-90), 'Left')
        onkey(lambda: p2aim.rotate(90), 'Up')
        onkey(lambda: p2aim.rotate(-90), 'Down')
        draw()
        done()
        break
    elif a==5:
        #TILES
        from random import *
        from turtle import *

        from freegames import floor, vector
  
        tiles = {}
        neighbors = [
            vector(100, 0),
            vector(-100, 0),
            vector(0, 100),
            vector(0, -100),
        ]


        def load():
            "Load tiles and scramble."
            count = 1

            for y in range(-200, 200, 100):
                for x in range(-200, 200, 100):
                    mark = vector(x, y)
                    tiles[mark] = count
                    count += 1

            tiles[mark] = None

            for count in range(1000):
                neighbor = choice(neighbors)
                spot = mark + neighbor

                if spot in tiles:
                   number = tiles[spot]
                   tiles[spot] = None
                   tiles[mark] = number
                   mark = spot


        def square(mark, number):
           "Draw white square with black outline and number."
           up()
           goto(mark.x, mark.y)
           down()

           color('black', 'white')
           begin_fill()
           for count in range(4):
               forward(99)
               left(90)
           end_fill()

           if number is None:
               return
           elif number < 10:
               forward(20)

           write(number, font=('Arial', 60, 'normal'))


        def tap(x, y):
           "Swap tile and empty square."
           x = floor(x, 100)
           y = floor(y, 100)
           mark = vector(x, y)

           for neighbor in neighbors:
               spot = mark + neighbor

               if spot in tiles and tiles[spot] is None:
                   number = tiles[mark]
                   tiles[spot] = number
                   square(spot, number)
                   tiles[mark] = None
                   square(mark, None)


        def draw():
           "Draw all tiles."
           for mark in tiles:
               square(mark, tiles[mark])
           update()


        setup(420, 420, 370, 0) 
        hideturtle()
        tracer(False)
        load()
        draw()
        onscreenclick(tap)
        done()
        break
    else:
        print("Choice not available")
        break

