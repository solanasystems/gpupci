Overview of the gpupci.sh command
gpupci.shコマンドの概要

Displays the presence or absence of a GPU card that is inserted into a physical PCI slot on the motherboard.
motherboardの物理的なPCIスロットに、GPUカードが挿入されているか確認するコマンドです。

It is used for the maintenance of rig at a mining factory.
このコマンドは、マイニングセンターで、Rigのメンテナンスに使用できます。

The motherboard is a "H81S" compatible board, or a "TB85".
マザーボードは「H81S」と互換性のあるボードと、「TB85」をサポートします・

The GPU supports Nvidia and AMD.
GPUはNVIDIAとAMDをサポートします。

-----------------------ex.(The GPU is all running in six slots)--------------------
$ scripts/gpupci.sh
[GPU card status of PCI slot] MotherboardName:H81A
PCI_1  Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon RX 470/480/570/580]
PCI_2  Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon RX 470/480/570/580]
PCI_3  Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon RX 470/480/570/580]
PCI_4  Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon RX 470/480/570/580]
PCI_5  Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon RX 470/480/570/580]
PCI_6  Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon RX 470/480/570/580]
-----------------------------------------------------------------------------------

-----------------------ex.(The GPU is not recognized in the second slot.)----------
$ scripts/gpupci.sh
[GPU card status of PCI slot] MotherboardName:Hi-Fi H81S2
PCI_1  Advanced Micro Devices, Inc. [AMD/ATI] Tonga PRO [Radeon R9 285/380]
PCI_3  Advanced Micro Devices, Inc. [AMD/ATI] Tonga PRO [Radeon R9 285/380]
PCI_4  Advanced Micro Devices, Inc. [AMD/ATI] Tonga PRO [Radeon R9 285/380]
PCI_5  Advanced Micro Devices, Inc. [AMD/ATI] Tonga PRO [Radeon R9 285/380]
PCI_6  Advanced Micro Devices, Inc. [AMD/ATI] Tonga PRO [Radeon R9 285/380]
-----------------------------------------------------------------------------------

-----------------------ex.(Visualize with-v option)--------------------------------
$ scripts/gpupci.sh -v
[GPU card status of PCI slot] MotherboardName:Hi-Fi H81S2
        ┌──────┐                                
        │      │┌──────┐┌──────┐┌──────┐┌──────┐
        │      ││      ││      ││      ││      │
        │      ││      ││      ││      ││      │
        │      ││      ││      ││      ││      │
        │      ││      ││      ││      ││      │
        │      ││      ││      ││      ││      │
        │ GPU1 ││      ││      ││      ││      │
        └──────┘│ GPU3 ││ GPU4 ││ GPU5 ││ GPU6 │
        ┌──────┐└──────┘└──────┘└──────┘└──────┘
┌──────┐│      │┌──────┐┌──────┐┌──────┐┌──────┐
│ PCI2 ││ PCI1 ││ PCI3 ││ PCI4 ││ PCI5 ││ PCI6 │
┘      └┘      └┘      └┘      └┘      └┘      └
────────────────────────────────────────────────
PCI_1  Advanced Micro Devices, Inc. [AMD/ATI] Tonga PRO [Radeon R9 285/380]
PCI_3  Advanced Micro Devices, Inc. [AMD/ATI] Tonga PRO [Radeon R9 285/380]
PCI_4  Advanced Micro Devices, Inc. [AMD/ATI] Tonga PRO [Radeon R9 285/380]
PCI_5  Advanced Micro Devices, Inc. [AMD/ATI] Tonga PRO [Radeon R9 285/380]
PCI_6  Advanced Micro Devices, Inc. [AMD/ATI] Tonga PRO [Radeon R9 285/380]
-----------------------------------------------------------------------------------

EOF

