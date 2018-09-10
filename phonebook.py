#!//usr/bin/env python3

import pickle

def main():
	ntrunning = 0
	phone_book = {}
	# creates empty dictionary to load phonebook into
	file = open('phonebook.dat','r')
	# opens file used between instances to store phonebook
	phone_book = pickle.load(file)
	# loads data into phonebook dictionary
	file.close()
	# closes file
	print("Welcome to phonebook")
	while ntrunning == 0:
		askUser()
if __name__ == '__main__':
	main()	
def askUser():
	userChoice = input("My Phonebook'\n'1. Find a phone number by name.'\n'2. Add an entry.'\n'3. Quit.'\n'Your choice:")
	if userChoice == 1:
		inName = input("Enter a name")
		viewEntry(inName)
		ntrunning = 0
		return 0
	elif userChoice == 2:
		inName = input("Enter a name")
		inNumber = input("Enter a number")
		newEntry(inName.inNumber)
		ntrunning = 0
		return 0
	elif userChoice == 3:
		quitBook()
		ntrunning = 1
		return 1
def newEntry(name, number):
	phone_book({name: number});
	# adds entry for 
def viewEntry(name):
	print("The Phonebook entry at ",name," is: ",phone_book(name))
def quitBook():
	file = open('phonebook.dat','wb')
	pickle.dump(phone_book, file)
	file.close()
	exit()
