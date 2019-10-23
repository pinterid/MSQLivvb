import os
class bcolors:
    HEADER = '\033[95m'
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'
    FAIL = '\033[91m'

directory_command = f"ls /mnt/backupshare/"
for dir in os.popen(directory_command):
        print(bcolors.FAIL)
        dir = dir.replace('\n','')
        file_command = f"ls /mnt/backupshare/{dir}/ | grep '.sql'"
        for file in os.popen(file_command):
                file = file.replace('\n','')
                database = file.split('-')[0]
                print(bcolors.HEADER + f"Creating Databae...{database}" + bcolors.ENDC)
                database_command = f"echo 'create database {database}' | mysql -u backupAdmin -ppassword"
                os.popen(database_command)
                print(bcolors.OKGREEN + f"Created Database...{database}" + bcolors.ENDC)
                print(bcolors.HEADER + f"Restoring Database...{database}...from...{file}" + bcolors.ENDC)
                restore_command = f"mysql -u backupAdmin -ppassword {database} < /mnt/backupshare/{dir}/{file}"
                os.popen(restore_command)
                print(bcolors.OKGREEN + f"Restored Database...{database}" + bcolors.ENDC)

print(bcolors.GREEN + f"Succesfully restored Databases!" + bcolors.ENDC)
