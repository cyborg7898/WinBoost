import win32com.shell.shell as shell
import subprocess
import os
import time


def go():
    a = input("Please note that this library will delete all temp files, Do you want to continue... (y/n): ")
    if a=='y':
        print(""" 

    █▀ █▀▀ ▄▀█ █▄░█ █▄░█ █ █▄░█ █▀▀ ░ ░ ░
    ▄█ █▄▄ █▀█ █░▀█ █░▀█ █ █░▀█ █▄█ ▄ ▄ ▄
                """)
        time.sleep(4)
        try:
            commands = 'del C:\Windows\Prefetch\*.* /Q'

            shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+commands)
            print(""" 

    █▀█ █▀█ ▀█▀ █ █▀▄▀█ █ ▀█ █ █▄░█ █▀▀   █▀ █▄█ █▀ ▀█▀ █▀▀ █▀▄▀█ ░ ░ ░
    █▄█ █▀▀ ░█░ █ █░▀░█ █ █▄ █ █░▀█ █▄█   ▄█ ░█░ ▄█ ░█░ ██▄ █░▀░█ ▄ ▄ ▄
                """)
            time.sleep(3)
            #For clear TEMP
            os.system("del /q/f/s %TEMP%\*")

            #For clear TEMP
            os.system("del /q/f/s TEMP\*")

            print(""" 

    ░██╗░░░░░░░██╗██╗███╗░░██╗░░░░░░██████╗░░█████╗░░█████╗░░██████╗████████╗███████╗██████╗░
    ░██║░░██╗░░██║██║████╗░██║░░░░░░██╔══██╗██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
    ░╚██╗████╗██╔╝██║██╔██╗██║█████╗██████╦╝██║░░██║██║░░██║╚█████╗░░░░██║░░░█████╗░░██║░░██║
    ░░████╔═████║░██║██║╚████║╚════╝██╔══██╗██║░░██║██║░░██║░╚═══██╗░░░██║░░░██╔══╝░░██║░░██║
    ░░╚██╔╝░╚██╔╝░██║██║░╚███║░░░░░░██████╦╝╚█████╔╝╚█████╔╝██████╔╝░░░██║░░░███████╗██████╔╝
    ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝░░░░░░╚═════╝░░╚════╝░░╚════╝░╚═════╝░░░░╚═╝░░░╚══════╝╚═════╝░
                """)


        except :
            pass
    else:
        print("Thanks for installing our library ;)")
        break
