import time
import psutil


# print(f"Number Of Physical Cores : {psutil.cpu_count(logical=False)}")
# print(f"Number Of Physical Cores : {psutil.cpu_count(logical=True)}")
#
# print(f"Current CPU Frequency : {psutil.cpu_freq().current}")
# print(f"Current CPU Frequency : {psutil.cpu_freq().min}")
# print(f"Current CPU Frequency : {psutil.cpu_freq().max}")
#
# print(f"Current CPU utilization : {psutil.cpuprint(f"Current per-CPU utilization : {psutil.cpu_percent(interval=1, percpu=True)}")_percent(interval=1)}")
#

def display_usage(cpu_usage, mem_usage, bars=50):
    cpu_percent = (cpu_usage / 100.0)
    cpu_bar = '' * int(cpu_percent * bars) + '_' * (bars - int(cpu_percent * bars))

    mem_percent = (mem_usage / 100.0)
    mem_bar = '' * int(mem_percent * bars) + '_' * (bars - int(mem_percent * bars))

    print(f"\rCPU Usage: |{cpu_bar}| {cpu_usage:.2f}% ", end="")
    print(f"MEM Usage: |{mem_bar}| {mem_usage:.2f}% ", end="")


while True:
    display_usage(psutil.cpu_percent(), psutil.virtual_memory().percent, 30)
    time.sleep(0.5)