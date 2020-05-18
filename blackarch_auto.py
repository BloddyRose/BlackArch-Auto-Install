#!/usr/bin/env python3 


# Modules but os don't need because not opening files
try:
	import pyfiglet
	from pyfiglet import Figlet
	import os 
	import sys
	from colorama import Fore, Style, Back
except: 
	print("No Modules Found View Source code")

if os.getuid() != 0:
	print("Sorry, run with sudo python3 blackarch_auto.py ")
	sys.exit()

# Functions and loop

'''
   The main function is init it have one loop so if you have an idea 
   aplly it but send an email with the source code to upload
'''

'''
   Thankx y0u f0r using!!!
'''

# Info is about me and my logo (Internet : https://www.asciiart.eu) 
def info():

   print(f"""{Back.BLACK}
      ______________________________________________________________

      \033----> Email >> bloddy.rose.404@gmail.com              
      \033----> Github >> https://github.com/BloddyRose
      \033----> It took me time to make so leave a star or like 
      ______________________________________________________________


      {Style.RESET_ALL}

      """)
# Main funcion print my name at the end

def main():
   banner = Figlet(font='speed')
   print(banner.renderText(' BloddyRose'))



def help():
   print(f"{Back.BLUE}You can use this commands:! {Style.RESET_ALL}")
   print(f"{Back.BLUE}sudo pacman -Sgg | grep blackarch | cut -d' ' -f2 | sort -u >> List all Hacking tools{Style.RESET_ALL}\n")
   print(f"{Back.BLUE}sudo pacman -S blackarch >> Installs al tools (Not recommend take time on slow pc!){Style.RESET_ALL}\n")
   print(f"{Back.BLUE}sudo pacman -Sg | grep blackarch >> Lists by Categories!{Style.RESET_ALL}\n")
   print(f"{Back.BLUE}sudo pacman -S blackarch-<category> >> where category is a name of category!!{Style.RESET_ALL}\n")

   print(f"""{Back.BLUE}# Note - it maybe be necessary to overwrite certain packages when installing blackarch tools. \n

# If you experience "failed to commit transaction" errors, use the --needed and --overwrite switches\n
# For example: \n
$ sudo pacman -Syyu --needed blackarch --overwrite='*'{Style.RESET_ALL}\n""")

# Init does it all work with while loop to keep in program

def init():

   print(f"{Back.RED} Hello to BlackArch install on Manjaro!{Style.RESET_ALL}\n")
   print(f"{Back.RED} Only for kiddies!{Style.RESET_ALL}\n")
   
   print(f"{Back.YELLOW}Do you want to install? {Style.RESET_ALL}\n")
   
   ch1 = input(f"{Back.GREEN}Enter [1 >> yes or 2 >> no or 3 >> Author or 4 >> Information (Recommand to see after installation!)] {Style.RESET_ALL}: ")
 # This is the loop I created with colorama not hard print statements   
   while ch1 == '1' :
      print(f"{Back.WHITE}1. Download Strap.sh\n{Style.RESET_ALL}")
      print(f"{Back.WHITE}2. Permission and execute!\n{Style.RESET_ALL}")
      print(f"{Back.WHITE}3. Blackman!\n{Style.RESET_ALL}")
      print(f"{Back.WHITE}4. Back\n{Style.RESET_ALL}")

      answer = input(f"{Back.GREEN}Enter 1/2/3/4: {Style.RESET_ALL}")

      if answer == '1' :
         print(f"{Back.RED}Downloading...{Style.RESET_ALL}")
         print("\n")
         os.system("curl -O https://blackarch.org/strap.sh")
         print(f"{Back.BLUE}Finished...{Style.RESET_ALL}")
      elif answer == '2' :
         print(f"{Back.GREEN}Setting Permission...{Style.RESET_ALL}")
         print("\n")
         os.system("chmod +x strap.sh && ./strap.sh")
         print(f"{Fore.RED}Take a while... Wait{Style.RESET_ALL}")
         print(f"{Back.BLUE}Finished...{Style.RESET_ALL}")
      elif answer == '3' :
         print(f"{Back.RED}Installing Blackman...{Style.RESET_ALL}")
         print("\n")
         os.system("sudo pacman -Syu blackman")
         print(f"{Back.BLUE}Finished...{Style.RESET_ALL}")

      elif answer == '4' :
         init()
   if ch1 == '2' :

      print(f"{Back.BLUE}Godbye...)({Style.RESET_ALL}")
      main()
      sys.exit();
   elif ch1 == '3' :
      info()
   elif ch1 == '4' :
      help()

   else: 
      print(f"{Back.RED}I don/'t know that command{Style.RESET_ALL}\n")

      init()

init()


