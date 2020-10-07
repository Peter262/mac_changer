'''In order to run command we import the sub-process module.'''
import subprocess
'''In order to search this we have to import re (Regular Expression) module in the program.'''
import re 

'''creating a mac changer class'''
class mac_changer:
    '''First function will be the constructor and it will take self.Self is argument '''
    def __init__(self):
        self.mac = ""
    
    '''Second function to get us mac address of the system.'''
    def get_mac(self,iface):
        output = subprocess.run(["ifconfig", iface], shell=False, capture_output=True)
        cmd_result = output.stdout.decode('utf-8')
        pattern = r'ether\s[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}'
        regex = re.compile(pattern)
        ans = regex.search(cmd_result)
        current_mac = ans.group().split(" ")[1]
        self.mac = current_mac
        return current_mac
    
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
