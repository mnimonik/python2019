import getch
import time
import os
from pathlib import Path
import random

position = 0
q = []

food = '¡™£¢∞§¶åßƒ©∆¬æΩ≈ç√∫µ≤≥÷'
def e():
    global q
    for i in range(size):
        g = random.randint(0,size*size - 1)
        q.append(g)
def grid(n):
    global q
    kaka()
    for i in range(n):
        print(' _'*n)
        for x in range(n):
            u = i * size + x
            if position == u :
                print('|•', end = '')
                if position in q:
                    q.remove(position)
            elif u in q:
                print('|*', end = '')
            else:
                print('| ', end = '')
        print('| ')
    print(' _'*n)

size = 5
def gog():
    f = open('kaka.txt','w+')
    f.write(str(position))
    f.close()

def kaka():
    global position
    kaka = Path("kaka.txt")
    if kaka.is_file():
        f = open("kaka.txt", "r+")
        kika = f.readline()
        if kika:
            position = int(kika)
def r():
    global position
    position += 1
    if position % size == 0:
        position -= size
    gog()
    
def l():
    global position
    if position % size == 0:
        position += size
    position -= 1
    gog()

def u():
    global position
    position -= size
    if position < 0:
        position += size * size - size
    gog()
def d():
    global position
    position += size
    if position >= size * size:
        position -= size * size - size
    gog()
def game_start(n):
    e()
    global position
    global size
    size = n
    newpid = os.fork() 
    if newpid == 0:
        while True:
            char = getch.getch()
            if char == 'w':
                u()
            if char == 'a':
                l()
            if char == 's':
                d()
            if char == 'd':
                r()
    else:
        while q:
            grid(size)
            a = time.time()
            time.sleep(2)
            
game_start(5) 
