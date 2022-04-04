#imports
from os import system
import time
import string
import random
import colorama
from datetime import datetime
from colorama import Fore, Back, init
colorama.init(convert=True)

#misc

string.ascii_uppercase
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

string.digits
'01234567'


#startup

print(f'{Fore.LIGHTCYAN_EX}                                  ╔═══════════════════════════════════════════════════╗')
print(f'{Fore.LIGHTCYAN_EX}                                  ║{Fore.LIGHTWHITE_EX}   ▄█  ███▄▄▄▄      ▄████████  ▄█  ███▄▄▄▄    ▄█   {Fore.LIGHTCYAN_EX}║')
print(f'{Fore.LIGHTCYAN_EX}                                  ║{Fore.LIGHTWHITE_EX}  ███  ███▀▀▀██▄   ███    ███ ███  ███▀▀▀██▄ ███   {Fore.LIGHTCYAN_EX}║')
print(f'{Fore.LIGHTCYAN_EX}                                  ║{Fore.LIGHTWHITE_EX}  ███▌ ███   ███   ███    █▀  ███▌ ███   ███ ███▌  {Fore.LIGHTCYAN_EX}║')
print(f'{Fore.LIGHTCYAN_EX}                                  ║{Fore.LIGHTWHITE_EX}  ███▌ ███   ███  ▄███▄▄▄     ███▌ ███   ███ ███▌  {Fore.LIGHTCYAN_EX}║')
print(f'{Fore.LIGHTCYAN_EX}                                  ║{Fore.LIGHTWHITE_EX}  ███▌ ███   ███ ▀▀███▀▀▀     ███▌ ███   ███ ███▌  {Fore.LIGHTCYAN_EX}║')
print(f'{Fore.LIGHTCYAN_EX}                                  ║{Fore.LIGHTWHITE_EX}  ███  ███   ███   ███        ███  ███   ███ ███   {Fore.LIGHTCYAN_EX}║')
print(f'{Fore.LIGHTCYAN_EX}                                  ║{Fore.LIGHTWHITE_EX}  ███  ███   ███   ███        ███  ███   ███ ███   {Fore.LIGHTCYAN_EX}║')
print(f'{Fore.LIGHTCYAN_EX}                                  ║{Fore.LIGHTWHITE_EX}  █▀    ▀█   █▀    ███        █▀    ▀█   █▀  █▀    {Fore.LIGHTCYAN_EX}║')
print(f'{Fore.LIGHTCYAN_EX}                                  ╠═══════════════════════════════════════════════════╣')
print(f'{Fore.LIGHTCYAN_EX}                                  ║{Fore.LIGHTMAGENTA_EX}             infini {Fore.RESET}- {Fore.LIGHTYELLOW_EX}Eth wallet miner             {Fore.LIGHTCYAN_EX}║')
print(f'{Fore.LIGHTCYAN_EX}                                  ╚═══════════════════════════════════════════════════╝')
print()
print(f'{Fore.LIGHTYELLOW_EX}                                  $ {Fore.LIGHTMAGENTA_EX}Eth Address: {Fore.LIGHTGREEN_EX} ', end='')
dep_add = input()

