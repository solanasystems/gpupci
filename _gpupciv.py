#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
lspci の視覚的整形 for Mining GPU
'''
__version__ = '0.0.0' #このスクリプトのバージョン

import sys
import argparse
import subprocess

if __name__ == "__main__":

    PARSER = argparse.ArgumentParser(description='GPU card status of visualized PCI slot', add_help = True)
    PARSER.add_argument( '-b', '--board', nargs=1, metavar='board_name',
                         type=str, default='H81A',help='MotherboardName:TB85 or None(Other)')
    PARSER.add_argument('-v', '--version', action='version',
                        version='%(prog)s {version}'.format(version=__version__))
    ARGS = PARSER.parse_args()

    if ARGS.board[0] == 'TB85':
        COMMAND = "lspci -tv | grep '\[..\]' | grep 'AMD\|NVIDIA' | sed -e 's/^[ ]*//' | sed -e 's/+-01.0-/PCI_1 /' | sed -e 's/+-1c.0-/PCI_2 /' | sed -e 's/+-1c.1-/PCI_3 /' | sed -e 's/+-1c.2-/PCI_4 /' | sed -e 's/+-1c.3-/PCI_5 /' | sed -e 's/+-1c.4-/PCI_6 /' | cut -d' ' -f1,3-"
    else:
        COMMAND = "lspci -tv | grep '\[..\]' | grep 'AMD\|NVIDIA' | sed -e 's/^[ ]*//' | sed -e 's/+-01.0-/PCI_1 /' | sed -e 's/+-1c.0-/PCI_2 /' | sed -e 's/+-1c.1-/PCI_3 /' | sed -e 's/+-1c.2-/PCI_4 /' | sed -e 's/+-1c.4-/PCI_5 /' | sed -e 's/+-1c.5-/PCI_6 /' | cut -d' ' -f1,3-"
        # COMMAND="cat test.txt"

    Existence_1_01 = '\033[33m        '
    Existence_1_02 = '\033[33m        '
    Existence_1_03 = '\033[33m        '
    Existence_1_04 = '\033[33m        '
    Existence_1_05 = '\033[33m        '
    Existence_1_06 = '\033[33m        '
    Existence_1_07 = '\033[33m        '
    Existence_1_08 = '\033[33m        '
    Existence_1_09 = '\033[33m        '
    Existence_1_10 = '\033[33m┌──────┐'
    Existence_1_11 = '\033[33m│      │'
    Existence_1_12 = '\033[33m│ PCI1 │'
    Existence_1_13 = '\033[33m┘      └'
    Existence_1_14 = '\033[33m────────'
    Existence_2_01 = '\033[37m        '
    Existence_2_02 = '\033[37m        '
    Existence_2_03 = '\033[37m        '
    Existence_2_04 = '\033[37m        '
    Existence_2_05 = '\033[37m        '
    Existence_2_06 = '\033[37m        '
    Existence_2_07 = '\033[37m        '
    Existence_2_08 = '\033[37m        '
    Existence_2_09 = '\033[37m        '
    Existence_2_10 = '\033[37m        '
    Existence_2_11 = '\033[37m┌──────┐'
    Existence_2_12 = '\033[37m│ PCI2 │'
    Existence_2_13 = '\033[37m┘      └'
    Existence_2_14 = '\033[37m────────'
    Existence_3_01 = '\033[37m        '
    Existence_3_02 = '\033[37m        '
    Existence_3_03 = '\033[37m        '
    Existence_3_04 = '\033[37m        '
    Existence_3_05 = '\033[37m        '
    Existence_3_06 = '\033[37m        '
    Existence_3_07 = '\033[37m        '
    Existence_3_08 = '\033[37m        '
    Existence_3_09 = '\033[37m        '
    Existence_3_10 = '\033[37m        '
    Existence_3_11 = '\033[37m┌──────┐'
    Existence_3_12 = '\033[37m│ PCI3 │'
    Existence_3_13 = '\033[37m┘      └'
    Existence_3_14 = '\033[37m────────'
    Existence_4_01 = '\033[37m        '
    Existence_4_02 = '\033[37m        '
    Existence_4_03 = '\033[37m        '
    Existence_4_04 = '\033[37m        '
    Existence_4_05 = '\033[37m        '
    Existence_4_06 = '\033[37m        '
    Existence_4_07 = '\033[37m        '
    Existence_4_08 = '\033[37m        '
    Existence_4_09 = '\033[37m        '
    Existence_4_10 = '\033[37m        '
    Existence_4_11 = '\033[37m┌──────┐'
    Existence_4_12 = '\033[37m│ PCI4 │'
    Existence_4_13 = '\033[37m┘      └'
    Existence_4_14 = '\033[37m────────'
    Existence_5_01 = '\033[37m        '
    Existence_5_02 = '\033[37m        '
    Existence_5_03 = '\033[37m        '
    Existence_5_04 = '\033[37m        '
    Existence_5_05 = '\033[37m        '
    Existence_5_06 = '\033[37m        '
    Existence_5_07 = '\033[37m        '
    Existence_5_08 = '\033[37m        '
    Existence_5_09 = '\033[37m        '
    Existence_5_10 = '\033[37m        '
    Existence_5_11 = '\033[37m┌──────┐'
    Existence_5_12 = '\033[37m│ PCI5 │'
    Existence_5_13 = '\033[37m┘      └'
    Existence_5_14 = '\033[37m────────'
    Existence_6_01 = '\033[37m        '
    Existence_6_02 = '\033[37m        '
    Existence_6_03 = '\033[37m        '
    Existence_6_04 = '\033[37m        '
    Existence_6_05 = '\033[37m        '
    Existence_6_06 = '\033[37m        '
    Existence_6_07 = '\033[37m        '
    Existence_6_08 = '\033[37m        '
    Existence_6_09 = '\033[37m        '
    Existence_6_10 = '\033[37m        '
    Existence_6_11 = '\033[37m┌──────┐'
    Existence_6_12 = '\033[37m│ PCI6 │'
    Existence_6_13 = '\033[37m┘      └'
    Existence_6_14 = '\033[37m────────'

    try:
        res = subprocess.getoutput(COMMAND).split('\n')
    except Exception as e:
        sys.stderr.write('Execution of the script failed:%s \n' % e)
    if len(res[0]) != 0:
        for i in res:
            if i.split()[0] == 'PCI_1':
                Existence_1_01 = '\033[33m┌──────┐'
                Existence_1_02 = '\033[33m│      │'
                Existence_1_03 = '\033[33m│      │'
                Existence_1_04 = '\033[33m│      │'
                Existence_1_05 = '\033[33m│      │'
                Existence_1_06 = '\033[33m│      │'
                Existence_1_07 = '\033[33m│      │'
                Existence_1_08 = '\033[33m│ GPU1 │'
                Existence_1_09 = '\033[33m└──────┘'
            elif i.split()[0] == 'PCI_2':
                Existence_2_02 = '\033[37m┌──────┐'
                Existence_2_03 = '\033[37m│      │'
                Existence_2_04 = '\033[37m│      │'
                Existence_2_05 = '\033[37m│      │'
                Existence_2_06 = '\033[37m│      │'
                Existence_2_07 = '\033[37m│      │'
                Existence_2_08 = '\033[37m│      │'
                Existence_2_09 = '\033[37m│ GPU2 │'
                Existence_2_10 = '\033[37m└──────┘'
            elif i.split()[0] == 'PCI_3':
                Existence_3_02 = '\033[37m┌──────┐'
                Existence_3_03 = '\033[37m│      │'
                Existence_3_04 = '\033[37m│      │'
                Existence_3_05 = '\033[37m│      │'
                Existence_3_06 = '\033[37m│      │'
                Existence_3_07 = '\033[37m│      │'
                Existence_3_08 = '\033[37m│      │'
                Existence_3_09 = '\033[37m│ GPU3 │'
                Existence_3_10 = '\033[37m└──────┘'
            elif i.split()[0] == 'PCI_4':
                Existence_4_02 = '\033[37m┌──────┐'
                Existence_4_03 = '\033[37m│      │'
                Existence_4_04 = '\033[37m│      │'
                Existence_4_05 = '\033[37m│      │'
                Existence_4_06 = '\033[37m│      │'
                Existence_4_07 = '\033[37m│      │'
                Existence_4_08 = '\033[37m│      │'
                Existence_4_09 = '\033[37m│ GPU4 │'
                Existence_4_10 = '\033[37m└──────┘'
            elif i.split()[0] == 'PCI_5':
                Existence_5_02 = '\033[37m┌──────┐'
                Existence_5_03 = '\033[37m│      │'
                Existence_5_04 = '\033[37m│      │'
                Existence_5_05 = '\033[37m│      │'
                Existence_5_06 = '\033[37m│      │'
                Existence_5_07 = '\033[37m│      │'
                Existence_5_08 = '\033[37m│      │'
                Existence_5_09 = '\033[37m│ GPU5 │'
                Existence_5_10 = '\033[37m└──────┘'
            elif i.split()[0] == 'PCI_6':
                Existence_6_02 = '\033[37m┌──────┐'
                Existence_6_03 = '\033[37m│      │'
                Existence_6_04 = '\033[37m│      │'
                Existence_6_05 = '\033[37m│      │'
                Existence_6_06 = '\033[37m│      │'
                Existence_6_07 = '\033[37m│      │'
                Existence_6_08 = '\033[37m│      │'
                Existence_6_09 = '\033[37m│ GPU6 │'
                Existence_6_10 = '\033[37m└──────┘'
            else:
                sys.stderr.write("system_error")

    print('{}{}{}{}{}{}'.format(Existence_2_01,Existence_1_01,Existence_3_01,Existence_4_01,Existence_5_01,Existence_6_01))
    print('{}{}{}{}{}{}'.format(Existence_2_02,Existence_1_02,Existence_3_02,Existence_4_02,Existence_5_02,Existence_6_02))
    print('{}{}{}{}{}{}'.format(Existence_2_03,Existence_1_03,Existence_3_03,Existence_4_03,Existence_5_03,Existence_6_03))
    print('{}{}{}{}{}{}'.format(Existence_2_04,Existence_1_04,Existence_3_04,Existence_4_04,Existence_5_04,Existence_6_04))
    print('{}{}{}{}{}{}'.format(Existence_2_05,Existence_1_05,Existence_3_05,Existence_4_05,Existence_5_05,Existence_6_05))
    print('{}{}{}{}{}{}'.format(Existence_2_06,Existence_1_06,Existence_3_06,Existence_4_06,Existence_5_06,Existence_6_06))
    print('{}{}{}{}{}{}'.format(Existence_2_07,Existence_1_07,Existence_3_07,Existence_4_07,Existence_5_07,Existence_6_07))
    print('{}{}{}{}{}{}'.format(Existence_2_08,Existence_1_08,Existence_3_08,Existence_4_08,Existence_5_08,Existence_6_08))
    print('{}{}{}{}{}{}'.format(Existence_2_09,Existence_1_09,Existence_3_09,Existence_4_09,Existence_5_09,Existence_6_09))
    print('{}{}{}{}{}{}'.format(Existence_2_10,Existence_1_10,Existence_3_10,Existence_4_10,Existence_5_10,Existence_6_10))
    print('{}{}{}{}{}{}'.format(Existence_2_11,Existence_1_11,Existence_3_11,Existence_4_11,Existence_5_11,Existence_6_11))
    print('{}{}{}{}{}{}'.format(Existence_2_12,Existence_1_12,Existence_3_12,Existence_4_12,Existence_5_12,Existence_6_12))
    print('{}{}{}{}{}{}'.format(Existence_2_13,Existence_1_13,Existence_3_13,Existence_4_13,Existence_5_13,Existence_6_13))
    print('{}{}{}{}{}{}'.format(Existence_2_14,Existence_1_14,Existence_3_14,Existence_4_14,Existence_5_14,Existence_6_14))

