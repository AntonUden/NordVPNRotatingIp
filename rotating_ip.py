from nordvpn_switcher import initialize_VPN,rotate_VPN
import time

minutest_between_switch = 5

vpn = initialize_VPN(area_input = ["complete rotation"])
print("Somehow we managed to initialize the VPN without burning down the server room")

while(True):
	print("Changing VPN server...")
	rotate_VPN(instructions=vpn, google_check=1)
	next_change = 60 * minutest_between_switch
	print("Done. Next change in " + str(next_change) + " seconds")
	time.sleep(next_change)