if "0x" in dep_add:
    print()
    ser = random.randint(1,12)

    if ser<10:
        print(f'{Fore.LIGHTBLUE_EX}                                                [Connecting to eu-pub0{ser}]')
    else:
        print(f'{Fore.LIGHTBLUE_EX}                                                [Connecting to eu-pub{ser}]')

    time.sleep(random.uniform(1, 1.5))

    print(f'{Fore.LIGHTGREEN_EX}                                                        [Done!]')
    print()

    time.sleep(random.uniform(0.2, 0.7))

    print(f'{Fore.LIGHTBLUE_EX}                                                 [Loading Wallet List]')
    time.sleep(random.uniform(1, 1.5))

    print(f'{Fore.LIGHTGREEN_EX}                                                        [Done!]')
    print()

    time.sleep(random.uniform(0.2, 0.7))

    print(f'{Fore.LIGHTBLUE_EX}                                                    [Matching Hash]')
    time.sleep(random.uniform(1, 1.5))

    print(f'{Fore.LIGHTGREEN_EX}                                                        [Done!]')
    print()

    time.sleep(random.uniform(0.2, 0.7))

    print(f'{Fore.LIGHTBLUE_EX}                                                    [Comparing HWID]')
    time.sleep(random.uniform(1, 1.5))

    print(f'{Fore.LIGHTGREEN_EX}                                                        [Done!]')
    print()

    time.sleep(random.uniform(0.2, 0.7))

    print(f'{Fore.LIGHTBLUE_EX}                                                  [Importing Proxies]')
    time.sleep(random.uniform(1, 1.5))

    print(f'{Fore.LIGHTGREEN_EX}                                                        [Done!]')
    print()

    system('CLS')

    print(f'{Fore.LIGHTCYAN_EX}                                  ╔═══════════════════════════════════════════════════╗')
    print(f'{Fore.LIGHTCYAN_EX}                                  ║{Fore.LIGHTWHITE_EX}   ▄█  ███▄▄▄▄      ▄████████  ▄█  ███▄▄▄▄    ▄█   {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}                                  ║{Fore.LIGHTWHITE_EX}  ███  ███▀▀▀██▄   ███    ███ ███  ███▀▀▀██▄ ███   {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}                                  ║{Fore.LIGHTWHITE_EX}  ███▌ ███   ███   ███    █▀  ███▌ ███   ███ ███▌  {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}                                  ║{Fore.LIGHTWHITE_EX}  ███▌ ███   ███  ▄███▄▄▄     ███▌ ███   ███ ███▌  {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}                                  ║{Fore.LIGHTWHITE_EX}  ███▌ ███   ███ ▀▀███▀▀▀     ███▌ ███   ███ ███▌  {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}                                  ║{Fore.LIGHTWHITE_EX}  ███  ███   ███   ███        ███  ███   ███ ███   {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}                                  ║{Fore.LIGHTWHITE_EX}  ███  ███   ███   ███        ███  ███   ███ ███   {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}                                  ║{Fore.LIGHTWHITE_EX}  █▀    ▀█   █▀    ███        █▀    ▀█   █▀  █▀    {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}                                  ╠═══════════════════════════════════════════════════╣')
    print(f'{Fore.LIGHTCYAN_EX}                                  ║{Fore.LIGHTMAGENTA_EX}             infini {Fore.RESET}- {Fore.LIGHTYELLOW_EX}eth wallet miner             {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}                                  ╚═══════════════════════════════════════════════════╝')
    print()
    time.sleep(0.03)

    system('CLS')

    print(f'{Fore.LIGHTCYAN_EX}                              ╔═══════════════════════════════════════════════════╗')
    print(f'{Fore.LIGHTCYAN_EX}                              ║{Fore.LIGHTWHITE_EX}   ▄█  ███▄▄▄▄      ▄████████  ▄█  ███▄▄▄▄    ▄█   {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}                              ║{Fore.LIGHTWHITE_EX}  ███  ███▀▀▀██▄   ███    ███ ███  ███▀▀▀██▄ ███   {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}                              ║{Fore.LIGHTWHITE_EX}  ███▌ ███   ███   ███    █▀  ███▌ ███   ███ ███▌  {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}                              ║{Fore.LIGHTWHITE_EX}  ███▌ ███   ███  ▄███▄▄▄     ███▌ ███   ███ ███▌  {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}                              ║{Fore.LIGHTWHITE_EX}  ███▌ ███   ███ ▀▀███▀▀▀     ███▌ ███   ███ ███▌  {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}                              ║{Fore.LIGHTWHITE_EX}  ███  ███   ███   ███        ███  ███   ███ ███   {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}                              ║{Fore.LIGHTWHITE_EX}  ███  ███   ███   ███        ███  ███   ███ ███   {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}                              ║{Fore.LIGHTWHITE_EX}  █▀    ▀█   █▀    ███        █▀    ▀█   █▀  █▀    {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}                              ╠═══════════════════════════════════════════════════╣')
    print(f'{Fore.LIGHTCYAN_EX}                              ║{Fore.LIGHTMAGENTA_EX}             infini {Fore.RESET}- {Fore.LIGHTYELLOW_EX}eth wallet miner             {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}                              ╚═══════════════════════════════════════════════════╝')
    print()
    time.sleep(0.02)

    system('CLS')

    print(f'{Fore.LIGHTCYAN_EX}                          ╔═══════════════════════════════════════════════════╗')
    print(f'{Fore.LIGHTCYAN_EX}                          ║{Fore.LIGHTWHITE_EX}   ▄█  ███▄▄▄▄      ▄████████  ▄█  ███▄▄▄▄    ▄█   {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}                          ║{Fore.LIGHTWHITE_EX}  ███  ███▀▀▀██▄   ███    ███ ███  ███▀▀▀██▄ ███   {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}                          ║{Fore.LIGHTWHITE_EX}  ███▌ ███   ███   ███    █▀  ███▌ ███   ███ ███▌  {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}                          ║{Fore.LIGHTWHITE_EX}  ███▌ ███   ███  ▄███▄▄▄     ███▌ ███   ███ ███▌  {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}                          ║{Fore.LIGHTWHITE_EX}  ███▌ ███   ███ ▀▀███▀▀▀     ███▌ ███   ███ ███▌  {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}                          ║{Fore.LIGHTWHITE_EX}  ███  ███   ███   ███        ███  ███   ███ ███   {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}                          ║{Fore.LIGHTWHITE_EX}  ███  ███   ███   ███        ███  ███   ███ ███   {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}                          ║{Fore.LIGHTWHITE_EX}  █▀    ▀█   █▀    ███        █▀    ▀█   █▀  █▀    {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}                          ╠═══════════════════════════════════════════════════╣')
    print(f'{Fore.LIGHTCYAN_EX}                          ║{Fore.LIGHTMAGENTA_EX}             infini {Fore.RESET}- {Fore.LIGHTYELLOW_EX}eth wallet miner             {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}                          ╚═══════════════════════════════════════════════════╝')
    print()
    time.sleep(0.01)

    system('CLS')

    print(f'{Fore.LIGHTCYAN_EX}                    ╔═══════════════════════════════════════════════════╗')
    print(f'{Fore.LIGHTCYAN_EX}                    ║{Fore.LIGHTWHITE_EX}   ▄█  ███▄▄▄▄      ▄████████  ▄█  ███▄▄▄▄    ▄█   {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}                    ║{Fore.LIGHTWHITE_EX}  ███  ███▀▀▀██▄   ███    ███ ███  ███▀▀▀██▄ ███   {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}                    ║{Fore.LIGHTWHITE_EX}  ███▌ ███   ███   ███    █▀  ███▌ ███   ███ ███▌  {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}                    ║{Fore.LIGHTWHITE_EX}  ███▌ ███   ███  ▄███▄▄▄     ███▌ ███   ███ ███▌  {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}                    ║{Fore.LIGHTWHITE_EX}  ███▌ ███   ███ ▀▀███▀▀▀     ███▌ ███   ███ ███▌  {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}                    ║{Fore.LIGHTWHITE_EX}  ███  ███   ███   ███        ███  ███   ███ ███   {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}                    ║{Fore.LIGHTWHITE_EX}  ███  ███   ███   ███        ███  ███   ███ ███   {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}                    ║{Fore.LIGHTWHITE_EX}  █▀    ▀█   █▀    ███        █▀    ▀█   █▀  █▀    {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}                    ╠═══════════════════════════════════════════════════╣')
    print(f'{Fore.LIGHTCYAN_EX}                    ║{Fore.LIGHTMAGENTA_EX}             infini {Fore.RESET}- {Fore.LIGHTYELLOW_EX}eth wallet miner             {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}                    ╚═══════════════════════════════════════════════════╝')
    print()
    time.sleep(0.01)

    system('CLS')

    print(f'{Fore.LIGHTCYAN_EX}            ╔═══════════════════════════════════════════════════╗')
    print(f'{Fore.LIGHTCYAN_EX}            ║{Fore.LIGHTWHITE_EX}   ▄█  ███▄▄▄▄      ▄████████  ▄█  ███▄▄▄▄    ▄█   {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}            ║{Fore.LIGHTWHITE_EX}  ███  ███▀▀▀██▄   ███    ███ ███  ███▀▀▀██▄ ███   {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}            ║{Fore.LIGHTWHITE_EX}  ███▌ ███   ███   ███    █▀  ███▌ ███   ███ ███▌  {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}            ║{Fore.LIGHTWHITE_EX}  ███▌ ███   ███  ▄███▄▄▄     ███▌ ███   ███ ███▌  {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}            ║{Fore.LIGHTWHITE_EX}  ███▌ ███   ███ ▀▀███▀▀▀     ███▌ ███   ███ ███▌  {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}            ║{Fore.LIGHTWHITE_EX}  ███  ███   ███   ███        ███  ███   ███ ███   {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}            ║{Fore.LIGHTWHITE_EX}  ███  ███   ███   ███        ███  ███   ███ ███   {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}            ║{Fore.LIGHTWHITE_EX}  █▀    ▀█   █▀    ███        █▀    ▀█   █▀  █▀    {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}            ╠═══════════════════════════════════════════════════╣')
    print(f'{Fore.LIGHTCYAN_EX}            ║{Fore.LIGHTMAGENTA_EX}             infini {Fore.RESET}- {Fore.LIGHTYELLOW_EX}eth wallet miner             {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}            ╚═══════════════════════════════════════════════════╝')
    print()
    time.sleep(0.01)

    system('CLS')

    print(f'{Fore.LIGHTCYAN_EX}    ╔═══════════════════════════════════════════════════╗')
    print(f'{Fore.LIGHTCYAN_EX}    ║{Fore.LIGHTWHITE_EX}   ▄█  ███▄▄▄▄      ▄████████  ▄█  ███▄▄▄▄    ▄█   {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}    ║{Fore.LIGHTWHITE_EX}  ███  ███▀▀▀██▄   ███    ███ ███  ███▀▀▀██▄ ███   {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}    ║{Fore.LIGHTWHITE_EX}  ███▌ ███   ███   ███    █▀  ███▌ ███   ███ ███▌  {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}    ║{Fore.LIGHTWHITE_EX}  ███▌ ███   ███  ▄███▄▄▄     ███▌ ███   ███ ███▌  {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}    ║{Fore.LIGHTWHITE_EX}  ███▌ ███   ███ ▀▀███▀▀▀     ███▌ ███   ███ ███▌  {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}    ║{Fore.LIGHTWHITE_EX}  ███  ███   ███   ███        ███  ███   ███ ███   {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}    ║{Fore.LIGHTWHITE_EX}  ███  ███   ███   ███        ███  ███   ███ ███   {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}    ║{Fore.LIGHTWHITE_EX}  █▀    ▀█   █▀    ███        █▀    ▀█   █▀  █▀    {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}    ╠═══════════════════════════════════════════════════╣')
    print(f'{Fore.LIGHTCYAN_EX}    ║{Fore.LIGHTMAGENTA_EX}             infini {Fore.RESET}- {Fore.LIGHTYELLOW_EX}eth wallet miner             {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}    ╚═══════════════════════════════════════════════════╝')
    print()
    time.sleep(0.02)

    system('CLS')

    print(f'{Fore.LIGHTCYAN_EX}  ╔═══════════════════════════════════════════════════╗')
    print(f'{Fore.LIGHTCYAN_EX}  ║{Fore.LIGHTWHITE_EX}   ▄█  ███▄▄▄▄      ▄████████  ▄█  ███▄▄▄▄    ▄█   {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}  ║{Fore.LIGHTWHITE_EX}  ███  ███▀▀▀██▄   ███    ███ ███  ███▀▀▀██▄ ███   {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}  ║{Fore.LIGHTWHITE_EX}  ███▌ ███   ███   ███    █▀  ███▌ ███   ███ ███▌  {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}  ║{Fore.LIGHTWHITE_EX}  ███▌ ███   ███  ▄███▄▄▄     ███▌ ███   ███ ███▌  {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}  ║{Fore.LIGHTWHITE_EX}  ███▌ ███   ███ ▀▀███▀▀▀     ███▌ ███   ███ ███▌  {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}  ║{Fore.LIGHTWHITE_EX}  ███  ███   ███   ███        ███  ███   ███ ███   {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}  ║{Fore.LIGHTWHITE_EX}  ███  ███   ███   ███        ███  ███   ███ ███   {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}  ║{Fore.LIGHTWHITE_EX}  █▀    ▀█   █▀    ███        █▀    ▀█   █▀  █▀    {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}  ╠═══════════════════════════════════════════════════╣')
    print(f'{Fore.LIGHTCYAN_EX}  ║{Fore.LIGHTMAGENTA_EX}             infini {Fore.RESET}- {Fore.LIGHTYELLOW_EX}eth wallet miner             {Fore.LIGHTCYAN_EX}║')
    print(f'{Fore.LIGHTCYAN_EX}  ╚═══════════════════════════════════════════════════╝')
    print()
    time.sleep(1)

    while True:

        now = datetime.now()
        cur_time = now.strftime("%H:%M:%S")

        a_list = [0, 1]
        distribution = [.99, .01]

        chance = random.choices(a_list, distribution)

        s = ''
        chanceint = s.join(map(str, chance))

        addy = ''.join(random.choices(string.ascii_uppercase + string.digits, k=40))
        ether = round(random.uniform(0.01, 12.000), 3)

        if chanceint == '1':
            print(f'{Back.LIGHTGREEN_EX}{Fore.LIGHTCYAN_EX}${Fore.LIGHTWHITE_EX} [{cur_time}] [ETH] [0x{addy}] [WALLET KEY HIT ETH ~ {Back.RESET}{Fore.LIGHTMAGENTA_EX} {ether} {Fore.LIGHTWHITE_EX}{Back.LIGHTGREEN_EX}]{Back.RESET} ')
            time.sleep(0.4)
            print(f'  {Fore.LIGHTYELLOW_EX}$ {Fore.LIGHTBLUE_EX}[Sending Eth to {dep_add}]')
            time.sleep(1.3)
            print(f'  {Fore.LIGHTYELLOW_EX}$ {Fore.LIGHTGREEN_EX}[Done!]')
            time.sleep(0.9)


        else:
            print(f'  {Fore.LIGHTCYAN_EX}${Fore.LIGHTRED_EX} [{cur_time}] [ETH] [0x{addy}] [NO WALLET BAL]{Back.RESET} ')

        print()
        
        time.sleep(random.uniform(0.3,0.6))

