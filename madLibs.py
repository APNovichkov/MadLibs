#!/usr/bin/env python


order_of_parts_of_speech = ["noun", "noun", "adjective", "adjective", "verb", "verb", "verb",
                            "noun", "adjective", "verb"]
number_of_user_inputs = len(order_of_parts_of_speech)
user_inputs = []


def get_user_input(user_inputs):
    for i in range(number_of_user_inputs):
        user_inputs.append(raw_input("Enter a " + order_of_parts_of_speech[i] + "\n"))


get_user_input(user_inputs)

print("I was walking down the road with " + user_inputs[0] + " and " + user_inputs[1] +
      " and then I stopped, I was flabbergasted at the " + user_inputs[2] + " view that before my very own eyes. It was a matted out, "
      + user_inputs[3] + ", old lamborghini. I " + user_inputs[4] + " towards my dream car, " + user_inputs[5]
      + " inside of it, and " + user_inputs[6] + " its sporty seats. I was about to push the start button, when "
      + user_inputs[7] + " walked up to me, and said in a cold, " + user_inputs[8]
      + " voice, WHAT THE HELL DO YOU THINK YOU ARE DOING, I AM GOING TO " + user_inputs[9] + " YOUU!!!! End of story :)")

# example madLib paragraph
# I was walking down the road with <noun>, when I saw <noun>. I was flabbergasted at the
# <adjective> view that before my very own eyes. It was a matted out, <adjective>, old
# lamborghini. I <verb> towards my dream car, <verb> inside of it, and <verb> its sporty
# seats. I was about to push the start button, when <noun> walked up to me, and
# said in a cold, <adjective> voice, WHAT THE HELL DO YOU THINK YOU ARE DOING, I AM GOING
# TO <verb> YOUU!!!! End of story ;)
