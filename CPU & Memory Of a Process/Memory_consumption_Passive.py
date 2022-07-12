import psutil

print(f"Total RAM installed : {psutil.virtual_memory().total/1000000000}")

print(f"Available RAM: {psutil.virtual_memory().available/1000000000}")

print(f"Used RAM: {psutil.virtual_memory().used/1000000000}")

print(f"RAM Usage: {psutil.virtual_memory().percent}%")




