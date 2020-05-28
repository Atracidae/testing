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


def net():
    host_name = input('Please Enter a HostName for system.')
    with open('/etc/hostname', 'x') as f3:
        f3.write(host_name)
    with open('/etc/hosts', 'a') as f4:
        f4.write(f"127.0.0.1     localhost")
        f4.write(f"::1           localhost")
        f4.write(f"127.0.1.1     {host_name}.localdomain {host_name}")







print('Hello')
time.sleep(.5)
os.system("ln -sf /usr/share/zoneinfo/America/New_York")
os.system("hwclock --systohc")
os.system("")
# Need to check if next part is working properly.
locale()
print("Finished!")
a = 12
