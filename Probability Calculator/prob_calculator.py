import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for times in range(value):
                self.contents.append(key)

    def draw(self, number_of_balls):
        drawn_balls = []

        if number_of_balls > len(self.contents):
            return self.contents

        for number in range(number_of_balls):
            chosen = random.choice(self.contents)
            self.contents.remove(chosen)
            drawn_balls.append(chosen)

        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    count = 0
    expected_list = []

    for expected, value in expected_balls.items():
        for times in range(value):
            expected_list.append(expected)

    expected_set = set(expected_list)
    is_in_list = False

    for experiment_no in range(num_experiments):

        copied_hat = copy.deepcopy(hat)
        drawn = copied_hat.draw(num_balls_drawn)
        
        for expected in expected_set:
            if drawn.count(expected) >= expected_list.count(expected):
                is_in_list = True
            else:
                is_in_list = False
                break

        if is_in_list == True:
            count += 1

    return count/num_experiments

    pass
