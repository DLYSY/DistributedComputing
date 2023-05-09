from threading import Thread
from os import system



def main(port,_):
    system("rpyc_classic.exe -p {} -q --logfile ./slave.log".format(port))

slaves=[]

for i in range(5):
    slaves.append(Thread(target=main,args=(11811+i,1)))

for i in slaves:
    i.start()

for i in slaves:
    i.join()