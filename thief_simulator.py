import time
import random
from pathlib import Path

eq = "==============="
multiplier = 1
print('============================Welcome!AutoSave is ON==============================')

def rob_bank(cash):
    f = random.randint(1,10)
    if f <= 3:
       k = random.randint(70000,200000)
       cash -= k
       print("==========You were caught during the robbery and fined", k, "cash!=========")
       print("====================Also you were jailed for 15 seconds!========================")
       for i in range(15):
           time.sleep(1)
           print('.',end = '')
       print(' ')
       print("===============You were released from the jail!===============")
    else:
        a = random.randint(10000,100000)
        cash = pcash(cash,a)
        print('============You have successfully robbed a bank and got', a * multiplier, 'cash!===========')
    return cash
    
def work(cash):
    a = random.randint(1000,10000)
    cash = pcash(cash,a)
    print(eq + "You worked really hard and got", a * multiplier, "cash!" + eq)
    return cash
    
kaka = {'Bronze_printer' : 100000,
            'Silver_printer' : 300000,
            'Golden_printer' : 1000000,
            'Platinum_printer': 5000000,
            'Titanium_printer' : 15000000}

def buy(cash,printers, name):
    price = kaka.get(name)
    if price:
        if name in printers:
                print("You can buy only one printer!")
        elif cash >= price:
            cash -= price
            printers.append(name)
            print("=======You just bought", name.replace("_", " "), ", congratulations!==========")
        else:
            print('sorry ur poor')
    else:
        print("This printer doesn't exist")
    return (printers, cash)

kaka_sec = {'Bronze_printer' : 500,
            'Silver_printer' : 1500,
            'Golden_printer' : 5000,
            'Platinum_printer': 25000,
            'Titanium_printer' : 150000}

def game_start():
    global multiplier
    multi_file = Path("multiplier.txt")
    if multi_file.is_file():
        f = open("multiplier.txt", "r+")
        uir = f.readline()
        if uir:
            multiplier = int(uir)
    timer = time.time()
    cash = 0
    printers = []
    called_work = time.time() - 100
    cash_file = Path("cash_balance.txt")
    if cash_file.is_file():
        f = open("cash_balance.txt", "r+")
        ui = f.readline()
        if ui:
            cash = int(ui)
            printers = (f.readline())[1:-1].replace(" ","").replace("'","").split(",")
            if printers == ['']:
                printers = []
            print("Your data has been loaded with", cash, "cash and", printers,"!")
    cmds=['rob bank', 'balance','work','buy','inventory',
          'cmds','casino','rebith','===================','clear data','close game']
    while 1 == 1:
        b = input('=============What do you want to do?(Type cmds for list of commands)============ ')
        b = b.lower()
        diffrence = int(time.time() - timer)
        save(cash,printers)
        for i in printers:
            o = diffrence*kaka_sec[i]
            cash = pcash(cash,o)
        timer = time.time()
        if b == "rob bank":
            cash = rob_bank(cash)
        elif b == "balance":
            bal(cash)
        elif b == "admin":
            cash = admin(cash)
        elif b == "save":
            save(cash,printers)
        elif b == "work":
            time_now = time.time()
            if (time_now - called_work) >= 15:
                cash = work(cash)
                called_work = time_now
            else:
                print('You can work in', int(15 - (time_now - called_work)),"seconds!")
        elif b == "buy":
            #kaka is printers {}
            for u in kaka:
                s = ""
                s+= str(u.replace('_',' '))+ ' - '+ str(kaka[u])
                print(s.center(80))
            kor = input("What do you want to buy?")
            kor = kor.lower().capitalize()
            printers, cash = buy(cash,printers, kor.replace(" ", "_"))
        elif b == "inventory":
            inventory(printers)
        elif b == 'cmds':
            cmds1(cmds)
        elif b == 'clear data':
            clear_data()
            cash = 0
            printers = []
            multiplier = 0
        elif b == 'casino':
            cash = casino(cash)
        elif b == 'rebith':
            cash,printers = rebith(cash,printers)
        elif b == 'close game':
            print('You just closed the game. Bye!')
            return
        else:
            print('This command doesnt exist!')
            cmds1(cmds)
            
def bal(cash):
    print('====================Currently you have', cash, 'cash!======================')

def admin(cash):
    cash += 20000000
    print("+20000000")
    return cash

def save(cash,printers):
    f= open("cash_balance.txt","w+")
    f.write(str(cash)+'\n')
    f.write(str(printers))
    f= open("multiplier.txt","w+")
    f.write(str(multiplier)+'\n')
    f.close()

def inventory(printers):
    print('Currently you have:')
    for i in printers:
        print(i)

def cmds1(cmds):
    print('List of commands:')
    for i in cmds:
        print(i.center(80))

def clear_data():
    g = input('Are you sure you want to clear all of your data? It will remove your cash, inventory and multipliers!(yes or no)')
    g = g.lower()
    if g == 'yes':
        f = open('cash_balance.txt','w+')
        f.write('')
        f.close()
        k = open('multiplier.txt','w+')
        k.write('')
        k.close
    else:
        print('they why u typed this command then?')

def casino(cash):
    b = int(input('What is your bet? '))
    if b > cash:
        print('sorry ur poor')
    else:
        f = random.randint(1,2)
        if f == 1:
            cash = pcash(cash,b)
            print('Congratulations, you just won', b * 2 * multiplier, 'cash!')
        else:
            cash -= b
            print('oh no u lost')
    return cash

def pcash(cash, amount):
    cash += multiplier*amount
    return cash

def rebith(cash,printers):
    global multiplier
    b = input("Are you sure that you want to do rebith? You are gonna lose everything, but you will get 2x multiplier.The price is 20 million.(yes or no)")
    b = b.lower()
    if b == 'yes':
        if cash >= 20000000:
              clear_data()
              multiplier += 1
              cash = 0
              printers = []
              f= open("multiplier.txt","w+")
              f.write(str(multiplier)+'\n')
              f.close()
              print("Congratulations you just made rebith! Current multiplier is x"+str(multiplier)+'!')
        else:
            print('sorry ur poor')
    else:
        print('but it gives u 2x multiplier!1!!111!!!1!')
    return (cash,printers)
game_start()
