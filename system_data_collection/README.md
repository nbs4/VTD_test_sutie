This script exemplifies a practical approach to system information gathering, automating what would otherwise be a manual and time-consuming process. 
By executing system commands and capturing their output, it provides a comprehensive snapshot of the system's configuration, which can be invaluable for troubleshooting, system audits, or preparing systems for specific tasks.

As of now it captures 
**"BASIC SUT INFO**": {
        **BIOS output**= command :"dmidecode | grep -i Version | head -1",
        **KERNEL version**= command :"uname -a",
        **CORE output**= command :"nproc",
        **PCI list**= command := command :"lspci",
    }
**"DETAILED SUT INFO"**: {
        "**PCI list**"= command :"lspci -vvv",
        "**Memory info**"= command :"cat /proc/meminfo",
        "**DISK output**"= command :"fdisk -l",
        "**CPU info**"= command :"cat /proc/cpuinfo",
        "**BIOS output**"= command :"dmidecode"
    }
