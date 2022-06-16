# rock scissor paper
import random
choices = ['paper', 'scissors', 'rock']
result = ['you win', 'draw', 'you lose']
user = int(input('choose...\n\t(1) paper\n\t(2) scissor\n\t(3) rock\nchoice: ')) - 1
cpu = random.randint(0, 2)
mod = (cpu - user + 1) % 3
print(f'you chose {choices[user]}, cpu chose {choices[cpu]}, {result[mod]}')
