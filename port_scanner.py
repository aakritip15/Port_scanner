import socket
import sys
import time
import threading

usage ="python3 portscanner.py TARGET START_PORT END_PORT"

print("*"*3)
print("*"*10)
print("*"*30)
print("YOUR PORT SCANNER")
print("*"*30)
print("*"*10)
print("*"*3)

start_time= time.time()

if(len(sys.argv)!=4):
    print(usage)
    sys.exit()

try:
    target = socket.gethostbyname(sys.argv[1])
    print(target)
except socket.gaierror:
    print("Name resolution error")
    sys.exit()
    
start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

print("Scanning Target", target)

def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3)
    con = s.connect_ex((target,port))
    if(not con):
        print("Port {} is open".format(port))
    s.close()

for port in range(start_port, end_port +1):
    thread = threading.Thread(target= scan_port, args=(port,))
    thread.start()

end_time = time.time()

print("Your scanning time is:",end_time-start_time,"s")
