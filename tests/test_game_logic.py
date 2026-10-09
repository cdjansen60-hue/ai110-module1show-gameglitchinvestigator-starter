from logic_utils import check_guess, update_score


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_winning_score_keeps_the_current_total():
    assert update_score(100, "Win", 1) == 100
    assert update_score(90, "Win", 2) == 90


def test_wrong_guess_penalizes_every_time():
    assert update_score(100, "Too Low", 1) == 90
    assert update_score(90, "Too High", 2) == 80
    assert update_score(80, "Too High", 10) == 70
