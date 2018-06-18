#!/bin/bash
CMDNAME=`basename $0`
SCRIPT_DIR=$(cd $(dirname $0); pwd)
while getopts vh OPT
do
  case $OPT in
    "v" ) VISUAL="VISUAL";;
    "h" ) echo -e "Usage: $CMDNAME [-h] [-v]\n"
          echo -e "GPU card status of PCI slot\n"
          echo -e "  optional arguments:"
          echo -e "  -h, show this help messages and exit"
          echo -e "  -v, Visual mode"
          exit 1;;
    * ) echo "invalid option"
        exit 1;;
  esac
done

BOARD=`cat /sys/devices/virtual/dmi/id/board_name`
echo '[GPU card status of PCI slot] MotherboardName:'$BOARD

if [ "$VISUAL" != "" ]; then
  $SCRIPT_DIR/_gpupciv.py --board "$BOARD"
fi

if [ "$BOARD" = "TB85" ]; then
   lspci -tv | grep '\[..\]' | grep 'AMD\|NVIDIA' | sed -e 's/^[ ]*//' | sed -e 's/+-01.0-/PCI_1 /' | sed -e 's/+-1c.0-/PCI_2 /' | sed -e 's/+-1c.1-/PCI_3 /' | sed -e 's/+-1c.2-/PCI_4 /' | sed -e 's/+-1c.3-/PCI_5 /' | sed -e 's/+-1c.4-/PCI_6 /' | cut -d' ' -f1,3-
else
   lspci -tv | grep '\[..\]' | grep 'AMD\|NVIDIA' | sed -e 's/^[ ]*//' | sed -e 's/+-01.0-/PCI_1 /' | sed -e 's/+-1c.0-/PCI_2 /' | sed -e 's/+-1c.1-/PCI_3 /' | sed -e 's/+-1c.2-/PCI_4 /' | sed -e 's/+-1c.4-/PCI_5 /' | sed -e 's/+-1c.5-/PCI_6 /' | cut -d' ' -f1,3-

fi
