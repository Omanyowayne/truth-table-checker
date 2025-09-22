A Python implementation of propositional logic with model checking to evaluate logical sentences and test entailment.

Features

Define logical sentences using:

Symbol (atomic propositions)

Not (negation)

And (conjunction)

Or (disjunction)

Implication (if–then)

Biconditional (if and only if)

Evaluate sentences against a model (truth assignments).

Perform entailment checking using truth table enumeration.

Automatically extract all symbols in a logical expression.

Pretty-print formulas with logical operators (¬, ∧, ∨, =>, <=>).

Project Structure
logic/
│── logic.py         # Core implementation (Sentence classes + model_check)
│── README.md        # Documentation

Getting Started
1. Clone the repository
git clone https://github.com/your-username/logic-model-checker.git
cd logic-model-checker

2. Run with Python

This project requires Python 3.7+.
You can test it directly in the Python REPL or create your own script.

Usage Examples
Example 1: Defining Symbols
from logic import Symbol, Not, And, Or, Implication, Biconditional, model_check

# Define propositional symbols
P = Symbol("P")
Q = Symbol("Q")

Example 2: Creating Sentences
# Logical sentence: (P ∧ Q)
sentence = And(P, Q)
print(sentence.formula())   # Output: (P) ∧ (Q)

Example 3: Evaluating with a Model
# Model: P = True, Q = False
model = {"P": True, "Q": False}

print(sentence.evaluate(model))  # Output: False

Example 4: Model Checking (Entailment)
# Knowledge base: P => Q
knowledge = Implication(P, Q)

# Query: ¬P ∨ Q
query = Or(Not(P), Q)

# Check if KB entails query
print(model_check(knowledge, query))  # Output: True

How It Works

The model checker works by:

Collecting all symbols in the knowledge base and query.

Enumerating all possible truth assignments (models).

Ensuring that if the knowledge base is true in a model, the query is also true in that model.

Returning True if the query is entailed, otherwise False.

Example Use Cases

Learning propositional logic and truth tables.

Practicing knowledge representation (AI/logic courses).

Building a base for AI reasoning systems.

Future Improvements

Support multiple sentences in the knowledge base.

Implement resolution-based inference.

Add a simple command-line interface (CLI) for interactive use.

License

This project is open-source and available under the MIT License.
