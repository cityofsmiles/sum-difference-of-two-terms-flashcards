# Sum and Difference of Two Terms Flashcards

This is a web app for practicing the **product of the sum and difference
of two terms** in algebra.\
It is hosted at:
<https://cityofsmiles.github.io/sum-difference-of-two-terms-flashcards>

## Overview

This project uses a **Python + React hybrid approach**:

-   **Python (backend, offline)**\
    Generates flashcards using [Sympy](https://www.sympy.org).\
    All expressions are pre-expanded and simplified to ensure
    correctness.\
    The generated flashcards are saved in `public/flashcards.json`.

-   **React (frontend, online)**\
    Loads flashcards from the JSON file.\
    Displays interactive cards with smooth animations.\
    Collects user input, checks answers against the pre-generated
    solutions, and gives instant feedback.

## Flashcard Content

Each flashcard is based on the difference of squares identity:

**(A + B)(A - B) = AÂ² - BÂ²**

Four cases are included:

1.  **(x + b)(x - b)**\
    Example: (x + 2)(x - 2) = xÂ² - 4

2.  **(x + by)(x - by)**\
    Example: (x + 4y)(x - 4y) = xÂ² - 16yÂ²

3.  **(ax + b)(ax - b)**\
    Example: (3x + 2)(3x - 2) = 9xÂ² - 4

4.  **(ax + by)(ax - by)**\
    Example: (3x + 2y)(3x - 2y) = 9xÂ² - 4yÂ²

### Rules for coefficients and variables

-   `a` is an integer from -9 to 9, excluding 0.
    -   Hidden when equal to 1.\
-   `b` is an integer from 1 to 9.
    -   Hidden when equal to 1 as a coefficient, always shown when
        constant.\
-   Variables are selected from `{a, b, c, m, n, p, q, x, y, z}`.\
-   Two variables are always ordered alphabetically.

## How It Works

1.  Run `generate_flashcards.py` to generate `flashcards.json` (200
    flashcards, 50 per case).\
2.  The React app fetches this JSON file.\
3.  A random set of 10 flashcards is selected for each session.\
4.  User inputs are compared with the correct answer string (after
    removing spaces and lowercasing).\
5.  The app shows a score and answer key at the end.

## Development Setup

### Backend (Python)

Requirements: - Python 3.8+ - `sympy`

To generate new flashcards:

``` bash
python generate_flashcards.py
```

This creates `public/flashcards.json`.

### Frontend (React)

Requirements: - Node.js 16+

Install dependencies:

``` bash
npm install
```

Run locally:

``` bash
npm run dev
```

Build for GitHub Pages:

``` bash
npm run build
```

Then push the `dist` folder to the `gh-pages` branch.

## Credits

Created by **Jonathan R. Bacolod, LPT**\
Designed for students practicing algebraic identities.