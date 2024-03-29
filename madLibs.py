#!/usr/bin/env python


def get_user_input(user_inputs, order_of_parts_of_speech):
    for i in range(len(order_of_parts_of_speech)):
        input_completed = False
        while not input_completed:
            user_input = input("Enter a " + order_of_parts_of_speech[i] + "\n")
            if validate_user_input(user_input):
                user_inputs.append(user_input)
                input_completed = True


def validate_user_input(user_input):
    return len(user_input) > 0 and user_input.isalpha()


def main():
    order_of_parts_of_speech = ["noun", "noun", "adjective", "adjective", "verb(past tense, ex: walked)",
                                "verb(past tense, ex: walked)", "verb(past tense, ex: walked)", "noun", "pronoun",
                                "adjective", "verb(present tence, ex: walk"]
    user_inputs = []

    get_user_input(user_inputs, order_of_parts_of_speech)

    print("Here is your story! Enjoy ;)")
    print("--------------------------------------------------------------------------------------------------------------------------------")
    print("I was walking down the road with " + user_inputs[0] + " and " + user_inputs[1] +
          " and then I stopped, I was flabbergasted at the " + user_inputs[2] + " view that before my very own eyes.\nIt was a matted out, "
          + user_inputs[3] + ", old lamborghini. I " + user_inputs[4] + " towards my dream car, " + user_inputs[5]
          + " inside of it, and " + user_inputs[6] + " on its sporty seats.\nI was about to push the start button, when "
          + user_inputs[7] + " walked up to me, and " + user_inputs[8] + " said in a cold, " + user_inputs[9]
          + " voice, WHAT THE HELL DO YOU THINK YOU ARE DOING,\nI AM GOING TO " + user_inputs[10] + " YOUU!!!! End of story :)")


if __name__ == "__main__":
    main()

# example madLib paragraph
# I was walking down the road with <noun>, when I saw <noun>. I was flabbergasted at the
# <adjective> view that before my very own eyes. It was a matted out, <adjective>, old
# lamborghini. I <verb> towards my dream car, <verb> inside of it, and <verb> its sporty
# seats. I was about to push the start button, when <noun> walked up to me, and
# said in a cold, <adjective> voice, WHAT THE HELL DO YOU THINK YOU ARE DOING, I AM GOING
# TO <verb> YOUU!!!! End of story ;)