if "0x" not in dep_add:
    system('CLS')
    print(f'{Fore.RED}  ╔═══════════════════════════════════════════════════╗')
    print(f'{Fore.RED}  ║{Fore.LIGHTWHITE_EX}   ▄█  ███▄▄▄▄      ▄████████  ▄█  ███▄▄▄▄    ▄█   {Fore.RED}║')
    print(f'{Fore.RED}  ║{Fore.LIGHTWHITE_EX}  ███  ███▀▀▀██▄   ███    ███ ███  ███▀▀▀██▄ ███   {Fore.RED}║')
    print(f'{Fore.RED}  ║{Fore.LIGHTWHITE_EX}  ███▌ ███   ███   ███    █▀  ███▌ ███   ███ ███▌  {Fore.RED}║')
    print(f'{Fore.RED}  ║{Fore.LIGHTWHITE_EX}  ███▌ ███   ███  ▄███▄▄▄     ███▌ ███   ███ ███▌  {Fore.RED}║')
    print(f'{Fore.RED}  ║{Fore.LIGHTWHITE_EX}  ███▌ ███   ███ ▀▀███▀▀▀     ███▌ ███   ███ ███▌  {Fore.RED}║')
    print(f'{Fore.RED}  ║{Fore.LIGHTWHITE_EX}  ███  ███   ███   ███        ███  ███   ███ ███   {Fore.RED}║')
    print(f'{Fore.RED}  ║{Fore.LIGHTWHITE_EX}  ███  ███   ███   ███        ███  ███   ███ ███   {Fore.RED}║')
    print(f'{Fore.RED}  ║{Fore.LIGHTWHITE_EX}  █▀    ▀█   █▀    ███        █▀    ▀█   █▀  █▀    {Fore.RED}║')
    print(f'{Fore.RED}  ╠═══════════════════════════════════════════════════╣')
    print(f'{Fore.RED}  ║{Fore.LIGHTMAGENTA_EX}          infini {Fore.RESET}- {Fore.LIGHTYELLOW_EX}not valid eth address!          {Fore.RED}║')
    print(f'{Fore.RED}  ╚═══════════════════════════════════════════════════╝')
    print()
    time.sleep(1)