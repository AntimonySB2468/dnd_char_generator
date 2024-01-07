
import dice

class ball:
    def __init__(self, name: str, size: int):
        self.size = size
        self.name = name
    def __str__(self):
        return self.name


ball_1 = ball("Howard", 10)
ball_2 = ball("Melissa", 4)

ball_dict = {
    ball_1: "He likes cheese",
    ball_2: "She likes rolling"
}

print(ball_dict)