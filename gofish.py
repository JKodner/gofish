import random
import sys
deck = []
ud = []
udt = []
cd = []
cdt = []
COUNT = " "
count = 1
card_count = 0
first = ["user", "com"]
choices = ["", "deck", "draw", "exit", "com", "decks"]
def sep(s, n):
	print s * n
NUM = " "
sep(" ", 1)
sep("-*-", 1)
while type(NUM) != int:
	try:
		NUM = int(raw_input("To What Range do You Want Your Numbers on Your Cards to be?"))
		if not NUM >= 9:
			NUM = " "
			print "Range Must be Greater or Equal to 9."
	except ValueError:
		None
COUNT = " "
while type(COUNT) != int:
	try:
		COUNT = int(raw_input("How Many Cards do You Want in Each Deck?"))
		if not COUNT >= 7:
			COUNT = " "
			print "Deck Count Must be Greater or Equal to 7."
	except ValueError:
		None
sep("-*-", 1)
num = range(1, NUM + 1)
sep(" ", 1)
sep("-", 30)
print "Creating the Game Deck..."
sep("-", 30)
for i in range(COUNT*2):
	deck.append(random.choice(num))
for i in range(3):
	random.shuffle(deck)
for i in range(COUNT):
	ud.append(deck.pop())
for i in range(COUNT):
	cd.append(deck.pop())
for i in range(52):
	deck.append(random.choice(num))
def ruc():
	ud.append(deck.pop())
	print "You Have Drawn a %d" % ud[-1]
def rcc():
	cd.append(deck.pop())
	print "The Computer has Drawn a %d." % cd[-1]
ask = " "
def response():
	global ask
	ask = " "
	global count
	while ask.lower() not in choices:
		sep(" ", 1)
		sep("-*-", 1)
		print "Press [Enter] if You Would Like to Continue."
		print "Type [Deck] if You Would Like to See Your Deck & Statistics."
		print "Type [Draw] if You Believe It is Necessary to Draw a Card."
		print "Type [Exit] to Exit the Program if Needed."
		ask = raw_input("")
	sep("-*-", 1)
	sep(" ", 1)
	if ask.lower() == choices[1]:
		sep("-", 30)
		ud.sort()
		print "Your Deck:"
		print ud
		sep("-", 30)
		sep(" ", 1)
		sep("#", 30)
		print "You Have %d cards in Your deck." % len(ud)
		print "You are Currently in Round #%d" % count
		print "The Game Deck Currently has %d Cards." % len(deck)
		sep("#", 30)
		sep(" ", 1)
	elif ask.lower() == choices[2]:
		ruc()
		print "You Have Drawn: %d" % ud[-1]
		sep(" ", 1)
	elif ask.lower() == choices[3]:
		print "Exiting the Program..."
		print sep(" ", 1)
		sys.exit()
	elif ask.lower() == choices[4]:
		sep("-", 30)
		cd.sort()
		print "Computer's Deck:"
		print cd
		sep("-", 30)
		sep(" ", 1)
		sep("#", 20)
		print "The Computer Has %d cards in Their deck." % len(ud)
		print "You are Currently in Round #%d" % count
		print "The Game Deck Currently has %d Cards." % len(deck)
		sep("#", 20)
		sep(" ", 1)
while len(ud) != 0 or len(cd) != 0 or len(deck) != 0:
	response()
	if ask.lower() == choices[0]:
		ask_card = " "
		while ask_card not in ud:
			try:
				ask_card = int(raw_input("What Card Do You Wish to Call?"))
			except ValueError:
				None
		if ask_card in cd:
			print "Foo"
			for i in cd:
				if i == ask_card:
					"You Have Taken a %d From the Computer." % i
					udt.append(i)
					cd.remove(i)
		else:
			rcc()
		com_ask_card = random.choice(num)
		print "The Computer has asked for all of your %d's" % com_ask_card
		if com_ask_card in ud:
			for i in ud:
				if i == ask_card:
					print "The Computer Has Taken a %d From You." % i
					cdt.append(i)
					ud.remove(i)
		else:
			ruc()

	
