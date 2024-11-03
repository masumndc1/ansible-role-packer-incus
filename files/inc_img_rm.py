#!/usr/bin/env python3

import subprocess

out = subprocess.getoutput("sudo incus image list -f csv")

for vm in out.splitlines():
    name = vm.split(",")[0]
    if len(name) == 0:
        rm_img = vm.split(",")[1]
        print("removing image %s" % rm_img)
        subprocess.getoutput("sudo incus image delete %s" % rm_img)
