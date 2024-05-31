import os
import subprocess
from logger import logger

# Dictionary of commands to be executed with their corresponding titles
commands = {
    "BASIC SUT INFO": {
        "BIOS output": "dmidecode | grep -i Version | head -1",
        "KERNEL version": "uname -a",
        "CORE output": "nproc",
        "PCI list": "lspci",
    },
    "DETAILED SUT INFO": {
        "PCI list": "lspci -vvv",
        "Memory info": "cat /proc/meminfo",
        "DISK output": "fdisk -l",
        "CPU info": "cat /proc/cpuinfo",
        "BIOS output": "dmidecode"
    }
}

# Path to the output file
output_file_path = "/home/system_info"

# Open the output file
with open(output_file_path, "w") as output_file:
    # Iterate over the outer dictionary
    for info_type, command_dict in commands.items():
        output_file.write(f"{info_type}:\n################\n")
        # Iterate over the inner dictionary
        for title, command in command_dict.items():
            try:
                # Execute the command and get the output
                command_output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
                
                # Write the command output to the file
                output_file.write(f"{title}:\n################\n")
                output_file.write(command_output.decode())
                output_file.write("###############################################################################################################################")
                output_file.write("\n\n")
            except subprocess.CalledProcessError as e:
                # If the command fails, write the error to the file
                output_file.write(f"Error occurred while executing '{command}':\n")
                output_file.write(str(e))
                output_file.write("\n\n")
    print("System data collected in one file under home directory with system_info file")
    logger.info('System data collected in one file under home directory with system_info file')
