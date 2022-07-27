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

        # print(f"Roll: {roll}")

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

    def play_dice(self):
        print("Welcome to Ten Thousand")
        while True:
            score_points = 0
            print("(y)es to play or (n)o to decline")
            choice = input("> ")
            round_num = 1
            if choice == "n":
                print("OK. Maybe another time")
                break
            elif choice == "y":
                while True:
                    print(f"Starting round {round_num}")
                    num_di = 6
                    roll_values = []
                    roll = GameLogic.roll_dice(num_di)
                    roll_length = len(roll)
                    print(f"Rolling {roll_length} dice...")
                    for value in roll:
                        roll_values.append(str(value))

                    formatted_roll = " ".join(roll_values)
                    print(f"*** {formatted_roll} ***")

                    print("Enter dice to keep, or (q)uit:")
                    choice = input("> ")

                    if choice == "q":
                        print(f"Thanks for playing. You earned {score_points} points")
                        break
                    else:
                        points_potential = [int(d) for d in str(choice)]
                        # points_potential.append(int(choice))
                        for point in points_potential:
                            num_di -= 1
                        points = GameLogic.calculate_score(tuple(points_potential))
                        print(f"You have {points} unbanked points and {num_di} dice remaining")
                        while True:

                            print("(r)oll again, (b)ank your points or (q)uit:")
                            choice = input("> ")
                            if choice == "b":
                                score_points += points
                                print(f"You banked {points} in round {round_num}")
                                print(f"Total score is {score_points} points")
                                round_num += 1
                                break
                            elif choice == "q":
                                break
                            break

                break


if __name__ == "__main__":

    test2 = GameLogic.roll_dice(6)

    test3 = GameLogic.play_dice(test2)