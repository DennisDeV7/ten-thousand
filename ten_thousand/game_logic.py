from random import randint
from collections import Counter


class GameLogic:
    def __init__(self):
        self.head = None

    @staticmethod
    def calculate_score(dice_roll):
        score = 0
        roll = Counter(dice_roll).most_common()

        if len(dice_roll) == 0:
            return score

        print(f"Roll: {roll}")

        # straight
        if len(roll) == 6:
            return 1500

        # 3 pairs
        if len(roll) > 2:
            if roll[0][1] == 2 and roll[1][1] == 2 and roll[2][1] == 2:
                score += 1500
                return score

        # 2 sets of 3
        if len(roll) == 2:
            if roll[0][1] == 3 and roll[1][1] == 3:
                score += 1200
                return score

        for num in roll:
            # Score cases for 1
            if num[0] == 1:
                if num[1] == 1:
                    score += 100
                if num[1] == 2:
                    score += 200
                if num[1] == 3:
                    score += 1000
                if num[1] == 4:
                    score += 2000
                if num[1] == 5:
                    score += 3000
                if num[1] == 6:
                    score += 4000

            # Score cases for 2
            if num[0] == 2:
                if num[1] < 3:
                    score += 0
                if num[1] == 3:
                    score += 200
                if num[1] == 4:
                    score += 400
                if num[1] == 5:
                    score += 600
                if num[1] == 6:
                    score += 800

            # Score cases for 3
            if num[0] == 3:
                if num[1] < 3:
                    score += 0
                if num[1] == 3:
                    score += 300
                if num[1] == 4:
                    score += 600
                if num[1] == 5:
                    score += 900
                if num[1] == 6:
                    score += 1200

            # Score cases for 4
            if num[0] == 4:
                if num[1] < 3:
                    score += 0
                if num[1] == 3:
                    score += 400
                if num[1] == 4:
                    score += 800
                if num[1] == 5:
                    score += 1200
                if num[1] == 6:
                    score += 1600

            # Score cases for 5
            if num[0] == 5:
                if num[1] == 1:
                    score += 50
                if num[1] == 2:
                    score += 100
                if num[1] == 3:
                    score += 500
                if num[1] == 4:
                    score += 1000
                if num[1] == 5:
                    score += 1500
                if num[1] == 6:
                    score += 2000

            # Score cases for 6
            if num[0] == 6:
                if num[1] < 3:
                    score += 0
                if num[1] == 3:
                    score += 600
                if num[1] == 4:
                    score += 1200
                if num[1] == 5:
                    score += 1800
                if num[1] == 6:
                    score += 2400

        return score

    @staticmethod
    def roll_dice(num_dice):
        results = []
        for num in range(num_dice):
            roll = randint(1, 6)
            results.append(roll)
        return tuple(results)


if __name__ == "__main__":

    test2 = GameLogic.roll_dice(6)
    print(test2)

    test = GameLogic.calculate_score(test2)
    print(test)