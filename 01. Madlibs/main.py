def madlib():
    

    time_of_day = input("Time of the day: ")
    body_part_plural = input("Body Part (plural) :")
    color = input("color: ")
    verb_past_tense = input("verb (past tense): ")
    food = input("food: ")
    noun1 = input("noun: ")
    noun_plural_1 = input("Noun (plural): ")
    adj1 = input("Adjective: ")
    adj2 = input("Adjective: ")
    adj3 = input("Adjective: ")

    madlib = f"It was a {adj1} summer {time_of_day} when we realized that the vacinne to stop \
spread of the disease did not work. Instead, it produced ZOMBIES!!!, They were thirsty for {body_part_plural} \
and the streets were lined with these monsters holding {noun_plural_1} in their hands.\
Their eyes were {color} with hunger as they {verb_past_tense} around the city looking for {food}. \
They were {adj2} and {adj3}, unknowing how to act in this human world... expect eat {body_part_plural}!!! \
That was thier sole mission and they were dedicated towards achieving it for the sake of {noun1}."
    
    print(madlib)

madlib()