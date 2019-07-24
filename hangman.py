import random

f = open("words2.txt", "r")
word_list = []
for x in f:
    word_list.append(x.replace('\n', ''))
f.close()

while True:
   b = input('Do you want to play Hangman? (yes or no)')
   if b == 'no':
       print('you are a kakaha vonuchaya!1!11!11!!!!!')
       break
   user_lost = False
   kakaha = random.randint(0, len(word_list))
   the_word = word_list[kakaha]
   a = len(the_word)
   guess = []
   popi = 6 
   for i in range(a):
           guess.append("_")
   past_guesses = []
   while not user_lost:
       print(" ".join(guess))
       print('Only', str(popi) ,'tries left!')
       c = input('wots ur ges?')

       if c in past_guesses:
           print('You already guessed this letter!')
       elif c in the_word:
           letter_positions = []
           for h in range(a):
               if c == the_word[h]:
                   letter_positions.append(h)
           for l in range(a):
               if l in letter_positions:
                    guess[l] = c
           past_guesses.append(c)
       else:
            popi -= 1
            past_guesses.append(c)
       if popi == 0:
           user_lost = True
   print("You Lost! hahahaha")
   print('The word was', the_word)
   print("")
