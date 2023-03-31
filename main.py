#turtle race

from turtle import Turtle, Screen
import random

is_race_on = False # do while loop
#########SCREEN SETUP###########
screen = Screen()
screen.setup(width=500, height=400)#ustawienie rozmiaru okna
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')
#title oznacza tytuł okna, promt to w oknie pytanie
print(user_bet)



###########TURTLE SETUP################
# create turtle on start line###
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [-70,-40,-10, 20, 50, 80]
all_turtles = [] #pusta lista na stworzone wszystkie żółwie


# turles has diffrent states: color, starting position,move.forward

for turtle_index in range(0,6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)#dodanie nowego żółwia do listy

##move turtle - while loop - zobacz do góry###

if user_bet:#jeśli zakład usera istnieje
    is_race_on = True #wyścig się rozpoczyna

#stworzenie warunku do while loop
while is_race_on:
    for turtle in all_turtles: # iterowanie po liście żółwi,żeby każdy inaczej się poruszał
        #end of game, reach the edge of the screen- create stopping condition
        if turtle.xcor() > 230: # edge of screen-20px (reach by head of turtle)
            # print(turtle.color()) #złe bo wyświetli dwa kolory-pencolor i fillcolor
            is_race_on = False #koniec wyścigu, bo tak kolejne żółwie będą się wyświetlały
            winning_color = turtle.pencolor() # sprawdzenie kto wygrał
            if winning_color == user_bet:
                print(f'You have won! The {winning_color} turtle is the winner!')
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        #losowy ruch do przodu
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()






##########Exercises###############

# ## create turtle on start line###
# colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
# y_positions = [-70,-40,-10, 20, 50, 80]
# all_arrow = [] #pusta lista na stworzone wszystkie żółwie

# # 0 stworzenie instancji zółwi
# # 1 rozstawienie żółwi do listy y wybieram arrow index
# # 2 wybór koloru
# # 3 dodanie do listy
# # 4 uruchomienie gry - if z warunkiem i while loop
# # 5 iterowanie pożółwaich w liście - ruch żółwi - pętla for po liście all
# # 6 utworzenie randomowego ruchu

# for arrow_index in range(0,6):
#     new_arrow = Turtle(shape='arrow')
#     new_arrow.penup()
#     new_arrow.goto(x=-230, y=y_positions[arrow_index])
#     new_arrow.color(colors[arrow_index])
#     all_arrow.append(new_arrow)

# #utworzenie warunku startu
# if user_bet:
#     is_race_on = True

# # start wyścigu
# while is_race_on:
#     for arrow in all_arrow: 
#         if arrow.xcor()>230:
#             is_race_on = False
#             winnig_color = arrow.pencolor()
#             if winning_color == user_bet:
#                 print(f'You have won! The {winning_color} turtle is the winner!')
#             else:
#                 print(f"You've lost! The {winning_color} turtle is the winner!")
        
#         random_distance = random.randint(0,10)
#         arrow.forward(random_distance)

# screen.exitonclick()