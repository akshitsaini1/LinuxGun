#!/usr/bin/env python
# coding: utf-8

# In[21]:


import os


# In[24]:


def listDisk():
    os.system("fdisk -l")
def createPartition(dev):
    os.system("fdisk {}".format(dev))
def listlvm(vgname,lvname):
    os.system("lvdisplay {}/{}".format(vgname,lvname))
def listalllvm():
    os.system("lvdisplay")
def listvg():
    os.system("vgdisplay")
def mountlvm(lvname,vgname,mounttarget):
    os.system("mount /dev/{}/{} {}".format(vgname,lvname,mounttarget))
def listpv():
    os.system("pvdisplay")
def createpv(dev):
    os.system("pvcreate {}".format(dev))
def createvg(vgname,dev1,dev2):
    os.system("vgcreate {} {} {}".format(vgname,dev1,dev2))
def createlvm(lvname, vgname,size):
    os.system("lvcreate --size {} --name {} {}".format(size,lvname,vgname))
def lvm(dic):
    createpv(dic['dev1'])
    createpv(dic['dev2'])
    createvg(dic['vgname'],dic['dev1'],dic['dev2'])
    createlvm(dic['lvname'],dic['vgname'],dic['size'])
def extendlvm(temp):
    os.system("lvextend --size {} /dev/{}/{}".format(temp['size'],temp['vgname'],temp['lvname']))
    os.system("resize2fs /dev/{}/{}".format(temp['vgname'],temp['lvname']))
def extendvg(temp):
    createpv(temp['dev'])
    os.system("vgextend {} {}".format(temp['vgname'],temp['dev']))


# In[25]:

def lvm_partition():
    print("""Enter ur choice
    1.  list all partitions
    2.  to create partition
    3.  to create lvm
    4.  list lvms
    5.  list volume groups
    6.  list pvs
    7.  extend lvm
    8.  list all lvms
    9.  create pv
    10. extend vg""")
    
    ch=input("enter ur choice\n")
    if ch=="1":
        listDisk()
    elif ch == "2":
            createPartition((input("enter device name")))
    elif ch=="3":
        a={"dev1":input("enter device name: "),"dev2":input("enter second device name: "),"vgname": input("enter ur volume group name: "),"lvname":input("Enter lvm name: "),"size":input("enter size of lv with unit: ")}    
        lvm(a)
    elif ch =="4":
        listlvm(input("enter vgname: "),input("enter lvname: "))
    elif ch=="5":
        listvg()
    elif ch=="6":
        listpv()
    elif ch=="7":
        temp={"size":input("enter the size to increase/decrease: "),"vgname":input("enter volume group name: "),"lvname":input("enter lvm name: ")}   
        extendlvm(temp)
    elif ch=="8":
        listalllvm()
    elif ch=="9":
        createpv(input("enter device name: "))
    elif ch=="10":
        temp={"vgname":input("enter name of vg in which is to be extended: "),"dev":input("enter device name: ")}
        extendvg(temp)
    else:
        print("bad choice")
        exit()


# In[ ]:
#lvm_partition()



