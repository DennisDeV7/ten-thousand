from random import randint


class GameLogic:
    def __init__(self):
        self.head = None

    @staticmethod
    def calculate_score(dice_roll):
        score_board = [
            (tuple(), 0),
            ((1,), 100),
            ((1, 1), 200),
            ((1, 1, 1), 1000),
            ((1, 1, 1, 1), 2000),
            ((1, 1, 1, 1, 1), 3000),
            ((1, 1, 1, 1, 1, 1), 4000),
            ((2,), 0),
            ((2, 2), 0),
            ((2, 2, 2), 200),
            ((2, 2, 2, 2), 400),
            ((2, 2, 2, 2, 2), 600),
            ((2, 2, 2, 2, 2, 2), 800),
            ((3,), 0),
            ((3, 3), 0),
            ((3, 3, 3), 300),
            ((3, 3, 3, 3), 600),
            ((3, 3, 3, 3, 3), 900),
            ((3, 3, 3, 3, 3, 3), 1200),
            ((4,), 0),
            ((4, 4), 0),
            ((4, 4, 4), 400),
            ((4, 4, 4, 4), 800),
            ((4, 4, 4, 4, 4), 1200),
            ((4, 4, 4, 4, 4, 4), 1600),
            ((5,), 50),
            ((5, 5), 100),
            ((5, 5, 5), 500),
            ((5, 5, 5, 5), 1000),
            ((5, 5, 5, 5, 5), 1500),
            ((5, 5, 5, 5, 5, 5), 2000),
            ((6,), 0),
            ((6, 6), 0),
            ((6, 6, 6), 600),
            ((6, 6, 6, 6), 1200),
            ((6, 6, 6, 6, 6), 1800),
            ((6, 6, 6, 6, 6, 6), 2400),
            ((1, 2, 3, 4, 5, 6), 1500),
            ((2, 2, 3, 3, 4, 6), 0),
            ((2, 2, 3, 3, 6, 6), 1500),
            ((1, 1, 1, 2, 2, 2), 1200),
        ]

        for x in score_board:
            if x[0] == dice_roll:
                return x[1]

    @staticmethod
    def roll_dice(num_dice):
        results = []
        for num in range(num_dice):
            roll = randint(1, 6)
            results.append(roll)
        return tuple(results)


if __name__ == "__main__":
    test = GameLogic.calculate_score((1, 2, 3, 4, 5, 6))
    print(test)
    test2 = GameLogic.roll_dice(2)
    print(test2)