from random import randint
from collections import Counter


class GameLogic:
    def __init__(self):
        self.head = None

    @staticmethod
    def calculate_score(dice_roll):
        # dice_roll is a tuple
        score = 0
        roll = Counter(dice_roll).most_common()

        if len(dice_roll) == 0:
            return score

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

    @staticmethod
    def validate_keepers(roll, keepers):
        roll_count = Counter(sorted(roll)).most_common()
        keepers_count = Counter(sorted(keepers)).most_common()

        r_qty = []
        k_qty = []
        for num in roll_count:
            r_qty.append(num[1])
        for bum in keepers_count:
            k_qty.append(bum[1])

        if set(sorted(keepers)).issubset(sorted(roll)) and GameLogic.confirm_quantity(roll_count, keepers_count):
            return True
        else:
            return False

    @staticmethod
    def confirm_quantity(roll_count, keepers_count):
        truth = 0

        for num in keepers_count:
            for bum in roll_count:
                if num[0] == bum[0] and num[1] <= bum[1]:
                    truth += 1

        if truth == len(keepers_count):
            return True
        else:
            return False

    @staticmethod
    def get_scorers(tup):
        scorers = ()
        staging_losers = []

        index = 0
        for num in tup:
            index += 1

        # empty case
        if tup == ():
            return scorers

        # Check first value from input
        if index >= 1:
            one = tup[0],
            if GameLogic.calculate_score(one) > 0:
                scorers += one
            else:
                staging_losers.append(tup[0])

        # Check second value from input
        if index >= 2:
            two = tup[1],
            if GameLogic.calculate_score(two) > 0:
                scorers += two
            else:
                staging_losers.append(tup[1])
        else:
            return scorers

        # Check third value from input
        if index >= 3:
            three = tup[2],
            if GameLogic.calculate_score(three) > 0:
                scorers += three
            else:
                staging_losers.append(tup[2])

        # Check fourth value from input
        if index >= 4:
            four = tup[3],
            if GameLogic.calculate_score(four) > 0:
                scorers += four
            else:
                staging_losers.append(tup[3])

        # Check fifth value from input
        if index >= 5:
            five = tup[4],
            if GameLogic.calculate_score(five) > 0:
                scorers += five
            else:
                staging_losers.append(tup[4])

        # Check six value from input
        if index >= 6:
            six = tup[5],
            if GameLogic.calculate_score(six) > 0:
                scorers += six
            else:
                staging_losers.append(tup[5])

        # This will add number sets other than 1 and 5
        numbers = Counter(staging_losers).most_common()
        x = 0
        for num in numbers:
            if num[1] >= 3:
                for loser in staging_losers:
                    if num[0] == loser:
                        scorers += loser,
            x += 1

        print(tuple(sorted(staging_losers)))
        return tuple(sorted(scorers))

    @staticmethod
    def zilch(roll):
        if GameLogic.calculate_score(roll) == 0:
            print("""
**********************************
**     Zilch!!! Round Over      **
**********************************
            """)
            return False

    @staticmethod
    def validate_hot_dice(keepers, num_di):
        hot_dice = GameLogic.get_scorers(keepers)
        if len(hot_dice) == 6:
            num_di = 6
            return num_di
        else:
            return num_di

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
                    # GameLogic.zilch(roll)
                    print("Enter dice to keep, or (q)uit:")
                    choice = input("> ")

                    if choice == "q":
                        print(f"Thanks for playing. You earned {score_points} points")
                        break

                    else:
                        keepers = [int(d) for d in str(choice)]

                        test = GameLogic.validate_keepers(tuple(roll), tuple(keepers))

                        if test == True:
                            pass

                        if test == False:
                            while test == False:
                                print("Cheater!!! Or possibly made a typo...")
                                print(f"*** {formatted_roll} ***")
                                print("Enter dice to keep, or (q)uit:")
                                # TODO: Add quit option in the while loop
                                choice = input("> ")
                                if test == True:
                                    break
                                break
                        points_potential = [int(d) for d in str(choice)]

                        for point in points_potential:
                            num_di -= 1
                        num_di = GameLogic.validate_hot_dice(tuple(points_potential), num_di)
                        points = GameLogic.calculate_score(tuple(points_potential))
                        print(f"You have {points} unbanked points and {num_di} dice remaining\n")
                        while True:
                            zilcher = 0
                            print("(r)oll again, (b)ank your points or (q)uit:")
                            choice = input("> ")
                            if choice == "q":
                                break

                            if choice == "b":
                                score_points += points
                                print(f"You banked {points} in round {round_num}")
                                print(f"Total score is {score_points} points\n")
                                round_num += 1
                                break
                            elif choice == "r":

                                roll_values = []
                                roll = GameLogic.roll_dice(num_di)
                                roll_length = len(roll)
                                print(f"Rolling {roll_length} dice...")
                                for value in roll:
                                    roll_values.append(str(value))
                                formatted_roll = " ".join(roll_values)
                                print(f"*** {formatted_roll} ***")

                                if GameLogic.zilch(roll) == False:
                                    zilcher += 1
                                    break

                                print("Enter dice to keep, or (q)uit:")
                                choice = input("> ")
                                if choice == "q":
                                    break
                                points_potential = [int(d) for d in str(choice)]

                                for point in points_potential:
                                    num_di -= 1
                                r_points = GameLogic.calculate_score(tuple(points_potential))
                                points += r_points
                                print(f"You have {r_points} unbanked points and {num_di} dice remaining\n")
                                continue

                            break
                        if zilcher == 1:
                            print(f"You banked 0 points in round {round_num}")
                            round_num += 1
                break


if __name__ == "__main__":

    # test2 = GameLogic.roll_dice(6)
    test2 = (1,1,2,2,3,3)
    test3 = GameLogic.play_dice(test2)

    # test4 = GameLogic.get_scorers((6,3,6,6,1,5))
    # print(test4)
    # roll = (6,3,6,6,1,5)
    # num = 6661
    # points = [int(d) for d in str(66)]
    #
    #
    #
    # test6 = set(points).issubset(roll)
    # print(test6)
    # test5 = GameLogic.validate_keepers(roll, tuple(points))
    # print(test5)
