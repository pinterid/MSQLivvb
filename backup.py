import os
class bcolors:
    HEADER = '\033[95m'
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'
    FAIL = '\033[91m'

mysql_command = 'echo "show databases;" | mysql -u admin -p"password"'
string_databases = os.popen(mysql_command)
for line in string_databases:
        print(bcolors.FAIL)
        line = line.replace('\n','')
        if line != 'Database':
                print(bcolors.HEADER + f"Creating...{line}" + bcolors.ENDC)
                folder_command = f"mkdir -p /mnt/backupshare/{line}"
                os.popen(folder_command)
                print(bcolors.OKGREEN + f"Succesfilly created...{line}" + bcolors.ENDC)
                print(bcolors.HEADER + f"Creating Backup...{line}" + bcolors.ENDC)
                backup_command = f"mysqldump -u backupAdmin -ppassword {line} > /mnt/backupshare/{line}/{line}-$(date +%F).sql"
                os.popen(backup_command)
                print(bcolors.OKGREEN + f"Succesfully created...{line}" + bcolors.ENDC)

print(bcolors.OKGREEN + f"Done...Closing now!" + bcolors.ENDC)