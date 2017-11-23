import time
from random import randint

exit = False
count = 0
sum_score = 0
while not exit:
    right = 0
    wrong = 0
    # limit = input('What is your limit?\n')
    limit = 10
    i = 0
    while i < int(limit):
        x = randint(2, 12)
        y = randint(2, 12)
        res = input('What is {} * {}?\n'.format(x, y))
        ans = x * y
        if res == 'quit':
            break
        elif int(res) == ans:
            print('That is correct!')
            right += 1
        else:
            print('Wrong! the correct answer was {}'.format(ans))
            wrong += 1
        time.sleep(.25)
        i += 1
    score = 0.0 if i == 0 else (float(right) / i) * 100
    sum_score += score
    count += 1
    print('you got {} out of {} correct\nyour score is {}%'.format(right, i, str(score)))
    q = input('exit? y/n\n')
    exit = True if q == 'y' else False
average = sum_score / count
print('your overall average: {}'.format(average))
input('press any key to quit')

# with open('avg.txt', 'a') as myfile:
    # myfile.write('{}, '.format(average))
