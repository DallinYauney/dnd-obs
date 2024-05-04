from health import parse_data
from time import sleep

print("Initializing file writer")

def write_file():
    # write data to health.txt file
    health_nums = parse_data().split(" ")
    f = open("health.txt", "w")
    bonusHP = ""
    if int(health_nums[2]) > 0:
        bonusHP = f" (+{health_nums[2]})"
    f.write(f"{health_nums[0]}/{health_nums[1]}{bonusHP}")
    return health_nums

while True:
    print(f"File written: {write_file()}")
    sleep(1)