import pgzrun

GRID_WIDTH = 16
GRID_HEIGHT = 12
GRID_SIZE = 50
WHIDTH = GRID_WIDTH * GRID_SIZE
HEIGHT = GRID_HEIGHT * GRID_SIZE
pgzrun.go()
def getScreenCoords(x, y):
    return (x * GRID_SIZE, y * GRID_SIZE)
def DrawBackground():
    for y in range (GRID_HEIGHT):
        for x in range (GRID_WIDTH):
            screen.blit("floor1", getScreenCoords (x, y))
def Draw():
    DrawBackground()
pgzrun.go()
MAP = ["WWWWWWWWWWWWWWWW",
       "W              W",
       "W              W",
       "W  W  KG       W",
       "W  WWWWWWWWWW  W",
       "W              W",
       "W      P       W",
       "W  WWWWWWWWWW  W",
       "W      GK   W  W",
       "W              W",
       "W              D",
       "WWWWWWWWWWWWWWWW"]
def getscreencoords(x, y):
    return (x * GRID_SIZE, y * GRID_SIZE)
def drawbackgrounds():
    for y in range (x * GRID_SIZE):
        for x in range (GRID_WIDTH):
            screen.blit("floor1", getScreenCoords(x, y))
def drawscenery():
    for y in range (GRID_HEIGHT):
        for x in range (GRID_WIDTH):
            square = MAP[y] [x]
            if square == "W":
                screen.blit("wall", getScreenCoords(x,y))
            elif square == "D":
                screen.blit("door", getScreenCoords(x,y))


            def draw():
                Screen.clear()
                DrawBackground()
                drawscenery()


