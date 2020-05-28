"""
Arch Install Part 1.

Do Not Run This Program!

Assumes that drive 'sda' has been partitioned.  No need to format.

Drive should be 20G  sda1: 300M,  sda2: 19G

"""

import time
import os
import shutil


os.system("timedatectl set-ntp true")

start = time.time()


def _import_(file_):
    """
    Creates Dictionary for making new and updated mirror list.

    :param file_: incoming text file
    :return: Dictionary representation of given file.
    """
    count = 0
    dict_ = {}
    with open(file_, 'r') as f:
        for i in f:
            dict_[count] = i
            count += 1
    return dict_


def mod_dictionary(dict_):
    count = -1
    _c = -1
    mod_dict_ = {}
    for i in dictionary.values():
        count += 1
        if count < 6:
            _c += 1
            mod_dict_[_c] = i
        if '## United States' in i:
            _c += 1
            mod_dict_[_c] = dict_[count+1]
    return mod_dict_


def to_file(out_file, mod_dict_):
    with open(out_file, 'w') as f:
        for i in mod_dict_.values():
            f.write(i)


file = '/etc/pacman.d/mirrorlist'

shutil.copy2(file, f'{file}copy')

dictionary = _import_(file)

mod_dict = mod_dictionary(dictionary)

file_to_save = '/etc/pacman.d/mirrorlist'

to_file(file_to_save, mod_dict)

print('\n\n\nUpdated /etc/pacman.d/mirrorlist\n\n')


os.system("mkfs.ext4 /dev/sda1")
os.system("mkfs.ext4 /dev/sda2")
os.system("mount /dev/sda2 /mnt")
os.system("mkdir /mnt/boot")
os.system("mount /dev/sda1 /mnt/boot")
print('\nPartitions formatted and mounted base packages installing now\n')
print('Sleeping for 3 seconds.')
time.sleep(3)
os.system("pacstrap /mnt base linux linux-firmware python3 dhcpcd grub git sudo nano vim vi man")
print('Sleeping for 3 seconds.')
time.sleep(3)
os.system("genfstab -U /mnt >> /mnt/etc/fstab")
os.system("arch-chroot /mnt")
os.system("git clone https://github.com/Atracidae/testing.git")


# Seems to fail after going into arch-chroot....
# Perhaps end the file here and start up a new file after using arch-chroot...?

# os.system("arch-chroot /mnt")
end = time.time()
total_time = end - start
print(f'Finished for now!\n....\nThis process took {round(total_time*.0001, 5)} minutes.')
print('It Works!')
exit()
# os.system("")
# Could I perhaps use my existing functions to do this next part with a little bit of modification?




# os.system('fdisk /dev/sda')
# seems that "partx" command could be used here.
# For now will Manually partition the disk
# Should still use Python to format the file system.
