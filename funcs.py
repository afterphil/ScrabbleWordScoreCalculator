def handle_s_letter_squares(special_square: str, l_score: int):
    """handle letter multipliers
    :param special_square: The special square selected for letter multipliers
    :param l_score: The original letter score"""
    s_score = 0
    match special_square:
        case "DL":
            s_score = l_score * 2
            print(f"{l_score} doubled to {s_score} points")
            return s_score
        case "TL":
            s_score = l_score * 3
            print(f"{l_score} tripled to {s_score} points")
            return s_score
        case _:
            return l_score

def handle_s_word_squares(special_square: str, w_score: int):
    """handle word multipliers
    :param special_square: The special square selected for word multipliers
    :param w_score: The original word score"""
    s_score = 0
    match special_square:
        case "DW":
            s_score = w_score * 2
            print(f"{w_score} doubled to {s_score} points")
            return s_score
        case "TW":
            s_score = w_score * 3
            print(f"{w_score} tripled to {s_score} points")
            return s_score
        case _:
            return w_score

def parse_word(word):
    dict = enumerate(word)
    return dict

def handle_idx(entered_s_letter, entered_word, s_letter_idx):
    if entered_s_letter == list(parse_word(entered_word))[s_letter_idx][s_letter_idx]:
        return s_letter_idx
    else:
        return None


if __name__ == "__main__":
    print(handle_s_letter_squares("DL", 2))
    print(handle_s_letter_squares("TL", 2))
    print(handle_s_word_squares("DW", 10))
    print(handle_s_word_squares("TW", 10))
    print(handle_idx("p", "apple", 1))
