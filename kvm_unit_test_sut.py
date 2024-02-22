import subprocess
import os
import tempfile
import shutil

list_of_passed_output = []
list_of_failed_output = []

def execute_linux_commands(commands, current_directory):
    for command in commands:
        try:
            ## Super_pages test
            if "smap" in command:
                print("Test to execute Super_pages")
                # Run the command in the shell with the specified working directory
                result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd=current_directory)

                # Print the command output
                print(f"Command: {command}")
                print("Output:")
                print(result.stdout)

                # Print any errors
                # if result.stderr:
                    # output = f"Test failed - Super_pages: {command}"
                    # print(output)
                    # list_of_failed_output.append(output)
                    # print("Errors:")
                    # print(result.stderr)
                if result.stderr:
                    print("Errors:")
                    print(result.stderr)

                # Check the last line for "PASS" or "FAIL"
                last_line = result.stdout.strip().split('\n')[-1]
                # if ("FAIL" or "error") in last_line:
                    # output = f"Test failed - Super_pages: {command}"
                    # print(output)
                    # list_of_failed_output.append(output)
                if result.returncode != 0:
                    output = f"Test failed: {command}"
                    print(output)
                    list_of_failed_output.append(output)
                elif "PASS" in last_line:
                    output = f"Test passed - Super_pages: {command}"
                    print(output)
                    print()
                    list_of_passed_output.append(output)
                else:
                    print(f"Unable to determine test result for command: {command}")
            # Real_Mode test
            elif "realmode" in command:
                print("Test to execute Real_Mode")
                # Run the command in the shell with the specified working directory
                result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd=current_directory)

                # Print the command output
                print(f"Command: {command}")
                print("Output:")
                print(result.stdout)

                # Print any errors
                # if result.stderr:
                    # output = f"Test failed - Super_pages: {command}"
                    # print(output)
                    # list_of_failed_output.append(output)
                    # print("Errors:")
                    # print(result.stderr)
                if result.stderr:
                    print("Errors:")
                    print(result.stderr)

                # Check the last line for "PASS" or "FAIL"
                last_line = result.stdout.strip().split('\n')[-1]
                # if ("FAIL" or "error") in last_line:
                    # output = f"Test failed - Super_pages: {command}"
                    # print(output)
                    # list_of_failed_output.append(output)
                if result.returncode != 0:
                    output = f"Test failed: {command}"
                    print(output)
                    list_of_failed_output.append(output)
                elif "PASS" in last_line:
                    output = f"Test passed - Real_Mode test: {command}"
                    print(output)
                    print()
                    list_of_passed_output.append(output)
                else:
                    print(f"Unable to determine test result for command: {command}")
            # EPT_subpage_protection_L test
            elif "vmx" in command:
                print("Test to execute EPT_subpage_protection_L test")
                # Run the command in the shell with the specified working directory
                result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd=current_directory)

                # Print the command output
                print(f"Command: {command}")
                print("Output:")
                print(result.stdout)

                # Print any errors
                # if result.stderr:
                    # output = f"Test failed - Super_pages: {command}"
                    # print(output)
                    # list_of_failed_output.append(output)
                    # print("Errors:")
                    # print(result.stderr)
                if result.stderr:
                    print("Errors:")
                    print(result.stderr)

                # Check the last line for "PASS" or "FAIL"
                last_line = result.stdout.strip().split('\n')[-1]
                # if ("FAIL" or "error") in last_line:
                    # output = f"Test failed - Super_pages: {command}"
                    # print(output)
                    # list_of_failed_output.append(output)
                if result.returncode != 0:
                    output = f"Test failed: {command}"
                    print(output)
                    list_of_failed_output.append(output)
                elif "PASS" in last_line:
                    output = f"Test passed - EPT_subpage_protection_L test: {command}"
                    print(output)
                    print()
                    list_of_passed_output.append(output)
                else:
                    print(f"Unable to determine test result for command: {command}")
            # IR_QI_L test
            elif "intel_iommu" in command:
                print("Test to execute IR_QI_L")
                # Run the command in the shell with the specified working directory
                result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd=current_directory)

                # Print the command output
                print(f"Command: {command}")
                print("Output:")
                print(result.stdout)

                # Print any errors
                # if result.stderr:
                    # output = f"Test failed - Super_pages: {command}"
                    # print(output)
                    # list_of_failed_output.append(output)
                    # print("Errors:")
                    # print(result.stderr)
                if result.stderr:
                    print("Errors:")
                    print(result.stderr)

                # Check the last line for "PASS" or "FAIL"
                last_line = result.stdout.strip().split('\n')[-1]
                # if ("FAIL" or "error") in last_line:
                    # output = f"Test failed - Super_pages: {command}"
                    # print(output)
                    # list_of_failed_output.append(output)
                if result.returncode != 0:
                    output = f"Test failed: {command}"
                    print(output)
                    list_of_failed_output.append(output)
                elif "PASS" in last_line:
                    output = f"Test passed - IR_QI_L test: {command}"
                    print(output)
                    print()
                    list_of_passed_output.append(output)
                else:
                    print(f"Unable to determine test result for command: {command}")
            # 5_level_page_table test
            elif "access" in command:
                print("Test to execute 5_level_page_table")
                # Run the command in the shell with the specified working directory
                result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd=current_directory)

                # Print the command output
                print(f"Command: {command}")
                print("Output:")
                print(result.stdout)

                # Print any errors
                # if result.stderr:
                    # output = f"Test failed - Super_pages: {command}"
                    # print(output)
                    # list_of_failed_output.append(output)
                    # print("Errors:")
                    # print(result.stderr)
                if result.stderr:
                    print("Errors:")
                    print(result.stderr)

                # Check the last line for "PASS" or "FAIL"
                last_line = result.stdout.strip().split('\n')[-1]
                # if ("FAIL" or "error") in last_line:
                    # output = f"Test failed - Super_pages: {command}"
                    # print(output)
                    # list_of_failed_output.append(output)
                if result.returncode != 0:
                    output = f"Test failed: {command}"
                    print(output)
                    list_of_failed_output.append(output)
                elif "PASS" in last_line:
                    output = f"Test passed - 5_level_page_table test: {command}"
                    print(output)
                    print()
                    list_of_passed_output.append(output)
                else:
                    print(f"Unable to determine test result for command: {command}")
            else:
                # Run the command in the shell with the specified working directory
                result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd=current_directory)

                # Print the command output
                print(f"Command: {command}")
                print("Output:")
                print(result.stdout)

                # Print any errors
                if result.stderr:
                    print("Errors:")
                    print(result.stderr)

                # Check if the command contains "FAIL"
                if "FAIL" in result.stdout:
                    print(f"Test failed: {command}")
                else:
                    print(f"Test passed: {command}")
            
        except subprocess.CalledProcessError as e:
            # Handle command execution errors
            print(f"Error executing command '{command}': {e}")

