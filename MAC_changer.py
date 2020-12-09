
# In order to run command we import the sub-process module.
import subprocess

# In order to search this we have to import re (Regular Expression) module in the program.
import re 

# Creating a mac changer class
class mac_changer:

# First function will be the constructor and it will take self.Self is argument
	def __init__(self):
# Initialize a variable with no mac address, to use them in further program.
		self.mac = "" 
# Second function to get us mac address of the system.
	def get_mac(self,iface):       

# To run the first ifconfig command to get the current mac address, you can give is as a list. 
# This line will give us the ifconfig result ( not a string ) & save it in variable.
		output = subprocess.run(["ifconfig", iface], shell=False, capture_output=True)
        
# In order to get the string format we can decode the result using utf-8 decoding. 
# If You don't give an argument to it by default takes the utf-8 as a decoding.
        	cmd_result = output.stdout.decode('utf-8')
        
# Getting the MAC address using Regular Expression Pattern
# ✪ Now our next goal is to search the whole previous output string to extract just MAC address. 
# To do that, copy the whole output. And go to https://regex101.com & paste it inside TEST STRING field. And set the FLAVOUR to Python.
#	1. First we want to search ether. So write down ether in the REGULAR EXPRESSION field.
#	2. Then we have to find a space after ether. To find the space we have to use \s after it. Like ether\s
#	3. Then we have to find the hexadecimal value of the MAC address. To do this we separately search all six sections of the mac address.
#		1. MAC address can contain letters & number. So we have to search both at a same time. 
# 		For numbers we have to write \d . 
# 		For letters we have to use a-f but we can use a-z for better result.
# 		2. And we use '[ ]' to put our every numbers search query inside. Like [\da-z]
#		3. We can see there are two digits in every section. So in order to select two digits we use 2 and put it inside { }. like {2} . Now we find the first section of the mac address. 
# 		4. To find the all six section of the mac address we can copy the search query, separate each section by : & paste it five times. like [\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}
# 	4. Now copy the whole ether\s[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2} 
        	pattern = r'ether\s[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}'

# Compiling the pattern
        	regex = re.compile(pattern)
        	ans = regex.search(cmd_result)
        	current_mac = ans.group().split(" ")[1]
        	self.mac = current_mac
        	return current_mac
# Third function to change the MAC address of the system.
	def change_mac (self,iface,new_mac):
        	print("[+] Current MAC Address is ", self.get_mac(iface))
        	output = subprocess.run(["ifconfig",iface,"down"], shell=False, capture_output=True)
        	print(output.stderr.decode('utf-8'))
        	output = subprocess.run(["ifconfig",iface,"hw" , "ether", new_mac], shell=False, capture_output=True)
        	print(output.stderr.decode('utf-8'))
        	output = subprocess.run(["ifconfig" , iface , "up"], shell=False,capture_output=True)
        	print(output.stderr.decode('utf-8'))
        	print("[+] Updated MAC Address is ", self.get_mac(iface))
        	return self.get_mac(iface)
