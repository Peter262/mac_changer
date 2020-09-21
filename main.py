#!/usr/bin/python3

from MAC_changer import mac_changer
if __name__== "__main__":
    mc = mac_changer ()
    mac = mc.get_mac("eth0")
    print(mac)
    curr_mac = mc.change_mac("eth0","00:50:56:c0:21:08")
    print(curr_mac)
    