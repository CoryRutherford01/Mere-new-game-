import psutil
import subprocess
import time
import socket

threshold_percentage = 50
included_processes = ['CTFarm.exe']
computer_name = socket.gethostname()

def main():
    while True:
        for process in psutil.process_iter(['name', 'cpu_percent']):
            try:
                if process.info['name'] in included_processes:
                    subprocess.run(['taskkill', '/F', '/IM', process.info['name']], check=True)
            except:
                pass
        time.sleep(10)

if __name__ == "__main__":
    main()
