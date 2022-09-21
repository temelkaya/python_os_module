import os 

dir(os)

help(os)

os.system("ls -l")

x = os.system("ls -l")  (What is difference in the output)

os.system("pwd")

os.getcwd() (Will return same output)

os.chdir("/tmp")    (Change directory)

os.system("ls -l")  

os.listdir(). (It will give the output in form of list and you itirate over the list)

for i in os.listdir():
...     print(i)

If you don't pass any parameter it will take current directory. 

os.listdir("/etc")

Create new file

os.mknod("testfileviaosmodule")

os.mkdir("testdir")

If you want to create directories recursively 

os.mkdir("test1/test2") will throw an exception

os.makedirs("test1/test2")


In Linux there is ENV command to list environment variables 

os.environ

if you're looking for specific value:     os.environ.get("HOME")


in Linux we have command ID

os.getuid()

os.getgid()

os.rmdir("test1") --> will throw error

os.rmdir("test1/test2")

os.removedirs()

dir(os.path)
os.path.exists("/etc/hosts")
os.path.exists("/etc/hostsss")
os.path.isfile("/etc/hosts")
os.path.isdir("/etc/hosts")
os.path.isdir("/etc")
os.path.islink("/etc/resolv.conf")
os.path.getsize("/etc/hosts")