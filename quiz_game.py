from curses import killchar


print("Welcome to my computer quiz!")


playing = input("Do you want to play? ")



if playing.lower() != "yes":
    quit()

print ("Okay! Let's play :)")
score = 0

answer = input( "What does IDS stand for? ")
if answer.lower() == "intrusion detection systems":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input( "What does OSINT stand for? ")
if answer.lower() == "open source intelligence":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input( "What does SIEM stand for? ")
if answer.lower() == "security information and event management":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input( "What does IAM stand for? ")
if answer.lower() == "identity and access management":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")
