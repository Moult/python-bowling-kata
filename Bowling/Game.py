class Game():

    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        score = 0
        roll = 0

        for frame in range(10):
            if self.__is_strike(roll):
                score += 10 + self.__get_strike_bonus(roll)
                roll += 1
            elif self.__is_spare(roll):
                score += 10 + self.__get_spare_bonus(roll)
                roll += 2
            else:
                score += self.__pins_knocked_down_in_frame(roll)
                roll += 2

        return score

    def __is_spare(self, roll):
        return self.rolls[roll] + self.rolls[roll + 1] == 10

    def __is_strike(self, roll):
        return self.rolls[roll] == 10

    def __get_strike_bonus(self, roll):
        return self.rolls[roll + 1] + self.rolls[roll + 2]

    def __get_spare_bonus(self, roll):
        return self.rolls[roll + 2]

    def __pins_knocked_down_in_frame(self, roll):
        return self.rolls[roll] + self.rolls[roll + 1]
