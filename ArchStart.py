"""
Arch Install Part 1.

Do Not Run This Program!

Assumes that drive 'sda' has been partitioned.  No need to format.

Drive should be 20G  sda1: 300M,  sda2: 19G

"""


import os
import shutil


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

os.system("datetimectl set-ntp true")
os.system("mkfs.ext4 /dev/sda1")
os.system("mkfs.ext4 /dev/sda2")
os.system("mount /dev/sda2 /mnt")
os.system("mkdir /mnt/boot")
os.system("mount /dev/sda1 /mnt/boot")

print('Partitions formatted and mounted')



# os.system('fdisk /dev/sda')
# seems that "partx" command could be used here.
# For now will Manually partition the disk
# Should still use Python to format the file system.
