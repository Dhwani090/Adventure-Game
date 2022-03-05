#Functions
def followSound():
    print("You keep moving closer to the sound.")
    print("The sound suddenly stops.")
    print("You try to call on your phone but there is no signal.")
def lost():
    print("You start walking back to the starting point.")
    print("You realize you are LOST.")
    print("The sound is behind you and is getting louder. You panic!")
    action = input("Do you want to run(r) or make a call(c)?")
    while action == "c":
        print('The call does not go through.')
        action = input("Do you want to run(r) or make a call(c)?")
    print("You are running fast. The sound gets really loud.")
def Direction():
    direction = input("Which direction do you want to go North(n), West(w), South(s), East(e)")
    if direction == "n":
        print("You have reached a cabin")
        print("The cabin is abandoned and looks dangerous")
        answer2 = input("Do you want to search the cabin(y/n)")
        if answer2 == "y":
            print("There is an underground bunker inside the cabin with blood everywhere")
            answer3 = input("Do you want to search the underground bunker(y/n)")
            if answer3 == "y":
                print("You have found a secret base with no one inside!")
                print("You use the materials inside the bunker to find your way home")
                print("You report the bunker to the authorities and get 10,000 dollars as your reward!!!")
            elif answer3 == "n":
                print("You escaped without any scratches")
                if item == "m":
                    print("You used your map to find a way")
                    print("You have won!!!Yay!")
                else:
                    print("You didn't have a map to find your way")
                    print("YOU LOSE")
        elif answer2 == "n":
            print("You avoided the cabin safely")
            if item == "m":
                    print("You used your map to find a way")
                    print("You have won!!!Yay!")
            else:
                print("You didn't have a map to find your way")
                print("YOU LOSE")
    elif direction == "w":
        print("You have reached a fork in the trail")
        print("One way has leads to a waterfall and the other leads to the deep jungle")
        answer4 = input("Which way do you want to go?(w/j)")
        if answer4 == "w":
            print("You find a old man next to the waterfall")
            answer5 = input("Do you want to talk to him(y/n)")
            if answer5 == "y":
                print("The old man shows you a way home")
                print("You have won!!!Yay!")
            if answer5 == "n":
                print("You pass by the old man and turn around")
                print("The old man pulls a gun and shoots you")
                print("YOU LOSE")
        if answer4 == "j":
            print("You make your way pass the dense leaves of the jungle")
            print("You hear growling noises to your right and there's a ravine to your left")
            print("You keep heading forward and find the lost city of the jungle")
            print("There is also a native american tribe living here")
            answer6 = input("Do you want to go inside the lost city(y/n)")
            while answer6 == "n":
              print("The tribe is forcing you inside")
              answer6 = input("Do you want to go inside the lost city(y/n)")
            print("You head inside and hear chants")
            print("The door closes behind you and you find tons of treasure!")
            print("You can't leave from the lost city so you make home here as a rich man")
            print("You have won!!!Yay!")
    elif direction == "s":
        print("You have reached a broken bridge")
        if item == "r":
            print("You have successfully fixed the bridge with your rope")
            print("You have won!!!Yay!")
        if item == "s":
            print("You have successfully fixed the bridge with your sticks")
            print("You have won!!!Yay!")
        else:
            print("You didn't have a rope or stick to fix the bridge")
            print("YOU LOSE")
    elif direction == "e":
        print("You have reached a highway")
        if item == "f":
            print("You signaled for help")
            print("Luckily a helicopter saw your flashlight and saved your life")
            print("You have won!!!Yay!")
        elif item == "r":
            print("You look around and find a path")
            print("You continue on the path")
            print("You have found a broken bridge")
            print("You used your rope to fix the bridge")
            print("You have won!!!Yay!")
        elif item == "s":
            print("You look around and find a path")
            print("You continue on the path")
            
            print("You have found a broken bridge")
            print("You used your sticks to fix the bridge")
            print("You have won!!!Yay!")
        else:
            print("You didn't have a rope or stick to fix the bridge")
            print("YOU LOSE")
print("Welcome to the Grand Canyon Mountain Adventure game.")
print("You are visiting the Grand Canyon")
print("You go on a hike alone on the Hermit trail. This trail has washouts and rockslides and requires some navigating skills to find the routes.")
item = input("Do you want to take map(m), flashlight(f), chocolate(c), rope(r), or sticks(s)")
print("You hear a humming sound")
Answer1 = input("Do you want to follow the sound(y/n)?")
if Answer1 == "y":
    followSound()
    lost()
elif Answer1 == "n":
    lost()
Direction()
