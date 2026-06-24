# 💭 Reflection: Game Glitch Investigator

## 1. What was broken when you started?

The first time I ran the game it loaded fine in the browser and looked polished, but the
logic was clearly broken underneath. The hints pointed the wrong way — guessing 1 (the
lowest possible number) told me to "Go LOWER," which is impossible. The attempt counts
contradicted each other: the sidebar said "Attempts allowed: 8" while the main message
said "Attempts left: 4." And the score drifted negative (down to -20) after a few wrong
guesses, which shouldn't happen.

**Bug Reproduction Log**

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess of 1 (range 1–100) | A hint like "Go HIGHER!" since 1 is the lowest number | Hint said "Go LOWER!" — impossible, nothing is below 1 | none |
| Opened app fresh, before guessing | Sidebar "Attempts allowed: 8" should match "Attempts left" in-game | Sidebar said 8 but main message said "Attempts left: 4" — mismatch | none |
| Several wrong guesses | Score stays at 0 or decreases reasonably; attempts count down from 8 | Score went to -20; Debug "Attempts" showed 5 and climbed instead of counting down | none |

---

## 2. How did you use AI as a teammate?

I used an AI coding assistant inside VS Code as my main teammate, giving it one focused
task at a time and attaching app.py and logic_utils.py so it could see how the UI and
logic files related to each other. I drove the process by writing specific prompts, then
reviewed every diff it produced before accepting it rather than trusting the changes blindly.

One AI suggestion that was correct came during the refactor step. I asked it to remove a
block that converted the secret number to a string on even attempts, but the assistant
correctly recognized that this block no longer existed — the earlier refactor had already
eliminated the string-comparison path when we removed the try/except fallback in
check_guess. Instead of inventing an unnecessary change, it explained that the secret was
already being passed as an integer. I verified this by reading through app.py myself and
confirming there was no % 2 string-conversion block, and by running the game to check the
hints stayed consistent across attempts.

One AI suggestion that was misleading was when the assistant reported "all tests pass" as
if that fully verified the score fix. In reality, the three passing tests only covered
check_guess, not update_score, so the score bug wasn't being tested at all. I caught this
by reading the test file and noticing none of the tests imported update_score. I then had
the AI add a dedicated test, update_score(0, "Too High", 2) == -5, which would have failed
against the old buggy code, and only then did I consider the scoring fix verified. This
taught me that a green test run only proves what the tests actually check.

---

## 3. Debugging and testing your fixes

I decided a bug was really fixed only when it was confirmed two ways: an automated test
that fails against the old code and passes against the new, plus a manual check in the
running game. This kept me from assuming a fix worked just because the app stopped looking
broken.

The clearest example was the scoring bug. I wrote (with the AI's help) a pytest case
asserting that update_score(0, "Too High", 2) returns -5. This mattered because the old
code returned +5 in that case — it rewarded wrong guesses on even attempts, which caused
the score to drift to -20 in Phase 1. Because the test was designed to fail against the
buggy version, its passing result proved the fix worked and guards against regression. I
ran the suite with python -m pytest test/ -v and confirmed all four tests passed. I also
played the live game and watched the score drop by a steady 5 points on each wrong guess.

AI helped me design these tests by generating the initial check_guess cases (guess 60 vs
secret 50 → "Too High"/"Go LOWER") and the update_score case, but I decided what each test
should assert based on the bugs I documented in Phase 1. The AI wrote the test code; I
supplied the expected behavior.

---

## 4. What did you learn about Streamlit and state?

Every time you interact with a Streamlit app — click a button or type in a box — Streamlit
re-runs the entire Python file from the top, like refreshing a page. That means normal
variables get reset every single time, so they can't be used to remember anything between
clicks. st.session_state is special storage that survives those reruns, which is where the
game keeps the things that need to persist: the secret number, the score, and the attempt
count. Several of this game's bugs came from session state being initialized or reset
inconsistently — for example, attempts starting at 1 but resetting to 0 — which is what
caused the off-by-one in the "Attempts left" display.

---

## 5. Looking ahead: your developer habits

One habit I want to reuse is writing a test that fails against the old code before
trusting a fix. Seeing the test catch the exact buggy behavior gave me real confidence the
fix worked, rather than just assuming it did because the app looked fine. I also want to
keep reviewing every AI diff before accepting it and tackling one bug per chat session to
stay focused.

One thing I would do differently next time is not trust a "all tests pass" message until I
have confirmed the tests actually cover the bug in question. I learned that passing tests
only prove what they check, so I need to read the tests, not just the result.

This project changed how I think about AI-generated code: it can look polished and
"production-ready" while being full of logic bugs, so I now treat AI output as a draft to
verify rather than an answer to trust. My job is to stay the decision-maker — accepting,
modifying, or rejecting what the AI produces based on evidence.