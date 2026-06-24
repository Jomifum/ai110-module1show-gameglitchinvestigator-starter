from logic_utils import check_guess, update_score


def test_guess_higher_than_secret_says_lower():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_guess_lower_than_secret_says_higher():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_correct_guess_wins():
    outcome, _message = check_guess(50, 50)
    assert outcome == "Win"


def test_wrong_guess_subtracts_points():
    # "Too High" on an even attempt must subtract, not reward, points.
    assert update_score(0, "Too High", 2) == -5
    # "Too Low" also subtracts 5 regardless of attempt number.
    assert update_score(0, "Too Low", 2) == -5
    assert update_score(0, "Too Low", 3) == -5
