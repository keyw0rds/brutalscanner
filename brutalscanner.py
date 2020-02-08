import os, time
# Author : Keyw0rd
# Instagram : _hidayt_ or keyw00rd
# Team : AnonCyberTeam - TEH Squad Cyber
#        Haxor Security - ELITE

#COLOR
BL = "\033[1;36;40m"
RD = "\033[1;31;40m"
WT = "\033[1;37;40m"
GR = "\033[1;32;40m"

os.system('cls')
time.sleep(4)

def banner():
    print(f"\n{BL}           _.------.         {RD}~ {WT}Author : {RD}Keyw0rd")
    print(f"{BL}       _.-`    {RD}('>{BL}.-`'''-.   {RD}~ {WT}Find Files That Access Denied.")
    print(f"{BL} _.---'`       _'`   _ .--.) {RD}~ {WT}Finding an Estimated Virus File.")
    print(f"{BL}   -'         '-.-';`   `")
    print(f"{BL}    ' -      _.'  ``'--. ")
    print(f"{BL}        '---`    .-'''`")
    print(f"{BL}               /`")
    print(f"{BL}----------------")

def remove():
    time.sleep(4)
    option = input(f"{BL}file>{WT} ")
    os.system(f"rm {option}")

def scan_file():
    time.sleep(4)
    os.system('attrib -r -a -s -h *.*')
    time.sleep(4)
    option = input(f"{BL}cmd>{WT} ")
    if option=='scan':
      scan_file()
    elif option=='remove':
      remove()
    elif option=='exit':
      exit()
    else:
        time.sleep(4)
        print(f"{BL}develop> {WT}Result Error...")

def exit():
    time.sleep(4)
    print(f"{BL}develop> {WT}Thanks For Using This Tools.")

def option_select():
    banner()
    time.sleep(4)
    option = input(f"{BL}cmd>{WT} ")
    if option=='scan':
      scan_file()
    elif option=='remove':
      remove()
    elif option=='exit':
      exit()
    else:
        time.sleep(4)
        print(f"{BL}develop> {WT}Result Error...")

option_select()
