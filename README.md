# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable.

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? The fix is to store the value in `st.session_state` so it survives reruns.
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. The comparison logic needs to compare the guess correctly against the secret number.
4. **Refactor & Test.** Move the core game logic into `logic_utils.py`, then run `pytest` until all tests pass.

## 📝 What I Fixed

This project was a debugging exercise in which the AI-generated game had several logic and state bugs. I repaired the app so that it keeps a stable secret number across reruns, the hints reflect the correct relationship between the guess and the secret, the first valid guess counts toward the total attempt count, and the score starts at 100 and decreases by 10 for each incorrect guess. I also fixed the history display so each guess appears immediately after submission and the final score is shown correctly when the game ends.

## 📸 Demo Walkthrough

1. Open the app in Streamlit and select a difficulty level from the sidebar.
2. Enter a guess in the input box and press Submit Guess.
3. The app compares the number to the secret and displays a correct hint such as "Go HIGHER!" or "Go LOWER!".
4. Each wrong guess reduces the score by 10, and the total score remains visible in the UI.
5. The game records the guess history immediately and ends when the secret is found or the attempt limit is reached.
6. After a win, the app shows the final score and keeps the current score total intact instead of resetting or going negative.

**Screenshot** *(optional)*: Not included in this version.

## 🧪 Test Results

```bash
pytest tests/
======================== 5 passed in 0.02s ========================
```

## 🚀 Stretch Features

- No stretch feature was added in this version.
- The core fix was focused on reliable Streamlit state management, correct comparison logic, and score/attempt behavior.
