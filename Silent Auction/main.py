from replit import clear
from art import logo

print(logo)

bid_list = {}
proceed_further = True

def find_highest_bidder(bid_record):
  highest_bid = 0
  winner = ""
  for bid in bid_record:
    if bid_record[bid] > highest_bid:
      highest_bid = bid_record[bid]
      winner = bid
  
  print(f"Winner is {winner} with a bid of  ₹{highest_bid}")


while(proceed_further):
  name = input("What's your name ? ").lower()
  price = int(input("What's your bid ? ₹"))

  bid_list[name] = price

  choice = input("Any other bidder is there, in the house ? type yes/no : ").lower()
  clear()

  if choice == 'no':
    proceed_further = False
#     print(bid_list)
    find_highest_bidder(bid_list)


