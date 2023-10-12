import random

def num():
    return random.randint(1, 50)
def star():
    return random.randint(1, 12)

for i in range(5):
    print(num())

print('------------√-------------')

for t in range(2):
    print(star())
