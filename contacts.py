#!/usr/bin/env/Pyton3
"""
contacts.py
Contacts Manager Program
Mini-Project - study for storing data on external file / no DB is required
Tutorial Richard White
Code Study Amir Bekhit
"""


def main():
    print("contacts Manager")
    # Initializing friends list and invoking stored data
    try:
        friendsList = []
        infile = open("contacts.txt", "r")
        line = infile.readline()
        while line:
            friendsList.append(line.rstrip("\n").split(","))
            line = infile.readline()
        infile.close()
    except FileNotFoundError:
        print("**********************")
        print("contacts.txt not found")
        print("Starting new address book")
        print("**********************")
        friendsList = []

    choice = 0

    while choice != 4:
        print("1) Add a friend")
        print("2) Lookup a friend")
        print("3) Display friends")
        print("4) Quit")
        choice = int(input())

        if choice == 1:
            print("Adding a friend")
            name = input("Enter name >>>")
            phone = input("Enter phone >>>")
            email = input("Enter email >>>")
            friendsList.append([name, phone, email])

        elif choice == 2:
            print("Look up a friend")
            keyword = input("Enter search a term >>>")
            for friend in friendsList:
                if keyword in friend:
                    print(friend)

        elif choice == 3:
            print("displaying all friends")
            for i in range(len(friendsList)):
                print(friendsList[i])

        elif choice == 4:
            print("Quitting program")
        else:
            print("Invalid Response")
    print("Saving Data ...")
    print("program terminated")


# Saving data to a text file
    outfile = open("contacts.txt", "w")
    for friend in friendsList:
        outfile.write(",".join(friend) + "\n")
    outfile.close()


main()


# Persistence - save data
# -------------------------
# * Database - SQLITE - MYSQL
# * "flat-file" database = text file
# CSV file ="comma-seperated values"
# python solution : pickle, shelve
