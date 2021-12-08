class Vector():
    initial_point: []
    terminal_point: []
    standard_vector: []
    magnitude: float

    def __init__(self, ip, tp):
        self.initial_point = ip
        self.terminal_point = tp
        self.standard_vector = self.find_standard_vector()
        self.magnitude = self.find_magnitude()

    def find_standard_vector(self):
        if (len(self.initial_point) != len(self.terminal_point)):
            print("initial and terminal points must be the same")
            return

        standard_vector = [None] * len(self.initial_point)
        for i in range(len(self.initial_point)):
            standard_vector[i] = self.terminal_point[i] - self.initial_point[i]

        return standard_vector

    def find_magnitude(self):
        if (self.standard_vector != None):
            sum = 0
            for i in range(len(self.standard_vector)):
                sum += self.standard_vector[i] * self.standard_vector[i]
            return sum ** (1/2)

    def __str__(self):
        return str(self.initial_point) + " to " + str(self.terminal_point)

ip = [0, 0, 0, 0, 0]
tp = [5, -12, 0, 7, 9]
vector = Vector(ip, tp)
print("vector: " + str(vector))
print("standard vector: " + str(vector.standard_vector))
print("magnitude: " + str(vector.magnitude))
