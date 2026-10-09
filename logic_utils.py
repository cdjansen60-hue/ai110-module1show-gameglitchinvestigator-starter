def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    ranges = {
        "Easy": (1, 20),
        "Normal": (1, 100),
        "Hard": (1, 50),
    }
    return ranges.get(difficulty, (1, 100))


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None or raw.strip() == "":
        return False, None, "Enter a guess."

    candidate = raw.strip()

    try:
        if "." in candidate:
            numeric = float(candidate)
            if not numeric.is_integer():
                raise ValueError
            guess = int(numeric)
        else:
            guess = int(candidate)
    except (TypeError, ValueError):
        return False, None, "That is not a number."

    return True, guess, None


# FIX: compare the guess against the secret correctly so the hint logic matches the actual number.
def check_guess(guess, secret):
    """Compare guess to secret and return the outcome as a string."""
    if guess == secret:
        return "Win"
    if guess > secret:
        return "Too High"
    return "Too Low"


# FIX: keep the score starting at 100 and subtract 10 for every incorrect guess, while leaving the score alone on a win.
def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        return current_score

    if outcome in {"Too High", "Too Low"}:
        return current_score - 10

    return current_score
