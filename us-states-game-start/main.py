import turtle
import pandas
screen=turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x,y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
states = pandas.read_csv("50_states.csv")
game_is_on=True
guessed = []
score =0
guessed_states = []
all_states = states.state.to_list()
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{score}/50 Guess the State", prompt="What's another state's name").title()

    print(answer_state in all_states)
    if answer_state == "Exit":
        not_known_states= {
            "States to learn": all_states
        }
        not_known_states = pandas.DataFrame(not_known_states)
        not_known_states.to_csv("missed_states.csv")
        break
    if answer_state in all_states:
        guessed = states[states.state == f"{answer_state}"]
        guessed_states.append(answer_state)
        score += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(guessed.x), int(guessed.y))
        t.write(guessed.state.item())

        all_states.remove(f"{answer_state}")

    # if (states.state == f"{answer_state}").any():
    #     guessed.append(states[states.state == f"{answer_state}"])
    #     score += 1
    #     states.drop(axis=0, row=f"{answer_state}", level=1)
    #     # states.pop(states.state == f"{answer_state}")
    print(guessed)






# screen.exitonclick()