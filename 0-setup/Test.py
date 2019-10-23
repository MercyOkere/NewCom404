print("Where is Forky?")
location = input()

if location == "With Bonnie":
    print("Phew Bonnie will be happy.")
elif location == "Running away":
    print("Oh no! Bonnie will be upset!")
else:
    print("Ah! I better look for him.") 




print("How many miles must I travel before i reach the secret base?")
miles = int(input())

print("I will count the miles...")

for count in range(miles,0,-1):
    print("I have" +str(miles) + "miles to go before I reach the base.")
    miles -=1

print("i have arrived at the secret headquarters of the MIB!")
print("It is time to sneak in.")


def item_from_suitcase(item):
    if item == "toothbrush":
        print("A toothbrush. Well got to have a clean teeth!")
    elif item == "spidey suit":
        print("Spidy suit! I wont be needing this. I am on holiday.")
     
