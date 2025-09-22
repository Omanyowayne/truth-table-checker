from logic import *

rain = Symbol("rain")
hagrid = Symbol("Hagrid")
dumbledore = Symbol("Dumbledore")

knowledge_base = And(
    Implication(Not(rain), hagrid),
    Or(hagrid, dumbledore),
    Not(And(hagrid, dumbledore)),
    hagrid
)

print(model_check(knowledge_base, hagrid))
