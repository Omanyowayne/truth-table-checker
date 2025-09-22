from logic import *

import termcolor

mustard = Symbol("ColMustard")
plum = Symbol("ProfPlum")
scarlet = Symbol("MsScarlet")
characters = [mustard, plum, scarlet]

knife = Symbol("knife")
wrench = Symbol("wrench")
revolver = Symbol("revolver")
weapons = [knife, wrench, revolver]

library = Symbol("library")
ballroom = Symbol("ballroom")
kitchen = Symbol("kitchen")
rooms = [library, ballroom, kitchen]

symbols = weapons + characters + rooms

def check_knowledge(knowledge):
    for symbol in symbols:
        if model_check(knowledge, symbol):
            termcolor.cprint(f"{symbol}: YES", "green")
        elif not model_check(knowledge, Not(symbol)):
            print(f"{symbol}: MAYBE")

knowledge = And(
    # Start with the game conditions: one item in each of the three categories has to be true.
    Or(mustard, plum, scarlet),
    Or(library, ballroom, kitchen),
    Or(knife, wrench, revolver),

    # Add the information from the three initial cards we saw
    Not(mustard),
    Not(knife),
    Not(kitchen),

    # Add the guess someone made that it is Scarlet, who used a wrench in the library
    Or(Not(scarlet), Not(library), Not(wrench)),

    # Add the cards that we were exposed to
    Not(ballroom)
)

knowledge.add(Not(scarlet))
knowledge.add(Not(revolver))

check_knowledge(knowledge)
