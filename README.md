# Logic Model Checker

**A Python implementation of propositional logic with model checking to evaluate logical sentences and test entailment.**

This repository includes the **core logic engine** (`logic.py`) and **example programs** (`mastermind.py`, `harrison.py`) that demonstrate how to use it in real reasoning problems.

---

##  Features

* Define logical sentences with:

  * **Symbol** (atomic propositions)
  * **Not** (negation)
  * **And** (conjunction)
  * **Or** (disjunction)
  * **Implication** (if–then)
  * **Biconditional** (if and only if)
* Evaluate logical sentences against truth assignments (models).
* Perform **entailment checking** using truth table enumeration.
* Pretty-print logical formulas with operators (`¬`, `∧`, `∨`, `=>`, `<=>`).
* Includes **demo programs** showing logic in action.

---

##  Project Structure

```
logic-model-checker/
│── logic.py          # Core logic engine
│── mastermind.py     # Example: Clue-style deduction puzzle
│── harrison.py       # Example: Simple reasoning with Harry Potter characters
│── README.md         # Documentation
```

---

##  Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/logic-model-checker.git
cd logic-model-checker
```

### 2. Install dependencies

```bash
pip install termcolor
```

### 3. Run the examples

```bash
python mastermind.py
python harrison.py
```

---

##  Usage

### Example 1: Core Logic (from `logic.py`)

```python
from logic import Symbol, Not, And, Or, Implication, Biconditional, model_check

P = Symbol("P")
Q = Symbol("Q")

knowledge = Implication(P, Q)
query = Or(Not(P), Q)

print(model_check(knowledge, query))  # Output: True
```

---

### Example 2: Clue-Style Puzzle (`mastermind.py`)

This script sets up a logic puzzle like the board game *Clue*:

* Exactly one **character**, one **weapon**, and one **room** is correct.
* Some information is known (cards seen, guesses made).
* The program uses `model_check` to deduce which facts are definitely true or maybe true.

Run it:

```bash
python mastermind.py
```

Output will highlight facts that are logically **entailed** (`YES` in green) or **possible** (`MAYBE`).

---

### Example 3: Reasoning Puzzle (`harrison.py`)

This script encodes a small knowledge base:

* If it’s not raining, Hagrid is outside.
* Either Hagrid or Dumbledore is present (but not both).
* Hagrid is observed.

The script checks whether the knowledge base entails that Hagrid is present:

```bash
python harrison.py
```

Expected output:

```
True
```

---

##  How It Works

* The model checker enumerates all possible truth assignments for symbols.
* It checks that whenever the **knowledge base** is true, the **query** is also true.
* If so, we say the knowledge base *entails* the query.

---

##  Use Cases

* Learn **propositional logic** and **model checking**.
* Practice **knowledge representation** and reasoning.
* Explore AI concepts from courses like **CS50 AI**.

---

##  Future Improvements

* Add support for multiple knowledge bases in one run.
* Implement **resolution-based reasoning**.
* Add CLI or GUI for interactive logic puzzles.

---

##  License

This project is licensed under the **MIT License**.



