import random

def play_one_round(switch):
	# The prize is behind a random door
	prize = random.randint(1,5)
	# We choose door B
	chosen = 2
	# The host opens a random door which is neither the prize nor the door we chose
	while True:
		opened = random.randint(1,5)
		if opened==chosen:
			continue
		elif opened==prize:
			continue
		else:
			break
	# If we decide to switch, we switch to a door which is neither the opened door nor the door we originally chose
	if switch:
		while True:
			chosen2 = random.randint(1,5)
			if chosen2==opened:
				continue
			elif chosen2==chosen:
				continue
			else:
				break
		chosen = chosen2
	# Now we see if we won or not
	# return True if we won, and False otherwise
	return chosen==prize

NUM_ROUNDS = 100000

# Play some rounds without switching
won = 0
for i in range(NUM_ROUNDS):
	if play_one_round(False):
		won += 1
print('Without switching, we won %d/%d'%(won,NUM_ROUNDS))
print('Expected: 1/5 = %d/%d'%(NUM_ROUNDS/5,NUM_ROUNDS))
print()

# Play some rounds with switching
won = 0
for i in range(100000):
	if play_one_round(True):
		won += 1
print('With switching, we won %d/%d'%(won,NUM_ROUNDS))
print('Expected: 4/15 = %d/%d'%(4*NUM_ROUNDS/15,NUM_ROUNDS))
