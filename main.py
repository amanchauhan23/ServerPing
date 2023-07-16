import socket
import time
import concurrent.futures

START_SESSION = time.perf_counter()
LIST_OF_IP = []

input ("\nCLOSE ALL FILES: \nhostname_list.txt\nip_output. txt\n\nip_output. txt WILL BE OVERWRITTEN\n\PRESS ENTER, to continue")

with open("hostname_list.txt") as file:
    HOSTNAME_LIST = file.read().splitlines()

def append_to_list(ip):
    LIST_OF_IP.append(ip)
    print(f"{ip.split('@')[1]}@response => {ip}")

# IP lookup from hostname
def resolve_ip(hostname):
    try:
        ip = socket.gethostbyname(hostname)
        append_to_list(f"{hostname}@{ip}\n")
    except socket.gaierror as e:
        err = f"Invalid hostname, error raised {e}"
        append_to_list(f"{hostname}@{err}\n")

# Multi-threading
@lambda _: _() #IIFE
def run_concurrent_threads():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(resolve_ip, HOSTNAME_LIST)

END_SESSION = time.perf_counter()
time_diff = END_SESSION - START_SESSION

print(f"\n\nTime taken: {round(time_diff, 3)} seconds\n # Servers pinged: {len(LIST_OF_IP)}\n")

with open("ip_output.txt", "w") as file:
    file.writelines(LIST_OF_IP)
    print("ip_output.txt updated")

input("\n\nPRESS ENTER, to exit")