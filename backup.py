import shutil, os, time

waiting_time = 2

# Load file names
file_name = 'files.txt'

try:
    file = open(file_name, 'r')
except Exception as error:
    print('Cannot Load ' + file_name)
    print(error)
    input()
    quit()

# Convert contents to usable format
contents = file.read()
file.close() # Gotta be friendly

contents = contents.replace('"', '')
dirs = contents.splitlines()

def get_parent(dir):
    for t_index in range(len(dir) - 1):
        index = len(dir) - t_index - 1
        if dir[index] == '/' or dir[index] == '\\':
            new_dir = dir[:index]
            file = dir[index + 1:]
            return new_dir, file


# Backup each file
completed = 0
for dir in dirs:

    if os.path.exists(dir):
        
        parent, self = get_parent(dir)
        backup_folder = parent + '\\' + self + '_Backups'

        # Make backup folder if needed
        if not os.path.exists(backup_folder):
            print('No backup folder for ' + dir + '. Making folder now')
            os.makedirs(backup_folder)

        # Make name
        # Remove ':' from string (Python will complain)
        asctime = time.asctime()
        asctime = asctime.replace(':', '.', 2)

        backup_name = self + ' (' + asctime + ')'

        # Do the backup          
        shutil.copytree(dir, backup_folder + '\\' + backup_name)

        print(dir + ' Completed')
        completed += 1

        
    else:
        print('No such file named ' + dir + '. Skipping this file')

print('Successfully backed up ' + str(completed) + ' file(s)')
time.sleep(waiting_time)

        
