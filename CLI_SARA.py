2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 08:13:29 2020

@author: ckbbe
"""
import socket
import tqdm
import os
SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 

options = {1 : "Submit a document for sentiment analysis",
           2 : "Pull risk report for entity (company, brand, etc.)",
           3 : "Quit"}


def main():
    print("""\t\t\t\tWelcome to SARA""")
    print("Sentiment and Risk Analyzer for all things business\n")
    print("Choose from the options below:")
    choice = displayOptions(options)         
    toServer(choice)

def inputOption(prompt):
    while True:
        try:
            num = int(input(prompt))
            break
        except ValueError:
            pass       
    return num

def displayOptions(options):
    for i in range(len(options)):
        print("{:d}. {:s}".format(i+1, options[i+1]))
        
    choice = 0
    while choice not in options.keys():
        choice = inputOption("Please enter a number: ")
            
    return choice

def toServer(choice):
    if choice == 1:
        localOrWeb = int(input("Would you like to analyze a local file [1] or a remote file [2]? "))
        if (localOrWeb == 1):
            file = input("Name of the local file: ")
            sendFile(file)
        elif (localOrWeb == 2):
            url = input("URL of the remote file: ")
    elif choice == 2:
        name = input("What is the name of the entity you would like a risk report for? ")
        print("Please input any keywords to help refine your report. i.e stocks, twitter, quarterly revenue")
        print("Enter 'done' when finished")
        keywords = []
        keywords.append(name)
        keyword = input("")
        while (keyword != "done"):
            keywords.append(keyword)
            keyword = input("")
    elif choice == 3:
        print("Goodbye")
        
def sendFile(file):
    host = "192.168.0.37" #Temporary host, change later
    port = 5001
    filename = file
    filesize = os.path.getsize(filename)
    print(filesize)
    s = socket.socket()
    print(f"[+] Connecting to {host}:{port}")
    s.connect((host, port))
    print("[+] Connected.")
    s.send(f"{filename}{SEPARATOR}{filesize}".encode())
    # start sending the file
    progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "rb") as f:
        for _ in progress:
            # read the bytes from the file
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                # file transmitting is done
                break
            # we use sendall to assure transimission in 
            # busy networks
            s.sendall(bytes_read)
            # update the progress bar
            progress.update(len(bytes_read))
    # close the socket
    s.close()
        
main()