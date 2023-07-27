
import time
import datetime
# int(time.mktime(time.strptime("2023-07-14 15:51:24"))) - time.timezone

def conversor(date):
    # 2023-07-14
    timing = datetime.datetime.strptime(date,"%Y-%m-%d")
    return int(time.mktime(time.strptime(f"{timing}"))) - time.timezone

def main():
    date = input("digite uma data no formato yy-mm-dd: ")
    timestamp = conversor(date)

    print(f"o timestamp atual agora é {timestamp}")

main()