def rock_paper_scissor(sys,user):
    if sys==user:
        print("Its a tie!")
    elif sys=='rock' and user=='scissor':
        print("Computer Won")
    elif sys=='paper' and user=='rock':
        print("Computer Won")
    elif sys=='scissor' and user=='paper':
        print("Computer Won")
    else:
        print("USER Won")
    return

import random
while True:
    choices=['rock','paper','scissor']
    comp=random.choice(choices)
    ur_input=input("Choose rock or paper or scissor:")
    user=ur_input.lower()
    if user not in choices:
        print ("Invalid option choose again")
        continue
    print("Computer's choice:",comp)
    print("Your choice:",user)
    rock_paper_scissor(comp,user)
    i=int(input("To play again:0 or To exit:1\n"))
    if i==1:
        break