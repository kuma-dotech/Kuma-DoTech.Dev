"""
Project     : System Monitor
Author      : kuma-dotech
Description : Check CPU & RAM Usage
    """

# System Health Monitor v1.0
# Built for Kuma-DoTech.dev internal resource tracking.
# Focused on lightweight execution and real-time analytics.
import psutil
import time

def monitor_system():
    print("--- Pro-Automation System Monitor ---")
    try:
        while True:
            cpu = psutil.cpu_percent(interval=1)
            ram = psutil.virtual_memory().percent
            print(f"CPU Usage: {cpu}% | RAM Usage: {ram}%", end="\r")
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

if __name__ == "__main__":
    monitor_system()
