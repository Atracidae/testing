"""
Arch Install Part 2.

Do Not Run This Program!

"""

import os
import time


def locale():
    to_write = 'LANG=en_US.UTF-8'
    file1 = "/etc/locale.gen"
    file2 = "/etc/locale.conf"
    os.system(f'rm {file1}')
    with open(file1, 'x') as f1:
        f1.write(to_write)
    os.system("locale-gen")
    with open(file2, 'x') as f2:
        f2.write(to_write)


print('Hello')
time.sleep(.5)
os.system("ln -sf /usr/share/zoneinfo/America/New_York")
os.system("hwclock --systohc")
os.system("")
# Need to check if next part is working properly.
locale()
print("finished")
