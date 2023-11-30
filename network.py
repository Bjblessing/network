import subprocess
import socket
import os
from datetime import datetime

def get_serial_and_top_level_number():
    serial_number = input("Enter system Serial Number: ")
    top_level_number = input("Enter Top Level Number: ")
    return serial_number, top_level_number

def log_data(filename, data):
    with open(filename, 'a') as file:
        file.write(data + '\n')

def ping_host(ip_address):
    try:
        result = subprocess.check_output(
            ["ping", ip_address],
            stderr=subprocess.STDOUT,
            text=True
        )
        return result
    except subprocess.CalledProcessError as e:
        return e.output

def main():
    # Get Serial Number and Top Level Number from the user
    serial_number, top_level_number = get_serial_and_top_level_number()

    # Generate a unique log filename based on the current date and time
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    log_filename = f"log_{timestamp}.txt"

    # Log Serial Number and Top Level Number
    log_data(log_filename, f"Serial Number: {serial_number}")
    log_data(log_filename, f"Top Level Number: {top_level_number}")

    # Get local machine's IP address
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    log_data(log_filename, f"Local IP Address: {ip_address}")

    # Ping the IP address and log the results
    ping_result = ping_host(ip_address)
    log_data(log_filename, "Ping Results:")
    log_data(log_filename, ping_result)

    print(f"Log file '{log_filename}' created with the requested information.")

if __name__ == "__main__":
    main()
