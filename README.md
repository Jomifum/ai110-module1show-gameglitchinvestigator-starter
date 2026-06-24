# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## Document Your Experience

This project started as an AI-generated guessing game full of bugs. Acting as a
"Game Glitch Investigator," I ran the app via Streamlit, reproduced and logged the
glitches, then used an AI coding assistant to diagnose and repair them.

Bugs found and fixed:
- Reversed hints: a guess higher than the secret incorrectly said "Go HIGHER" instead
  of "Go LOWER" (and vice versa).
- A hidden string-comparison bug that converted the secret to text on even attempts,
  breaking the guess comparison.
- An inconsistent attempts counter that started at 1 but reset to 0, causing an
  off-by-one in "Attempts left."
- An erratic scoring bug where wrong guesses on even attempts added points instead of
  subtracting them.

I refactored the core logic out of app.py into logic_utils.py to separate UI from logic,
then wrote pytest cases to verify each fix and guard against regressions.

### Demo Walkthrough

A sample game on Normal difficulty (range 1–100), secret number 74:

1. User guesses 23 → "📈 Go HIGHER!" (below the secret)
2. User guesses 50 → "📈 Go HIGHER!" (still below)
3. User guesses 75 → "📉 Go LOWER!" (just above)
4. User guesses 66 → "📈 Go HIGHER!"
5. User guesses 70 → "📈 Go HIGHER!"
6. User guesses 74 → "🎉 Correct!" — game ends with a win

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
