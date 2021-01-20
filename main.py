import turtle

class Circuito():
    corredores = []
    __posStartY = (-30, -10, 10, 30)
    __coloTurtle = ('red', "blue", 'green', 'orange')
    
    def __init__(self, width, height):
        self.__screen = turtle.Screen()
        self.__screen.setup(width, height)
        self.__screen.bgcolor('lightgray')
        self.__startLine = -width/2 + 20
        self.__finishLine = width/2 - 20
        
        for i in range(4):
            new_turtle = turtle.Turtle()
            new_turtle.shape('turtle')
            new_turtle.penup()
            new_turtle.setpos(self.__startLine, self.__posStartY[i])
            new_turtle.color(self.__colorTurtle[1])
            
            self.corredores.append(new_turtle)
        






if __name__ == '__mai__':
    circuito = Circuito(640, 480)
        
        