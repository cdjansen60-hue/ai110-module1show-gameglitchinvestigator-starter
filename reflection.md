# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

When I first ran the app, the game looked like a normal number guessing interface, but it was impossible to win because the hidden number was re-randomized on each submit. The hints were also wrong, and the score started at zero instead of 100, which caused incorrect negative values after the first wrong guess. I also noticed that the history did not refresh until the next guess, which made the app feel inconsistent and unreliable.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess 20 after a fresh game | Secret stays the same for that run | Secret changed after clicking Submit | No exception, but the game reset state unexpectedly |
| Guess smaller than secret | "Go HIGHER!" | "Go LOWER!" or opposite message | Hint text contradicted the actual comparison |
| First wrong guess | Score becomes 90 | Score became -10 or started at 0 | Python values were being reset or decremented incorrectly |
| Guess 15, then guess 25 | History shows both guesses immediately | History only updated on the following submit | Session state lagged by one render |

---

## 2. How did you use AI as a teammate?

I used Copilot and the course's AI coding workflow as a debugging partner while I worked through the project. One AI suggestion that was useful was asking for help understanding Streamlit session state, because the explanation helped me see that the secret number needed to be stored instead of re-created on every rerun. I did not accept a suggestion to keep the old score formula because it was tied to a broken indexing model; instead, I adjusted the logic to match a clear rule: start at 100 and subtract 10 for each wrong guess. I verified that fix by running pytest and checking the game behavior against the expected score math.

---

## 3. Debugging and testing your fixes

I decided a bug was fixed when the same scenario could be reproduced and then consistently behaved the way the game logic said it should. I ran pytest on the project after moving the logic into logic_utils.py and it showed the repaired logic was consistent. I also checked the app behavior manually by testing hint direction, score updates, and history updates to confirm that the same guess did not trigger a new secret or delayed UI update. AI helped me design tests by suggesting I check edge cases like incorrect guesses, win conditions, and score progression, which made the verification easier and more trustworthy.

---

## 4. What did you learn about Streamlit and state?

I learned that Streamlit reruns the script every time an interaction happens, so any value that is not stored in session_state can disappear or be recreated. In practice, session state is the place where the game should keep the secret number, attempts, score, and history so the app behaves consistently across clicks. If I explained this to a friend, I would say: each click is a fresh rerun, and session state is the memory that survives between reruns. Without it, the app feels random because it keeps forgetting its previous values.

---

## 5. Looking ahead: your developer habits

One habit I want to reuse is testing the game logic in isolation before trusting a UI fix, because the real bugs were easier to validate in small functions than in the full app. Next time I work with AI, I would start by stating the expected behavior and the exact bug before accepting a code suggestion, so the fix stays focused and traceable. This project changed how I think about AI-generated code because I saw that the generated app was fast to create but inconsistent in state and logic, so human review and automated tests are still essential for reliable software.
