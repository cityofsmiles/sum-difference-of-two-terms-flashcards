

import sympy as sp
import random
import json
import os
import re

# Variables (typical algebra vars)
vars_list = ["a", "b", "c", "m", "n", "p", "q", "x", "y", "z"]

flashcards = []


def format_poly(expr):
    """Format polynomial into a nice string."""
    terms = []
    for term in expr.as_ordered_terms():
        coef, factors = term.as_coeff_Mul()

        if factors == 1:  # pure constant
            terms.append(str(coef))
            continue

        # extract vars
        vars = []
        if isinstance(factors, sp.Symbol):
            vars = [(str(factors), 1)]
        elif isinstance(factors, sp.Pow):
            base, exp = factors.as_base_exp()
            vars = [(str(base), int(exp))]
        else:
            for f in factors.as_ordered_factors():
                if isinstance(f, sp.Symbol):
                    vars.append((str(f), 1))
                elif isinstance(f, sp.Pow):
                    base, exp = f.as_base_exp()
                    vars.append((str(base), int(exp)))

        var_str = "".join([f"{v}" if e == 1 else f"{v}^{e}" for v, e in vars])

        if coef == 1:
            coef_str = ""
        elif coef == -1:
            coef_str = "-"
        else:
            coef_str = str(coef)

        terms.append(coef_str + var_str)

    # join with spacing
    s = " + ".join(terms)
    s = s.replace("+ -", "- ")
    return s


def pick_vars():
    """Pick two distinct variables, return them in alphabetical order."""
    v1, v2 = random.sample(vars_list, 2)
    return tuple(sorted([sp.Symbol(v1), sp.Symbol(v2)], key=lambda s: str(s)))


def generate_case(case_type):
    x, y = pick_vars()  # alphabetically ordered

    if case_type == 1:
        # (x + b)(x - b)
        b = random.randint(1, 9)
        q = f"({x} + {b})({x} - {b})"
        ans = format_poly(sp.expand((x + b) * (x - b)))

    elif case_type == 2:
        # (x + by)(x - by)
        b = random.randint(1, 9)
        b_str = "" if b == 1 else str(b)
        q = f"({x} + {b_str}{y})({x} - {b_str}{y})"
        ans = format_poly(sp.expand((x + b * y) * (x - b * y)))

    elif case_type == 3:
        # (ax + b)(ax - b)
        a = random.choice([i for i in range(-9, 10) if i != 0])
        b = random.randint(1, 9)
        a_str = "" if a == 1 else ("-" if a == -1 else str(a))
        q = f"({a_str}{x} + {b})({a_str}{x} - {b})"
        ans = format_poly(sp.expand((a * x + b) * (a * x - b)))

    else:  # case_type == 4
        # (ax + by)(ax - by)
        a = random.choice([i for i in range(-9, 10) if i != 0])
        b = random.randint(1, 9)
        a_str = "" if a == 1 else ("-" if a == -1 else str(a))
        b_str = "" if b == 1 else str(b)
        q = f"({a_str}{x} + {b_str}{y})({a_str}{x} - {b_str}{y})"
        ans = format_poly(sp.expand((a * x + b * y) * (a * x - b * y)))

    return {"question": q, "answer": ans}


# Generate 200 flashcards (50 per case)
for case_type in range(1, 5):
    for _ in range(50):
        flashcards.append(generate_case(case_type))

# Save to ./public/flashcards.json
output_dir = os.path.join(os.getcwd(), "public")
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "flashcards.json")

with open(output_path, "w") as f:
    json.dump(flashcards, f, indent=2)

print(f"✅ flashcards.json generated with {len(flashcards)} flashcards at {output_path}")


 