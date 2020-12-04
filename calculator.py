#Calculator GUI

##To Do:
#Update function to handle multiple operations in one go

from guizero import *

#Commands

screen_capture = ""

def clearLists():
    global numbers, operations, screen_capture
    screen_capture = ""
    display.value = screen_capture


def backSpace():
    global screen_capture
    try:
        screen_capture = screen_capture[0:len(screen_capture)-1]
        display.value = screen_capture
    except:
        pass

def getOperator(num1, operator, num2):
    if operator == "+":
        answer = float(num1) + float(num2)
    elif operator == "-":
        answer = float(num1) - float(num2)
    elif operator == "x":
        answer = float(num1) * float(num2)
    elif operator == "÷":
        answer = float(num1) / float(num2)
    elif operator == "P":
        answer = float(num1) ** float(num2)

    return answer

def calculate():
    global numbers, operations, screen_capture
    operators = ["+", "-", "x", "÷", "P"]
    hold = []

    until = len(screen_capture)
    i = 0
    while len(screen_capture) != 1 or screen_capture[len(screen_capture)-1] not in operators:
        if screen_capture[i] in operators:
            number = screen_capture[0:i]

            hold.append(number)
            operator = screen_capture[i]
            hold.append(operator)
            screen_capture = screen_capture[i+1:len(screen_capture)]
            hold.append(screen_capture)
            break
            
        else:
            i += 1

    if len(screen_capture) == 1:
        hold.append(screen_capture)


    
    display.value = getOperator(hold[0], hold[1], hold[2])
    screen_capture = display.value

def screenCapture(obj):
    global screen_capture, display
    obj = str(obj)
    screen_capture += obj
    display.value = screen_capture

#Configure app
app = App("Calculator", height=400, width=500)
#Display Box

displayBox = Box(app, border=True, height=100, width=350)
display = Text(displayBox, text="CodedByJade")

#Numbers Box

numbersBox = Box(app, layout="grid", align="left", height=200, width=175)

one = PushButton(numbersBox, text="1", command=lambda:screenCapture(1) , grid=[0,0])
two = PushButton(numbersBox, text="2", command=lambda:screenCapture(2) , grid=[0,1])
three = PushButton(numbersBox, text="3", command=lambda:screenCapture(3) , grid=[0,2])
four = PushButton(numbersBox, text="4", command=lambda:screenCapture(4) , grid=[1,0])
five = PushButton(numbersBox, text="5", command=lambda:screenCapture(5) , grid=[1,1])
six = PushButton(numbersBox, text="6", command=lambda:screenCapture(6) , grid=[1,2])
seven = PushButton(numbersBox, text="7", command=lambda:screenCapture(7) , grid=[2,0])
eight = PushButton(numbersBox, text="8", command=lambda:screenCapture(8) , grid=[2,1])
nine = PushButton(numbersBox, text="9", command=lambda:screenCapture(9) , grid=[2,2])
zero = PushButton(numbersBox, text="0", command=lambda:screenCapture(0) , grid=[3,0])



#Operators Box

operatorsBox = Box(app, layout="grid", align="right", height=200, width=175)

plus = PushButton(operatorsBox, text="+", command=lambda:screenCapture("+"), grid=[0,0])
minus = PushButton(operatorsBox, text="-", command=lambda:screenCapture("-"), grid=[0,1])
multiply = PushButton(operatorsBox, text="x", command=lambda:screenCapture("x"), grid=[1,0])
divide = PushButton(operatorsBox, text="÷", command=lambda:screenCapture("÷"), grid=[1,1])
indice = PushButton(operatorsBox, text="P", command=lambda:screenCapture("P"), grid=[2,0])


#Input/Output

ioBox = Box(app, layout="grid", align="bottom", height=100,width=350)

clear = PushButton(ioBox, text="CLEAR", command=clearLists, grid=[0,0])
enter = PushButton(ioBox, text="=", command=calculate, grid=[1,0])
delete = PushButton(ioBox, text="DEL", command=backSpace, grid=[2,0])



app.display()
