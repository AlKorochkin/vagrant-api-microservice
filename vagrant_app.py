from vagrant import Vagrant
import os
import requests

# vaos.environ["PATH"] += os.pathsep + os.path.join("C:", "HashiCorp", "Vagrant", "bin")

def vagrant_up(path):
    vg = Vagrant()
    vg.up()

def vagrant_destroy(path):
    vg = Vagrant()
    vg.destroy()

if __name__ == "__main__":
    path = "vm_Vagrantfile"
    print("Test vagrant up")
    vagrant_up(path)
    print("Up Done")
    print("Test vagrant down")
    vagrant_destroy(path)
    print("Down Done")