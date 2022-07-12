import psutil, datetime, time, schedule, openpyxl

# PID from User
pid = int(input("Enter Process ID:"))

# Warning of CPU and VM Percentage
def warning():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > 50:
        print("Cpu usage is above 50%", cpu_usage)

    mem_usage = psutil.virtual_memory().percent
    if mem_usage > 50:
        print("Memory usage is about 50%", mem_usage)


def monitor():
    time = datetime.datetime.now().strftime("%Y%m%d - %H:%M:%S")
    p = psutil.Process(pid)
    cpu = p.cpu_percent(interval=1) / psutil.cpu_percent()

    memory_mb = p.memory_full_info().rss / (1024 * 1024)

    memory = p.memory_percent()

# Export to this file ( EXCEL )
    path = r".\Monitor_result.xlsx"
    file = openpyxl.load_workbook(path)
    sheet = file.active
# Filing in Cells
    sheet.cell(column=1, row=sheet.max_row + 1, value=time)
    sheet.cell(column=2, row=sheet.max_row, value=pid)
    sheet.cell(column=3, row=sheet.max_row, value=cpu)
    sheet.cell(column=4, row=sheet.max_row, value=memory_mb)
    sheet.cell(column=4, row=sheet.max_row, value=memory)
    file.save(path)


schedule.every(1).second.do(warning)
schedule.every(5).seconds.do(monitor)

while True:
    schedule.run_pending()
    time.sleep(1)

