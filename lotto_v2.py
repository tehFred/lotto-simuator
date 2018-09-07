import random
import pprint
import locale

locale.setlocale(locale.LC_ALL, '')


print_every = 52000

balls = tuple(range(1, 46))
# all available balls

#tickets, ticket_price = 9, 11.85
#tickets, ticket_price = 12, 15.75
tickets, ticket_price = 18, 23.60
#tickets, ticket_price = 24, 31.50
#tickets, ticket_price = 36, 47.25
#tickets, ticket_price = 50, 65.65

#tickets = 100000
#ticket_price = tickets * 1.30

winnings = 0.0
spent = 0
iterations = 0
total_iterations = 0

stop = 0

entry = {}

div1_win = 35000000.00
div2_win = 32521.30
div3_win = 4951.70
div4_win = 387.30
div5_win = 52.00
div6_win = 25.65
div7_win = 15.95

div1_total = 0
div2_total = 0
div3_total = 0
div4_total = 0
div5_total = 0
div6_total = 0
div7_total = 0

loop = True

while loop == True:

	winning_balls = random.sample(balls, 9)
	winning_numbers = winning_balls[:7]
	winning_supps = winning_balls[7:9]
	ticket = [winning_numbers, winning_supps]

	for i in range(tickets):
		combined_ticket = []
		chosen_balls = random.sample(balls, 9)
		numbers = chosen_balls[:7]
		supps = chosen_balls[7:9]
	
		combined_ticket.append(numbers)
		combined_ticket.append(supps)
		# creates a single entry ticket

		entry[i] = combined_ticket
		# adds single entry into multi play
	
	spent += ticket_price

	for i in range(tickets):
		player_entry = entry[i]
		standard_hit = sum(1 for x in player_entry[0] if x in ticket[0])
		supp_hit = sum(1 for x in player_entry[1] if x in ticket[1])
		# determines number of right numbers in each catergory

		if standard_hit == 7:
			winnings += div1_win
			div1_total += 1
			print '\n!\n!\nDIV 1 WIN\n!\n!'
			#time = total_iterations / 52
			#stats = '\nspent: $%s, winnings: $%s, net: $%s' % (
			#												locale.currency(spent, symbol=False, grouping=True),
			#												locale.currency(winnings, symbol=False, grouping=True),
			#												locale.currency(winnings-spent, symbol=False, grouping=True)
			#												)
			#totals = div1_total, div2_total, div3_total, div4_total, div5_total, div6_total, div7_total
			#time = total_iterations / 52
			#print stats
			#print totals
			#print 'Years played: %s' % time
			#jackpot = True

		elif standard_hit == 6 and supp_hit > 1:
			winnings += div2_win
			div2_total += 1
	
		elif standard_hit == 6:
			winnings += div3_win
			div3_total += 1

		elif standard_hit == 5 and supp_hit > 1:
			div4_total += 1
			winnings += div4_win
	
		elif standard_hit == 5:
			div5_total += 1
			winnings += div5_win

		elif standard_hit == 4:
			div6_total += 1
			winnings += div6_win

		elif standard_hit == 3 and supp_hit > 1:
			div7_total += 1
			winnings += div7_win
			
	
	iterations += 1
	total_iterations += 1

	if iterations == print_every:
		stats = '\nspent: $%s, winnings: $%s, net: $%s' % (
														locale.currency(spent, symbol=False, grouping=True),
														locale.currency(winnings, symbol=False, grouping=True),
														locale.currency(winnings-spent, symbol=False, grouping=True)
														)
		totals = div1_total, div2_total, div3_total, div4_total, div5_total, div6_total, div7_total
		time = total_iterations / 52
		print stats
		print totals
		print 'Years played: %s' % time
		iterations = 0
		#loop = False
	



