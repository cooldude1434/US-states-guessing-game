import turtle
import pandas

screen = turtle.Screen()

screen.title("US states")

image = "blank_states_img.gif"
screen.addshape(image)



turtle.shape(image)  


data = pandas.read_csv("50_states.csv")

states_list = data["state"].to_list()
guessed_state = []


while len(guessed_state) < 50:
    guess_state = screen.textinput(title=f"{len(guessed_state)}/50",prompt="Whats another state name").title()

    if guess_state == 'Exit':
        missed_state = [state for state in states_list if state not in guessed_state]
        data_dict = pandas.DataFrame(missed_state)
        data_dict.to_csv("states_to_learn.csv")
        break

    if guess_state in states_list:

      t = turtle.Turtle()
      t.hideturtle()
      t.penup()
      state_data =data[data.state == guess_state]
      t.goto(int(state_data.x),int(state_data.y))
      t.write(guess_state)






