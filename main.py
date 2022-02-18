# Shopping List
import os, time
from datetime import date

shoppingList = []


def main():
    print("SHOPPING LIST")
    print("-------------")
    print(
        "a) View List\nb) Add to List\nc) Delete an Item\nd) Delete List\ne) Export List\nf) Exit program\n"
    )

    userInput = input("Select a choice: ")

    select(userInput)


def select(self):
    if self == "A" or self == "a":
        viewList()
        enterDialogue()
    elif self == "B" or self == "b":
        addToList()
    elif self == "C" or self == "c":
        deleteItem()
    elif self == "D" or self == "d":
        deleteList()
    elif self == "E" or self == "e":
        export()
    elif self == "F" or self == "f":
        exit()
    else:
        print("Error, please try again...")
        enterDialogue()


def viewList():
    if len(shoppingList) == 0:
        print("Error: Empty list")
        enterDialogue()
    else:
        os.system("clear")
        print("\nCurrent Shopping List")
        print("------------")

        for items in shoppingList:
            print(items)


def addToList():
    os.system("clear")
    amnt = int(input("How many items would you like to add? "))
    i = 0

    print()

    for i in range(amnt):
        item = input("Enter item %d: " % (i + 1))
        shoppingList.append(item)

    print("\n%d item(s) have been added!" % amnt)
    enterDialogue()


def deleteItem():
    viewList()
    print()
    item = input("Which item do you want to delete? ")

    shoppingList.remove("%s" % item)

    print("The item (%s) has been removed..." % item)
    enterDialogue()


def deleteList():
    os.system("clear")
    shoppingList.clear()

    print("The shopping list has been cleared...")
    enterDialogue()


def export():
    if len(shoppingList) == 0:
        print("Error: Empty list")
        enterDialogue()
    else:
        os.system("clear")
        f = open("shopping-list.txt", "w")

        today = date.today()
        currDate = today.strftime("%m/%d/%y")

        f.write("SHOPPING LIST (%s)\n" % currDate)
        f.write("-------------\n")

        for item in shoppingList:
            f.write(item + "\n")

        f.close()

        print("The file has been exported!")
        enterDialogue()


def exit():
    os.system("clear")
    print("Exiting program...")
    time.sleep(3)
    os.system("clear")
    quit()


def enterDialogue():
    input("\nPress Enter to continue...")
    os.system("clear")
    main()


main()
