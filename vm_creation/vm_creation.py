import subprocess
import time
import os
import re
import threading
import glob

SUT_RAW_IMG_IMAGE_LOCATION = "/home/CENTOS_img/"

def find_latest_img_file(directory="/home/raw_img"):
    list_of_files = glob.glob(os.path.join(directory, '*.img'))
    if not list_of_files:
        raise FileNotFoundError("No .img files found in the directory: {}".format(directory))
    latest_file = max(list_of_files, key=os.path.getctime)
    return os.path.basename(latest_file)
    
def input_with_timeout(prompt, timeout=5, default='4'):
    def user_input(queue):
        queue.put(input(prompt))

    queue = queue.Queue()
    input_thread = threading.Thread(target=user_input, args=(queue,))
    input_thread.daemon = True
    input_thread.start()

    try:
        # Wait for input or timeout
        return queue.get(block=True, timeout=timeout)
    except queue.Empty:
        return default

def launch_qemu_vm(img_file, num_vms, num_cpus):
    for i in range(num_vms):        
        vm_name = "CENTOS_{}".format(i)
        target_file_path = os.path.join(SUT_RAW_IMG_IMAGE_LOCATION, vm_name)
        if not os.path.exists(target_file_path):
            download_command = "mkdir -p {}".format(target_file_path)
            subprocess.run(download_command, shell=True, check=True)

        cp_cmd = "cp /home/rawimg/{} /{}/".format(img_file, target_file_path)
        subprocess.run(cp_cmd, shell=True, check=True)

        mkdir_cmd = "rm -f {}/{}_launch.exp;".format(target_file_path, vm_name)
        subprocess.run(mkdir_cmd, shell=True, check=True)

        touch_cmd = "touch {}/{}_launch.exp;".format(target_file_path, vm_name)
        subprocess.run(touch_cmd, shell=True, check=True)

        vm_launch_filepath = "{}/{}_launch.exp".format(target_file_path, vm_name)

        qemu_cmd = "/usr/libexec/qemu-kvm -name {} -machine q35 -enable-kvm -global kvm-apic.vapic=false -m 8192 -cpu host -drive format=raw,file=/home/CENTOS_{}_img/{} -bios /usr/share/qemu/OVMF.fd -object iommufd,id=iommufd0 -device intel-iommu,caching-mode=on,dma-drain=on,x-scalable-mode=modern,x-pasid-mode=true,device-iotlb=on,iommufd=iommufd0 -smp {} -serial mon:stdio -nic user,hostfwd=tcp::{}-:22 -nographic".format(vm_name,i, img_file, num_cpus, 2222+i)
        
        print(qemu_cmd)

        vmlaunch_content = "echo '#!/usr/bin/expect -f' >> {};" \
                               "echo 'set timeout -1'  >> {};" \
                               "echo 'spawn {}' >> {};" \
                               "echo 'expect \"login: \"' >> {};" \
                               "echo 'send \"root\\n\"' >> {};" \
                               "echo 'expect {}' >> {};" \
                               "echo '\"Password:*\" {} send \"password\\n\" {}' >> {};" \
                               "echo '\"# \" {} send \"\\n\" {}' >> {};" \
                               "echo '{}' >> {};" \
                               "echo 'expect \"# \"' >> {};" \
                               "echo 'send \"passwd root\\n\"' >> {};" \
                               "echo 'expect \"*password:\"' >> {};" \
                               "echo 'send \"password\\n\"' >> {};" \
                               "echo 'expect \"*password:\"' >> {};" \
                               "echo 'send \"password\\n\"' >> {};".format(vm_launch_filepath, vm_launch_filepath, qemu_cmd,
                                                                 vm_launch_filepath, vm_launch_filepath, vm_launch_filepath,
                                                                 "{",
                                                                 vm_launch_filepath, "{", "}", vm_launch_filepath,
                                                                 "{", "}", vm_launch_filepath, "}", vm_launch_filepath,
                                                                 vm_launch_filepath, vm_launch_filepath, vm_launch_filepath,
                                                                 vm_launch_filepath, vm_launch_filepath, vm_launch_filepath,
                                                                 vm_launch_filepath)
                                                                 
        subprocess.run(vmlaunch_content, shell=True, check=True)
        
        vmlaunch_content =  "echo 'interact' >> {};".format(vm_launch_filepath)
        subprocess.run(vmlaunch_content, shell=True, check=True)
        
        chmod_cmd = "chmod 777 {}".format(vm_launch_filepath)
        subprocess.run(chmod_cmd, shell=True, check=True)
            
        screen_cmd = "screen -dmS CENTOS_{}_scr bash -c '{}'".format(i,vm_launch_filepath)
        subprocess.run(screen_cmd, shell=True, check=True)
        
        time.sleep(100)

def ssh_and_execute_command(num_vms, num_cpus):
    for i in range(num_vms):
        ssh_cmd = 'sshpass -p "password" ssh -o StrictHostKeyChecking=no -p {} root@localhost "hostnamectl"'.format(2222+i)
        while True:
            ssh_process = subprocess.Popen(ssh_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = ssh_process.communicate()
            if ssh_process.returncode == 0:
                output = stdout.decode()
                print(output)
                break
            else:
                print("SSH connection failed, retrying in 5 seconds...")
                time.sleep(5)
        
        ssh_cmd = 'sshpass -p "password" ssh -o StrictHostKeyChecking=no -p {} root@localhost "lscpu"'.format(2222+i)
        while True:
            ssh_process = subprocess.Popen(ssh_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = ssh_process.communicate()
            if ssh_process.returncode == 0:
                output = stdout.decode()
                print(output)
                cpu_pattern = re.compile(r'^CPU\(s\):.*$', re.MULTILINE)
                # Search for the pattern in the output
                match = cpu_pattern.search(output)
                if match:
                    # If the pattern is found, extract the number of CPUs
                    actual_num_cpus = int(match.group(0).split(':')[1].strip())
                    if actual_num_cpus == num_cpus:
                        print("The number of CPUs is correct with user given and vm created")
                    else:
                        print("The number of CPUs is incorrect. Expected: {}, Actual: {}".format(num_cpus, actual_num_cpus))
                else:
                    # If the pattern is not found, print that the information is not available
                    print("The output does not contain information about the number of CPUs.")
                break
            else:
                print("SSH connection failed, retrying in 5 seconds...")
                time.sleep(5)
        
try:
    img_file = find_latest_img_file()  # Dynamically find the latest img file
    num_vms = 1
    num_cpus_input = input_with_timeout("Enter the number of CPU with vm need to create (default 4): ", 5, '4')
    num_cpus = int(num_cpus_input)
    launch_qemu_vm(img_file, num_vms, num_cpus)
    # Wait for the VM to boot up before trying to connect via SSH
    time.sleep(100)
    ssh_and_execute_command(num_vms, num_cpus)
except Exception as ex:
    print(ex)
finally:
    kill_cmd = "pkill -f qemu"
    subprocess.run(kill_cmd, shell=True, check=True)
    
   
