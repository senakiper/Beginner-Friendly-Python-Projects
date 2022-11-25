print("Welcome to my QUIZ!")

playing = input("Do you want to play? ")

if playing.lower() != "yes" : 
    quit()

print("Alright! Let's play:)" )
score = 0

answer = input("What does SQL stands for? ")
if answer.lower() == "structured query language":
    print("correct!")
    score += 1 
else:
    print("ıncorrect!")

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("correct!")
    score += 1 
else:
    print("ıncorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("correct!")
    score += 1 
else:
    print("ıncorrect!")

answer = input("What does RAM stand for? ").lower
if answer == "random access memory":
    print("correct!")
    score += 1 
else:
    print("ıncorrect!")

print("You got " + str(score) + " question correct") 
print("You got " + str((score/4) * 100) + "%. ")