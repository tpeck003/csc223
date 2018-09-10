#!//usr/bin/env python3

import pickle

def main()
	file = open('phonebook.dat','r')
	phone_book = pickle.load(file)
	file.close()
def newEntry(name, number)
	phone_book({name: number});
def viewEntry(name)
	print("The Phonebook entry at ",name," is: ",phone_book(name))
def quit()
	file = open('phonebook.dat','wb')
		pickle.dump(phone_book, file)
	file.close()
	exit()