def unzip_and_execute_commands(zip_file_path, commands_to_execute):
    try:
        #Home directory to download and extract the contents
        home_dir = "/home/"
        file_name = os.path.basename(file_url)
        
        # Check if the file already exists in /home/
        target_file_path = os.path.join(home_dir, file_name)
        if not os.path.exists(target_file_path):
            # Download the file using wget to /home/
            download_command = f"wget --timeout=30 --tries=3 --quiet --show-progress --directory-prefix={home_dir} {file_url}"
            subprocess.run(download_command, shell=True, check=True)

        # Get the downloaded file name
        downloaded_file = os.path.join(home_dir, file_name)
        print(downloaded_file)

        # Unzip the file
        if downloaded_file.endswith(".tar.gz") or downloaded_file.endswith(".tar"):
            extract_command = f"tar -xvf {downloaded_file}"
        elif downloaded_file.endswith(".zip"):
            extract_command = f"unzip -q {downloaded_file}"
        else:
            print("Unsupported archive format.")
            return

        # Execute the extraction command
        subprocess.run(extract_command, shell=True, check=True)

        # Find the untarred path
        untarred_path = os.path.join(home_dir, os.path.splitext(file_name)[0])
        print(untarred_path)

        # Execute commands inside the untarred folder
        execute_linux_commands(commands_to_execute, untarred_path)
        
        print(f"list_of_passed_output = {list_of_passed_output}")
        print(f"list_of_failed_output = {list_of_failed_output}")

    except subprocess.CalledProcessError as e:
        # Handle extraction or command execution errors
        print(f"Error: {e}")


# Example usage
file_url = "https://ubit-artifactory-ba.intel.com/artifactory/dcg-dea-srvplat-local/Automation_Tools/SRF/Linux/kvm-unit-tests-master.tar"
commands_to_execute = ["ls -la","chmod -R 777 *", "./configure", "make standalone","./tests/vmx","./tests/smap","./tests/realmode","./tests/intel_iommu","./tests/access"]

# Unzip the file and execute commands inside the untarred folder
unzip_and_execute_commands(file_url, commands_to_execute)
