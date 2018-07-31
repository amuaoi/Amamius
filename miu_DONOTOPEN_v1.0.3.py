import time
import random
import sys


class Miu(object):
    def __init__(self):
        self.lastUpdateTime = time.time()
        self.hunger = 150
        self.status = 'Alive'
    
    def update(self):
        self.hungerUpdate()
        self.statusCheck()

    def hungerUpdate(self):
        self.hunger -= (time.time() - self.lastUpdateTime) * 2
        self.lastUpdateTime = time.time()

    def statusCheck(self):
        if self.hunger <= 0:
            self.status = 'Dead'
            print('Kawaii Miumiu died of hunger!!!')


    def feed(self,food):
        if self.status == 'Alive':
            if food == 'pudding':
                self.hunger += 20
            elif food == 'ramen':
                self.hunger += 40
            elif food == 'Wei':
                self.hunger = 150
                print(self.hunger)
            else:
                self.hunger += random.randint(-50,50)
            print('AwuAwuAwu')
            self.update()
        else:
            print('Miumiu dead!')
            print('Give me 100 Ero-wei pictures to make revival potion')

    def checkHunger(self):
        if self.status == 'Alive':
            print('Miumiu Hunger: %d' % self.hunger)
        else:
            print('Miumiu dead!')
            print('Give me 100 Ero-wei pictures to make revival potion')
        self.update()

    def play(self):
        if self.status == 'Alive': 
            reactions = ['Very happy!','Miuao','Feeling sad','SUPER HUNGRY']
            print('Miumiu '+random.choice(reactions)+' Miuaooooo')
            self.hunger -= 10
            self.update()
        else:
            print('Miumiu dead!')
            print('Give me 100 Ero-wei pictures to make revival potion')


def askForWeiZhao():
    


def main():
    miu = Miu()
    print('''   Miumiu caught!!!!
    You can now:
    1. Type 'Feed Miu with xxx' to feed Miumiu
        (xxx can be pudding, ramen, Wei or any random food)
    2. Type 'Check hunger' to get Miumiu's hunger status
    3. Type 'Play' to play with Miumiu!
    4. Type 'Byebye' to ...
    ''')
    number = random.randint(1,100000000)
    print('You have just caught Miumiu No.%d...' % number)
    try:
        with open('Miumiu_version.txt','r') as f:
            oldNumber = int(f.read())
        print('BUT YOU HAVE TO REMEMBER THAT')
        print('!!!!!YOU KILLED MIUMIU NO.%d JUST NOW!!!!' % oldNumber)
    except:
        pass
    with open('Miumiu_version.txt','w') as f:
        f.write(str(number))
    while True:
        command = sys.stdin.readline().strip()
        if command[:14] == 'Feed Miu with ':
            food = command.split(' ')[-1]
            print(food)
            miu.feed(food)
        elif command == 'Check hunger':
            miu.checkHunger()
        elif command == 'Play':
            miu.play()
        elif command == 'Byebye':
            break
        else:
            print('Error! Command not found')
    print('AOUUUUUUU')

main()









